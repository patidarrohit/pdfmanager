from django.shortcuts import render


def home(request):
    return render(request, "pdfmanager/home.html")


def about(request):
    return render(request, "pdfmanager/about.html")

