import fitz


def load_pdf(pdf_path):

    doc = fitz.open(pdf_path)

    pages = []

    for page_num in range(len(doc)):

        page = doc[page_num]

        pages.append(
            {
                "page_number": page_num + 1,
                "text": page.get_text()
            }
        )

    return pages