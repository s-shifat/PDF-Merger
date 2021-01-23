from img2pdf import convert

file_name = "E:\\Python\\PDF Merger\\samples\\img.jpg"

with open(file_name,'rb') as f:
    pdf = convert(f)
    print(pdf)
    with open("result.pdf",'wb') as w:
        w.write(pdf)




