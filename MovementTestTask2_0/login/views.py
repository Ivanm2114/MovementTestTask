from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    context = {}
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "login/index.html", context)



def success_create(request, name):
    return render(request, "login/success.html")