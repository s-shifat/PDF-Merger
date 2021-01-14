from PyPDF2 import PdfFileMerger
import os

pdfs = os.listdir('samples')

def i_Merge(pdfs):
    print(pdfs)
    merger = PdfFileMerger(False)

    for pdf in pdfs:
        current_file = ".\\samples\\" + pdf
        merger.append(current_file)

    merger.write("result.pdf")
    merger.close()
