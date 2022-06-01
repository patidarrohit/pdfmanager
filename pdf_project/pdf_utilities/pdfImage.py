from pdf2image import convert_from_path, convert_from_bytes
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from datetime import datetime
import os

base_dir = str(settings.BASE_DIR)
#ts = str(int(round(datetime.now().timestamp())))


def pdf_to_image_low(pdf, output, ts, util_nme):
    pages = convert_from_path(base_dir+pdf, 50)
    os.system(f"mkdir -p {base_dir}/media/temp/{util_nme}/{ts}/pdf")
    os.system(f"mkdir -p {base_dir}/media/temp/{util_nme}/{ts}/images")
    dr = f"{base_dir}/media/temp/{util_nme}/{ts}/images/"
    for c, page in enumerate(pages):
        page.save(dr + ts + '_' + str(c) + '.jpg', 'JPEG')
    return [ts, dr]


def pdf_to_image(pdf, output, quality):
    if quality == 'High':
        dpi = 500
    elif quality == 'Medium':
        dpi = 250
    else:
        dpi = 100

    pages = convert_from_path(pdf, dpi)
    for c, page in enumerate(pages):
        page.save(output + '_' + str(c) + '.jpg', 'JPEG')


if __name__ == '__main__':
    pdf = "/Users/rohitmac/Downloads/00 Sedgwick U.S. Leave of Absence Process Document - FINAL.pdf"
    output = "/Users/rohitmac/MyMAC/Projects/repo/pdfproject/pdf_project/output/pdfmerge/pdf_image"
    pdf_to_image_low(pdf, base_dir + '/media/temp/pdf_rotate/'+output)
