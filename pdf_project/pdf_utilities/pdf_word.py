from pdf2docx import parse


def convert_pdf_to_word(pdf, op_file):
    parse(pdf, op_file)


if __name__ == "__main__":
    pdf = '/Users/rohitmac/Downloads/Rental_Application.pdf'
    op_file = '/Users/rohitmac/Downloads/test.docx'
    convert_pdf_to_word(pdf, op_file)