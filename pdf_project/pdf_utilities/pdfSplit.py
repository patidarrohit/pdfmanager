import PyPDF2 as p


def pdf_split(pdf, splits):
    pdf_reader = p.PdfFileReader(pdf)
    if len(splits) >= pdf_reader.getNumPages() or splits[-1] >= pdf_reader.getNumPages():
        raise Exception('Number of splits are more than pages in pdf.')

    start = 0
    end = splits[0]

    for i in range(len(splits) + 1):
        pdf_writer = p.PdfFileWriter()
        output_pdf = pdf.split('.pdf')[0] + str(i) + '.pdf'

        for page in range(start, end):
            pdf_writer.addPage(pdf_reader.getPage(page))

        with open(output_pdf, 'wb') as f:
            pdf_writer.write(f)

        start = end
        try:
            end = splits[i+1]
        except IndexError:
            end = pdf_reader.numPages


def main():
    pdf = '/Users/rohitmac/Downloads/Rental_Application-2.pdf'
    # Splits is list of pages from where you want to split the pdf
    splits = [3]
    pdf_split(pdf, splits)


if __name__ == "__main__":
    main()
