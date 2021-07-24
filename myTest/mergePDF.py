"""
merge multi pdf files to one

If you have pip, PyPDF2 is on the Python Package Index, so you can install it with the following in your terminal/command prompt:

pip install PyPDF2


"""

import os 
from PyPDF2 import PdfFileMerger

target_path = './'
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

file_merger = PdfFileMerger()
for pdf in pdf_lst:
    file_merger.append(pdf)

file_merger.write("./merge.pdf")