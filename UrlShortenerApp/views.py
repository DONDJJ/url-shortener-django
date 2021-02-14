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


class CreateUrlView(FormView):
    template_name = 'UrlShortenerApp/create_url.html'
    form_class = EnterUrlForm

    def get(self, request, *args, **kwargs):
        """Выполняется при GET запросе, в самом начале"""
        prev_url = request.GET.get('url', None)  # извлечение GET параметра - предыдущего созданного URL
        form = EnterUrlForm()
        self.request = request
        return render(request, 'UrlShortenerApp/create_url.html',
                      {'form': form, "prev_url": prev_url})

    def form_valid(self, form):
        """Обработка введенных в форму данных"""
        su = ShortenedUrl()
        su.save(self.request.user, form.cleaned_data['user_original_url'])
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
    original_URL_fromDB = ShortenedUrl.get_full_url_from_requested(request)
    u = UrlClick(related_url=original_URL_fromDB)
    return redirect(original_URL_fromDB.original_url)


def change_url_status_view(request, url_for_delete):
    """
    Если ссылка неактивна - делает ее активной и наоборот
    """
    success_url = ShortenedUrl.objects.get(pk=url_for_delete).change_active_status()
    return redirect(success_url)


def statistic_about_url(request, url_for_stat):
    """Получение статистики для ссылки за последние 30 дней"""
    statistic = UrlClick.get_statistic_for_url(url_for_stat=url_for_stat)
    return render(request, 'UrlShortenerApp/statistic.html', {'full_stat': statistic})
