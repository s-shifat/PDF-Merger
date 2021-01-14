from PyPDF2 import PdfFileMerger
import os

pdfs = os.listdir('./pdfs')

def i_Merge(pdfs):
    print(pdfs)
    merger = PdfFileMerger(False)

    for pdf in pdfs:
        current_file = ".\\pdfs\\" + pdf
        merger.append(current_file)

    merger.write("result.pdf")
    merger.close()
