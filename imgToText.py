from pytesseract import pytesseract
from PIL import Image
import os

class OCR:
    def __init__(self):
        self.path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    def extract(self, filename):
        try:
            pytesseract.tesseract_cmd = self.path
            text = pytesseract.image_to_string(filename)

            return text
        except Exception as e:
            print(e)
            return "Error"
        

image_path = os.path.abspath(os.path.join( 'train_data', '41uwo4PVnuL.jpg'))
ocr = OCR()
image = Image.open(image_path)
txt = ocr.extract(image)
print(txt)