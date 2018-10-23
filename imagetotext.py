try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


# Simple image to string
print(pytesseract.image_to_string(Image.open('maxresdefault.jpg')))

pdf = pytesseract.image_to_pdf_or_hocr('maxresdefault.jpg', extension='pdf')