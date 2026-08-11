import fitz  # PyMuPDF
import pytesseract
from PIL import Image


def extract_text_from_pdf(file_path):
    """
    Extract text from normal PDFs.
    If the PDF is scanned, use OCR as a fallback.
    """

    text = ""

    try:
        # Open PDF
        pdf_document = fitz.open(file_path)

        # First: normal text extraction
        for page in pdf_document:
            page_text = page.get_text("text")

            if page_text:
                text += page_text + "\n"

        # If normal text was found, return it
        if text.strip():
            return text

        # OCR fallback for scanned PDFs
        print("Normal text extraction failed. Trying OCR...")

        for page in pdf_document:
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

            image = Image.frombytes(
                "RGB",
                [pix.width, pix.height],
                pix.samples
            )

            page_text = pytesseract.image_to_string(image)
            text += page_text + "\n"

        return text.strip()

    except Exception as e:
        print("PDF extraction error:", str(e))
        return ""


# Test this file directly
if __name__ == "__main__":

    file_path = "uploads/M.Furqan (Resume).pdf"

    text = extract_text_from_pdf(file_path)

    print("\nTEXT LENGTH:", len(text))
    print("\nEXTRACTED TEXT:\n")
    print(text[:3000])