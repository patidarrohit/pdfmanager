import PyPDF2 as p
import os
src_dir = '/Users/rohitmac/Downloads'


def pdf_merge(pdfs, output):
    pdf_merger = p.PdfFileMerger()
    pdfs = []
    for f in pdf_files:
        file = os.path.join('/Users/rohitmac/Downloads', f)
        pdf_merger.append(file)

    with open(output, 'wb') as f:
        pdf_merger.write(f)


if __name__ == "__main__":
    pdf_files = ['Hardik_10th.pdf', 'Hardik_12th.pdf']
    output = '/Users/rohitmac/Downloads/Hardik_10th_12th.pdf'
    pdf_merge(pdfs=pdf_files, output=output)
