from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import EnterUrlForm
from .models import ShortenedUrl
from UserApp.models import User
from PetProject.settings import SITE_BASE_URL
from django.urls import reverse_lazy


def create_url_view(request, **kwargs):
    if request.method == 'POST':
        form = EnterUrlForm(request.POST)
        if form.is_valid():
            su = ShortenedUrl()
            # su = ShortenedUrl(pk=None, user=request.user, original_url=form.cleaned_data['user_original_url'])
            if isinstance(request.user, User):
                su.save(request.user, form.cleaned_data['user_original_url'])
            else:
                su.save(User.objects.get(pk=1), form.cleaned_data['user_original_url'])
            prev_url = su.new_short_url
            return HttpResponseRedirect(f'/urls/create_url/?url={prev_url}')

    else:

        prev_url = request.GET.get('url', None)
        form = EnterUrlForm()

    return render(request, 'UrlShortenerApp/create_url.html',
                  {'form': form, 'current_user': request.user, 'user_logged_in': request.user.is_authenticated,
                   "prev_url": prev_url})


def shorted_url_handler(request):
    request_url = request.get_full_path()
    final_url = SITE_BASE_URL + request_url[1:]
    # return HttpResponse(final_url)
    original_URL_fromDB = ShortenedUrl.objects.get(new_short_url=final_url)
    return HttpResponseRedirect(original_URL_fromDB.original_url)


def change_url_status_view(request, url_for_delete):
    if ShortenedUrl.objects.get(pk=url_for_delete).is_active:
        ShortenedUrl.objects.filter(pk=url_for_delete).update(is_active=False)
        return redirect('profile_url')
    else:
        ShortenedUrl.objects.filter(pk=url_for_delete).update(is_active=True)
        return redirect('hidden_urls_url')
