from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import EnterUrlForm
from .models import ShortenedUrl
from PetProject.settings import SITE_BASE_URL

def create_url_view(request):
    if request.method=='POST':
        form=EnterUrlForm(request.POST)
        if form.is_valid():
            su=ShortenedUrl()
            # su = ShortenedUrl(pk=None, user=request.user, original_url=form.cleaned_data['user_original_url'])
            su.save(request.user,form.cleaned_data['user_original_url'] )

            return HttpResponseRedirect('/user/profile')
    else:
        form=EnterUrlForm()

    return render(request, 'UrlShortenerApp/create_url.html', {'form':form})
# Create your views here.

def shorted_url_handler(request):
    request_url=request.get_full_path()
    final_url=SITE_BASE_URL+request_url[1:]
    # return HttpResponse(final_url)
    original_URL_fromDB=ShortenedUrl.objects.get(new_short_url=final_url)
    return HttpResponseRedirect(original_URL_fromDB.original_url)