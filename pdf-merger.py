import PyPDF2 as pydf
import os

merger = pydf.PdfMerger()

filesList = os.listdir("merge")
for file in filesList:
    if ".pdf" in file:
        merger.append(f"merge/{file}")

merger.write("teorico.pdf")