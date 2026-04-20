import pdfplumber

with pdfplumber.open("data/CV_tongkhanhhuy_VIE.pdf") as pdf:
    text = pdf.pages[0].extract_text()

print(text)