import PyPDF2 as p
import os


def pdf_add_password(pdf, passwd, output_pdf):
    pdf_reader = p.PdfFileReader(pdf)
    pdf_writer = p.PdfFileWriter()

    try:
        pdf_nums = pdf_reader.numPages
    except p.errors.PdfReadError:
        print(f'PDF file {pdf} is already encrypted. Please upload the file which is not password protected.')
        exit()

    for i in range(pdf_nums):
        page = pdf_reader.getPage(i)
        pdf_writer.addPage(page)

    if passwd is not None:
        if pdf_reader.isEncrypted:
            print(f'PDF file {pdf} is already encrypted. Please upload the file which is not password protected.')
        else:
            pdf_writer.encrypt(passwd)
            output_file = output_pdf

    with open(output_file, 'wb') as f:
        pdf_writer.write(f)

    return True

def pdf_remove_password(pdf, passwd, output_pdf):
    pdf_reader = p.PdfFileReader(pdf)
    pdf_writer = p.PdfFileWriter()

    if pdf_reader.isEncrypted:
        pdf_reader.decrypt(passwd)
        output_file = output_pdf
    else:
        print(f'PDF file {pdf} is not encrypted. please pass correct file which is password protected.')

    try:
        pdf_nums = pdf_reader.numPages
    except p.errors.PdfReadError:
        print(f'PDF file {pdf} is already encrypted. Please upload the file which is not password protected.')
        return False

    for i in range(pdf_nums):
        page = pdf_reader.getPage(i)
        pdf_writer.addPage(page)

    with open(output_file, 'wb') as f:
        pdf_writer.write(f)

    return True


if __name__ == "__main__":
    pdf = '/Users/rohitmac/Downloads/JEE_Score_encrypted.pdf'
    op =  '/Users/rohitmac/Downloads/JEE_Score_decrypted.pdf'
    pdf_remove_password(pdf, '1234', op)


    # pp.pdf_remove_password('/Users/rohitmac/Downloads/5773202305067003606277.pdf','LGKV06277', '/Users/rohitmac/Downloads/5773202305067003606277_ul.pdf')
    # pp.pdf_remove_password('/Users/rohitmac/Downloads/5773202210074801576277.pdf','LGKV06277', '/Users/rohitmac/Downloads/5773202210074801576277_ul.pdf')
    # pp.pdf_remove_password('/Users/rohitmac/Downloads/5773202209046602756277.pdf','LGKV06277', '/Users/rohitmac/Downloads/5773202209046602756277_ul.pdf')
    # pp.pdf_remove_password('/Users/rohitmac/Downloads/5773202206032401976277.pdf','LGKV06277', '/Users/rohitmac/Downloads/5773202206032401976277_ul.pdf')
    # pp.pdf_remove_password('/Users/rohitmac/Downloads/5773202205092100896277.pdf','LGKV06277', '/Users/rohitmac/Downloads/5773202205092100896277_ul.pdf')
    # pp.pdf_remove_password('/Users/rohitmac/Downloads/5773202203038602166277.pdf','LGKV06277', '/Users/rohitmac/Downloads/5773202203038602166277_ul.pdf')
    # pp.pdf_remove_password('/Users/rohitmac/Downloads/5773202202093103176277.pdf','LGKV06277', '/Users/rohitmac/Downloads/5773202202093103176277_ul.pdf')
    #
    # pp.pdf_remove_password('/Users/rohitmac/Downloads/AFNXXXXX6K_Q2_2023-24.pdf','AFNPK0756K', '/Users/rohitmac/Downloads/AFNXXXXX6K_Q2_2023-24_ul.pdf')
    #
    # 83139270968





