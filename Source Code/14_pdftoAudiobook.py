#A python program to convert PDF into Audiobook

import PyPDF2
import pyttsx3
from tkinter.filedialog import *


root = Tk()
root.title("Pdf to Audiobook")
# Open Dialogbox that requests selection of an existing file
book = askopenfilename()

#reading the pdf file and storing in str
a = PyPDF2.PdfFileReader(book)
str = ""
for i in range(0,a.getNumPages()):
    str += a.getPage(i).extractText()

# init function to get an engine instance for the speech synthesis  
engine = pyttsx3.init()
engine.say(str)
engine.runAndWait()
