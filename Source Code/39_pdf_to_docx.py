from pdf2docx import Converter

# enter your pdf name
pdf_file = 'ang.pdf'
# docs file to be created
docx_file = 'main.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()
