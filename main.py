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

window = tk.Tk()
menu = tk.Menu(window)
fileMenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=fileOpen)
window.config(menu=menu)
window.mainloop()

