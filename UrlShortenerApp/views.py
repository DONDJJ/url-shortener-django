from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateResponseMixin, TemplateView
from django.views.generic.edit import ProcessFormView, FormView

from .forms import EnterUrlForm
from .models import ShortenedUrl, UrlClick
from UserApp.models import User
from PetProject.settings import SITE_BASE_URL
from django.urls import reverse_lazy
from datetime import date, timedelta


class CreateUrlView(FormView):
    template_name = 'UrlShortenerApp/create_url.html'
    form_class = EnterUrlForm

    def get(self, request, *args, **kwargs):
        """Выполняется при GET запросе, в самом начале"""
        prev_url = request.GET.get('url', None)  # извлечение GET параметра - предыдущего созданного URL
        form = EnterUrlForm()
        self.request = request
        return render(request, 'UrlShortenerApp/create_url.html',
                      {'form': form, 'current_user': request.user, 'user_logged_in': request.user.is_authenticated,
                       "prev_url": prev_url})

    def form_valid(self, form):
        """Обработка введенных в форму данных"""
        su = ShortenedUrl()
        if isinstance(self.request.user, User):  # проверка анонимности юзера
            su.save(self.request.user, form.cleaned_data['user_original_url'])
        else:
            su.save(User.objects.get(pk=1), form.cleaned_data['user_original_url'])
        prev_url = su.new_short_url
        return HttpResponseRedirect(self.get_success_url(prev_url=prev_url))
        # return super().form_valid(form)  # базовая версия этого метода, перенаправление по адресу,
        # # возвращаемому ф-ей get_success_url()

    def get_success_url(self, prev_url):
        """Return the URL to redirect to after processing a valid form."""
        return f'/urls/create_url/?url={prev_url}'


def shorted_url_handler(request):
    """
    Обработчик сокращенных адресов.
    Вызывается каждый раз при переходе по сокращенной ссылке и подставляет
    в адресную строку исходную ссылку
    """
    request_url = request.get_full_path()
    final_url = SITE_BASE_URL + request_url[1:]
    # return HttpResponse(final_url)
    original_URL_fromDB = ShortenedUrl.objects.get(new_short_url=final_url)
    u = UrlClick()
    u.related_url = original_URL_fromDB
    u.save()
    # return HttpResponseRedirect(original_URL_fromDB.original_url,status=404)
    return redirect(original_URL_fromDB.original_url)


def change_url_status_view(request, url_for_delete):
    """
    Если ссылка неактивна - делает ее активной и наоборот
    """
    if ShortenedUrl.objects.get(pk=url_for_delete).is_active:
        ShortenedUrl.objects.filter(pk=url_for_delete).update(is_active=False)
        return redirect('profile_url')
    else:
        ShortenedUrl.objects.filter(pk=url_for_delete).update(is_active=True)
        return redirect('hidden_urls_url')


def statistic_about_url(request, url_for_stat):
    all_clicks = UrlClick.objects.filter(related_url=ShortenedUrl(pk=url_for_stat)).count()
    delta = timedelta(days=1)
    today = date.today()
    list_of_30_days = [today - delta * i for i in range(30)]  # 30 предыдущих дней начиная с сегодняшнего
    full_stat = {datestring: len(count_of_clicks) for
                 datestring, count_of_clicks in
                 zip(
                     list_of_30_days,
                     [UrlClick.objects.filter(
                         related_url=ShortenedUrl(pk=url_for_stat),
                         click_date=day
                     ) for day in list_of_30_days
                     ]
                 )
                 }
    return render(request, 'UrlShortenerApp/statistic.html', {'full_stat': full_stat.items(),
                                                              'request': request,
                                                              'current_user': request.user,
                                                              'user_logged_in': request.user.is_authenticated})
