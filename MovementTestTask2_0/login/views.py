from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import UserForm


def index(request):
    context = {}
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        print(form.data)
        return redirect('success', form.data['name'], form.data['surname'])
    context['form'] = form
    return render(request, "login/index.html", context)


def success_create(request, name, surname):
    return render(request, "login/success.html", {'name': name, 'surname': surname})
