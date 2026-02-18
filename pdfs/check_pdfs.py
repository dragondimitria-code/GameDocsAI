import fitz
import os

folder_path = "."

for filename in os.listdir(folder_path):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(folder_path, filename)
        doc = fitz.open(pdf_path)

        text_pages = sum(1 for page in doc if page.get_text().strip())
        total_pages = len(doc)

        if text_pages == 0:
            result = "Scanned / Image-based"
        elif text_pages == total_pages:
            result = "Fully text-based"
        else:
            result = "Mixed"

        print(f"{filename}: {result} ({text_pages}/{total_pages} pages with text)")
