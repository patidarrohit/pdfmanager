from django.shortcuts import render, redirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from pathlib import Path
from django.core.files import File
from pdf_utilities.pdfMerge import pdf_merge as pm
from pdf_utilities.pdfImage import pdf_to_image_low
from pdf_utilities.pdfRotate import pdf_rotate_selected
from django.conf import settings
from datetime import datetime
import os
import mimetypes
from django.http import FileResponse, Http404


base_dir = str(settings.BASE_DIR)
temp_dir = '/Users/rohitmac/MyMAC/Projects/repo/pdfproject/pdf_project/output/temp'


def get_curr_dir():
    curr_dir_name = str(int(round(datetime.now().timestamp())))
    os.system(f"mkdir {temp_dir}/{curr_dir_name}")
    curr_dir = temp_dir + '/' + curr_dir_name
    return curr_dir

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
        file_dir, file_name = pm(file_list, op_file_name)
        path = Path(file_dir + '/' + file_name)
        fs = FileSystemStorage()
        path = '/' + os.path.relpath(path, './media')
        fileurl = fs.url(path)
        return render(request, "pdfmanager/pdfmerge_download.html", {'fileurl': fileurl})
    return render(request, "pdfmanager/pdfmerge.html")


def pdf_merge_download(request):
    return render(request, "pdfmanager/pdfmerge_download.html")


def pdf_split(request):
    return render(request, "pdfmanager/pdfsplit.html")


def pdf_rotate(request):
    return render(request, "pdfmanager/pdfrotate.html")


def pdf_rotate_show(request):
    ts = str(int(round(datetime.now().timestamp())))
    op_file_prefix = 'pdf_rotate_img_' + ts
    if request.method == 'POST':
        my_file = list(request.FILES.values())[0]
        fs = FileSystemStorage()
        file = fs.save(f'temp/pdf_rotate/{ts}/pdf/'+ op_file_prefix + '.pdf', my_file)         # Arguments-> filename, file object
        res = pdf_to_image_low(fs.url(file),  f'/media/temp/pdf_rotate/{ts}/pdf' + op_file_prefix + '/', ts)

        ts = res[0]
        img_dir = res[1]
        img_rel = os.path.relpath(img_dir, '.')
        img_rel = '/' + img_rel + '/'
        # Read images and pass it to template for selection.
        img_list = [img_rel + p for p in os.listdir(img_dir)]
        print(img_list)
        img_list.sort()
        return render(request, "pdfmanager/pdfrotateshow.html", {'images': img_list, 'ts': ts})


def pdf_rotate_download(request):
    if request.method == 'POST':
        inp = request.POST
        print(inp)
        angle = int(inp.getlist('rotate-angle')[0])
        pages = inp.getlist('check')
        ts = inp.getlist('timestamp')[0]
        all_img = [f'./media/temp/pdf_rotate/{ts}/images' + i for i in os.listdir(f'./media/temp/pdf_rotate/{ts}/images')]
        inp_file = f'./media/temp/pdf_rotate/{ts}/pdf/' + os.listdir(f'./media/temp/pdf_rotate/{ts}/pdf')[0]
        op_file = f'./media/temp/pdf_rotate/{ts}/pdf/output.pdf'
        with open(inp_file, 'rb') as f:
            pdf_rotate_selected(f, pages, op_file, angle)
        print(op_file)
        path = Path(os.path.abspath(op_file))
        fs = FileSystemStorage()
        path = '/' + os.path.relpath(path, './media')
        fileurl = fs.url(path)
        return render(request, "pdfmanager/pdfrotate_download.html", {'fileurl': fileurl})


def pdf_extract(request):
    return render(request, "pdfmanager/pdfextract.html")


def pdf_watermark(request):
    return render(request, "pdfmanager/pdfwatermark.html")


def pdf_info(request):
    return render(request, "pdfmanager/pdfinfo.html")


# def pdf_view(request):
#     try:
#         return FileResponse(open('/Users/rohitmac/MyMAC/Projects/repo/pdfproject/pdf_project/output/pdfmerge/pdf_merge_1653327541.pdf', 'rb'), content_type='application/pdf')
#     except FileNotFoundError:
#         raise Http404()