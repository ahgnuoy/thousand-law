import tkinter as tk
import tkinter.filedialog as fd
from PyPDF2 import PdfReader
from law import Law
import os

def fileOpen():
    fileName = fd.askopenfilename(initialdir=os.getcwd() + "/original", title="Open file", filetypes=[("PDF Files", "*.pdf")])
    reader = PdfReader(fileName)
    pages = []
    for i in range(len(reader.pages)):
        extracted = reader.pages[i].extract_text()
        pages.append(extracted)

    law = Law(pages)
    law.make_file()

def test():
    reader = PdfReader("C:/Ahgnuoy/Works/thousand-law/original/대한민국헌법(헌법)(제00010호)(19880225).pdf")
    pages = []
    for i in range(len(reader.pages)):
        extracted = reader.pages[i].extract_text()
        pages.append(extracted)
    law = Law(pages)
    law.make_file()


window = tk.Tk()
menu = tk.Menu(window)
fileMenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=fileOpen)
window.config(menu=menu)
button = tk.Button(window, text="run", command=test)
button.place(x=0, y=0)
window.mainloop()

