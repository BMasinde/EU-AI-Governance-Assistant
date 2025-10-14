import pdfplumber

# read EU AI Act pdf file
ai_text = "" 
with pdfplumber.open("data/raw/EU_AI_Act.pdf") as pdf:
    # iterate over pages
    for page in pdf.pages:
        ai_text += page.extract_text() + "\n"

# print(ai_text[0:4])