# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pypdfium2 as pdfium
import os

def create_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

# Load a document
book_name = "新完全マスター文法日本語能力試験N2"
filepath = os.path.join("..","..","data","books", book_name + ".pdf")
pdf = pdfium.PdfDocument(filepath)

save_dir = os.path.join("..","..","data",book_name,"book_images" )

create_dir(save_dir)



# render multiple pages concurrently (in this case: all)
page_indices = [i for i in range(len(pdf))]
renderer = pdf.render_topil(
    page_indices = page_indices,
    scale=3
)
for image, index in zip(renderer, page_indices):
    
    save_path = os.path.join(save_dir,"%03d.jpg" % index)
    
    image.save(save_path)
    image.close()

pdf.close()