from django.shortcuts import render


def home(request):
    return render(request, "pdfmanager/home.html")


def about(request):
    return render(request, "pdfmanager/about.html")


def pdf_merge(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        print('Yes')
    return render(request, "pdfmanager/pdfmerge.html")


def pdf_split(request):
    return render(request, "pdfmanager/pdfsplit.html")


def pdf_rotate(request):
    return render(request, "pdfmanager/pdfrotate.html")


def pdf_extract(request):
    return render(request, "pdfmanager/pdfextract.html")


def pdf_watermark(request):
    return render(request, "pdfmanager/pdfwatermark.html")


def pdf_info(request):
    return render(request, "pdfmanager/pdfinfo.html")