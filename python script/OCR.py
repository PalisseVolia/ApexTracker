import os
import pytesseract
from PIL import Image
import pandas as pd
import json
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ===============================================================================
# Genreal variables
# ===============================================================================

# Path to the directory containing the images
image_dir = "images"

# Initialize an empty list to store the OCR results
ocr_results = []

# Manual corrections dictionary
corrections = {
    'oon2': '',
    'S2ns': '',
    ' Jmx ': '',
    ' Jr ': '',
    'Ty ': '',
    'i ': '',
    'Wini': 'Win a',
    ' Cc ': 'Control legend only',
    ' A ': '',
    'Opena': 'Open a',
    'orConduit': 'or Conduit',
    'combin ation': 'combination',
    ' time ': '',
    '2030': '',
    'BRI': '',
    'BR.': '',
    'BR ': '',
    'Rl ': '',
    'Phe ': 'Phenix Kit',
    ' jx': '',
    'SOO': '500',
    'SO': '50',
    'OOO': '000',
    'OO': '00',
    'O00': '000',
    ' UN': '',
    'ina': 'in a',
    'fl ': '',
    'fOutlive': 'Outlive',
    'fi ': '',
    'Winmatch': 'Win 1 match',
    'combin ation': 'combination',
    'knock': 'knockdowns',
    'top3 1with': 'top-3 1 time with',
    'eml': '5'
}

legends = [
    "Ash",
    "Alter",
    "Ballistic",
    "Bangalore",
    "Bloodhound",
    "Catalyst",
    "Caustic",
    "Conduit",
    "Crypto",
    "Fuse",
    "Gibraltar",
    "Horizon",
    "Lifeline",
    "Loba",
    "Mad Maggie",
    "Mirage",
    "Newcastle",
    "Octane",
    "Pathfinder",
    "Rampart",
    "Revenant",
    "Seer",
    "Valkyrie",
    "Vantage",
    "Wattson",
    "Wraith"
]

weapons = [
    "marksman weapons",
    "assault rifles",
    "pistols",
    "shotguns",
    "light machine guns",
    "sniper rifles",
    "sub machine guns"
]

chall_5 = [
    "5000 ",
    "500 ",
    "15 ",
    "50 ",
    "1 "
]

chall_67 = [
    "1000 ",
    "4000 ",
    "500 ",
    "knockdowns",
    "25 ",
    "finish 10",
    "10 finishing",
    "Assault",
    "Controller",
    "Recon",
    "Skirmisher",
    "Support",
    "50 ",
    "30 "
]

chall_l4 = [
    "Replicator",
    "Card",
    "Deal 1000",
    "Deal 1500",
    "Deal 750",
    "Scanning",
    "Equip",
    "Evolve",
    "2 ",
    "another",
    "legendary",
    "neutral",
    "Loot 50",
    "Obtain",
    "10 Extended",
    "10 Weapon",
    "Open 50",
    "300 ",
    "Play 10",
    "Reach",
    "Restore 1000",
    "Restore 1500",
    "Regenerate 1500",
    "Breach",
    "Reveal",
    "Revive",
    "Survive",
    "Thank",
    "Use a Ring",
    "Use a Survey"
]

# ===============================================================================
# OCR to get challenges descrtpion from images, stored in a dataframe
# ===============================================================================

# Loop through each image file in the directory
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Load the image using PIL
        image_path = os.path.join(image_dir, filename)
        image = Image.open(image_path)

        # Perform OCR using pytesseract
        text = pytesseract.image_to_string(image)

        # Apply manual corrections to the OCR text
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text)
        for wrong, correct in corrections.items():
            text = text.replace(wrong, correct)
        
        # Remove spaces at the beginning and end of each line
        text = '\n'.join([line.strip() for line in text.split('\n')])

        # Append the OCR result to the list
        ocr_results.append({"ID": filename, "Text": text})

# Create a pandas DataFrame from the OCR results
df = pd.DataFrame(ocr_results)

for index, row in df.iterrows():
    # Access the values of each column in the row
    image_filename = row["ID"]
    
    # Perform operations on the values
    image_number = int(image_filename.split(".")[0])
    # Replace the value in the DataFrame
    df.at[index, "ID"] = image_number

# Sort the DataFrame by the "Image" column in ascending order
df = df.sort_values(by="ID")

# ===============================================================================
# Data cleaning and processing for UI integration
# ===============================================================================

def find_strings(text, strings_to_check):
    found_strings = []
    for string in strings_to_check:
        if string in text:
            found_strings.append(string.strip())
    if found_strings:
        text = found_strings
    else:
        text = "No matching legend found ("+text+")"
    return text

k = 1
# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Access the values of each column in the row
    text = row["Text"]

    if k == 12:
        k = 1
    print(k)
    match k:
        case 1:
            df.at[index, "Text"] = find_strings(text, legends)
        case 2:
            df.at[index, "Text"] = find_strings(text, weapons)
        case 3:
            df.at[index, "Text"] = find_strings(text, legends)
        case 4:
            df.at[index, "Text"] = find_strings(text, weapons)
        case 5:
            df.at[index, "Text"] = find_strings(text, chall_5)
        case 6:
            df.at[index, "Text"] = find_strings(text, chall_67)
        case 7:
            df.at[index, "Text"] = find_strings(text, chall_67)
        case 8:
            df.at[index, "Text"] = find_strings(text, chall_l4)
        case 9:
            df.at[index, "Text"] = find_strings(text, chall_l4)
        case 10:
            df.at[index, "Text"] = find_strings(text, chall_l4)
        case 11:
            df.at[index, "Text"] = find_strings(text, chall_l4)
    k+=1
    
# Convert the DataFrame to JSON
json_data = df.to_json(orient="records")

# ===============================================================================
# Export to Json file
# ===============================================================================

# Write the JSON data to a file
json_file = "json/ocr_results.json"
with open(json_file, "w") as f:
    f.write(json_data)

print("JSON file created: ", json_file)