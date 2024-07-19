import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_info(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Preprocess the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Perform OCR
    text = pytesseract.image_to_string(thresh, lang='fra')
    
    # Parse the extracted text
    challenges = []
    for line in text.split('\n'):
        if 'Disputer' in line or 'Infliger' in line or 'Mettre KO' in line or 'Réaliser' in line:
            challenges.append(line.strip())
    
    return challenges

# Usage
image_path = 'images\Sans titre.png'
challenges = extract_info(image_path)

for challenge in challenges:
    print(challenge)