import PyPDF2 as p


def pdfrotate(origFileName, newFileName, rotation):
    pdfFileObj = open(origFileName, 'rb')
    pdfReader = p.PdfFileReader(pdfFileObj)
    pdfWriter = p.PdfFileWriter()

    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        pageObj.rotateClockwise(rotation)

        pdfWriter.addPage(pageObj)
    
    newFile = open(newFileName, 'wb')

    pdfWriter.write(newFile)
    pdfFileObj.close()
    newFile.close()


def main():
    origFileName = '/Users/rohitmac/Downloads/Hardik_10th.pdf'
    newFileName = '/Users/rohitmac/Downloads/Hardik_10th_90.pdf'
    rotation = 90
    pdfrotate(origFileName, newFileName, rotation)


if __name__ == "__main__":
    main()
    
