from django.shortcuts import render


def index(request):
    template = 'homepage/index.html'
    return render(request, template)


def contacts(request):
    template = 'homepage/contacts.html'
    return render(request, template)


def about(request):
    template = 'homepage/about.html'
    return render(request, template)
