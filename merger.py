from PyPDF2 import PdfFileMerger

pdfs = [str(i) + ".pdf" for i in range(1,13)]
addings = ["example19.2_Garg.pdf","Maliha-Mam-4-Assignments.pdf"]
if len(addings)>0:
    [pdfs.append(file) for file in addings]
print(pdfs)
merger = PdfFileMerger(False)

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
