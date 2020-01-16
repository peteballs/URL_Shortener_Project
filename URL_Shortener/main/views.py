from django.shortcuts import render, redirect
from .models import short_urls
from .forms import UrlForm
from .shortener import shortner
import random
import string

def make(request):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for i in range(5))

    if request.method == 'POST':
        url = request.POST['url']
        
        if not short_urls.objects.filter(url = url).exists():
            new_url = short_urls.objects.create(
                url = url,
                short_url = random_string
            )
            context = {
                "newest_url": new_url,
                "short_urls": short_urls.objects.all()

            }
            return render(request, 'home.html', context)
        else:
            context = {
                "newest_url": short_urls.objects.filter(url = url),
                "short_urls": short_urls.objects.all()
            }
            print(context)
            return render(request, 'home.html', context)
    else:
        context = {
            "short_urls": short_urls.objects.all()
        }
        return render(request, 'home.html', context)

    
    return render(request, 'home.html')


def redirector(request, url):
    redirect_url = short_urls.objects.get(short_url = url)
    return redirect(redirect_url.url)

