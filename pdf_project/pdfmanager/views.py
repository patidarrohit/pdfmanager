from django.shortcuts import render, redirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from pdf_utilities.pdfMerge import pdf_merge as pm
from datetime import datetime
import mimetypes


def home(request):
    return render(request, "pdfmanager/home.html")


def about(request):
    return render(request, "pdfmanager/about.html")


# def pdf_merge(request):
#     op_file_name = 'pdf_merge_' + str(int(round(datetime.now().timestamp())))
#     if request.method == 'POST':
#         my_files = request.FILES
#         # with open('/Users/rohitmac/test.pdf', 'wb+') as destination:
#         #     for chunk in my_file.chunks():
#         #         destination.write(chunk)
#         file_list = []
#         for k, v in my_files.items():
#             file_list.append(v)
#         file_dir, file_name = pm(file_list, op_file_name)
#         with open(file_dir+'/'+file_name, 'rb') as f:
#             mime_type, _ = mimetypes.guess_type(file_dir+'/'+file_name)
#             print(mime_type)
#             response = HttpResponse(f, content_type=mime_type)
#             response['Content-Disposition'] = "attachment; filename=%s" % file_name
#             print(response)
#         return redirect("/pdfmergedownload/")
#     return render(request, "pdfmanager/pdfmerge.html")

def pdf_merge(request):
    op_file_name = 'pdf_merge_' + str(int(round(datetime.now().timestamp())))
    if request.method == 'POST':
        my_files = request.FILES
        file_list = []
        for k, v in my_files.items():
            file_list.append(v)
        pm(file_list, op_file_name)
        file_dir, file_name = pm(file_list, op_file_name)
        with open(file_dir + '/' + file_name, 'rb') as f:
            print(file_dir + '/' + file_name)
            fs = FileSystemStorage()
            file = fs.save(file_name, f)
            fileurl = fs.url(file)
            fileSize = fs.size(file)
            print(fileSize, fileurl)
        return render(request, "pdfmanager/pdfmerge_download.html", {'fileurl': fileurl})
    return render(request, "pdfmanager/pdfmerge.html")


def pdf_merge_download(request):
    return render(request, "pdfmanager/pdfmerge_download.html")


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