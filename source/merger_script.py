from PyPDF2 import PdfFileMerger
import os

def merger(pdfs):
    print(pdfs)
    merger = PdfFileMerger(False)

    for pdf in pdfs:
        current_file = ".\\samples\\" + pdf
        merger.append(current_file)

    merger.write("result.pdf")
    merger.close()
    
if __name__ == '__main__':
    pdfs = os.listdir('../samples')
    merger(pdfs)
    
