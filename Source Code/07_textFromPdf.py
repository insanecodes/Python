import PyPDF2

a = PyPDF2.PdfFileReader('Learning_python.pdf')

str = ""

for i in range(0,a.getNumPages()):
    str += a.getPage(i).extractText()

with open('text.txt'."w",encoding='utf-8') as f:
    f.write(str)
