# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pypdfium2 as pdfium

# Load a document
filepath = "新にほんご500問　N2.pdf"
pdf = pdfium.PdfDocument(filepath)

# render a single page (in this case: the first one)
page = pdf.get_page(0)
pil_image = page.render_topil(scale=2)
pil_image.save("output.jpg")
page.close()

# render multiple pages concurrently (in this case: all)
page_indices = [i for i in range(len(pdf))]
renderer = pdf.render_topil(
    page_indices = page_indices,
    scale=3
)
for image, index in zip(renderer, page_indices):
    image.save("output/%02d.jpg" % index)
    image.close()

pdf.close()