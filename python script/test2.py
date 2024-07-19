import pytesseract
from PIL import Image
import os
import re

# Configuration du chemin de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def clean_text(text):
    """
    Nettoie le texte extrait pour le rendre plus lisible.
    :param text: Texte brut extrait par l'OCR.
    :return: Texte nettoyé.
    """
    # Supprimer les caractères non alphanumériques, à l'exception des retours à la ligne et des espaces
    text = re.sub(r'[^\w\s]', '', text)
    # Remplacer les séquences de plusieurs espaces par un seul espace
    text = re.sub(r'\s+', ' ', text)
    # Corriger les fautes courantes d'OCR
    corrections = {
        'oon2': '',
        'S2ns': '',
        '2030':'',
        'contrdle': 'contrôle',
        'nimporte': 'n\'importe',
        'BRI': 'BR',
        'BR.': 'BR.',
        'SOO': '500',
        'SO': '50',
        'OOO': '000',
        'OO': '00',
        'O00': '000',
        'eml': '5'
    }
    for wrong, correct in corrections.items():
        text = text.replace(wrong, correct)
    # Remettre les retours à la ligne pour structurer le texte
    text = text.replace('Disputer', '\nDisputer').replace('Infliger', '\nInfliger').replace('Mettre KO', '\nMettre KO').replace('Réaliser', '\nRéaliser')
    return text.strip()

def ocr_image(image_path):
    """
    Effectue l'OCR sur une image donnée et retourne le texte extrait.
    :param image_path: Chemin de l'image.
    :return: Texte extrait.
    """
    try:
        # Ouvrir l'image
        img = Image.open(image_path)
        # Utiliser pytesseract pour extraire le texte
        text = pytesseract.image_to_string(img)
        # Nettoyer le texte extrait
        cleaned_text = clean_text(text)
        return cleaned_text
    except Exception as e:
        print(f"Erreur lors de l'OCR de l'image {image_path}: {e}")
        return ""

def process_images_in_folder(folder_path):
    """
    Traite toutes les images dans un dossier et extrait les textes.
    :param folder_path: Chemin du dossier contenant les images.
    :return: Dictionnaire avec les noms des fichiers et les textes extraits.
    """
    extracted_texts = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            text = ocr_image(image_path)
            extracted_texts[filename] = text
    return extracted_texts

# Chemin du dossier contenant les captures d'écran
folder_path = r'images'  # Mettre à jour avec le chemin réel

# Extraire les textes des images
extracted_texts = process_images_in_folder(folder_path)

# Afficher les résultats
for filename, text in extracted_texts.items():
    print(f"--- {filename} ---")
    print(text)
    print("\n")
