import os
import pytesseract
from PIL import Image
import pandas as pd
import json
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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
    'fi ': '',
    'eml': '5'
}

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
        ocr_results.append({"Image": filename, "Text": text})

# Create a pandas DataFrame from the OCR results
df = pd.DataFrame(ocr_results)

k = 1
# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Access the values of each column in the row
    image_filename = row["Image"]
    text = row["Text"]
    
    # Perform operations on the values
    image_number = int(image_filename.split(".")[0])
    # Replace the value in the DataFrame
    df.at[index, "Image"] = image_number

    if k == 12:
        k = 1
    print(k)
    match k:
        case 1:
            strings_to_check = ["Ash", "Alter", "Ballistic", "Bangalore", "Bloodhound", "Catalyst", "Caustic", "Conduit", "Crypto", "Fuse", "Gibraltar", "Horizon", "Lifeline", "Loba", "Mad Maggie", "Mirage", "Newcastle", "Octane", "Pathfinder", "Rampart", "Revenant", "Seer", "Valkyrie", "Vantage", "Wattson", "Wraith"]

            found_strings = []
            for string in strings_to_check:
                if string in text:
                    found_strings.append(string)

            if found_strings:
                text = ", ".join(found_strings)
            else:
                text = "No matching strings found"

            df.at[index, "Text"] = text
        case 2:
            strings_to_check = ["marksman weapons", "assault rifles", "pistols", "shotguns", "light machine guns", "sniper rifles", "sub machine guns"]

            found_strings = []
            for string in strings_to_check:
                if string in text:
                    found_strings.append(string)

            if found_strings:
                text = ", ".join(found_strings)
            else:
                text = "No matching strings found"

            df.at[index, "Text"] = text
        case 3:
            strings_to_check = ["Ash", "Alter", "Ballistic", "Bangalore", "Bloodhound", "Catalyst", "Caustic", "Conduit", "Crypto", "Fuse", "Gibraltar", "Horizon", "Lifeline", "Loba", "Mad Maggie", "Mirage", "Newcastle", "Octane", "Pathfinder", "Rampart", "Revenant", "Seer", "Valkyrie", "Vantage", "Wattson", "Wraith"]

            found_strings = []
            for string in strings_to_check:
                if string in text:
                    found_strings.append(string)

            if found_strings:
                text = ", ".join(found_strings)
            else:
                text = "No matching strings found"

            df.at[index, "Text"] = text
        case 4:
            strings_to_check = ["marksman weapons", "assault rifles", "pistols", "shotguns", "light machine guns", "sniper rifles", "sub machine guns"]

            found_strings = []
            for string in strings_to_check:
                if string in text:
                    found_strings.append(string)

            if found_strings:
                text = ", ".join(found_strings)
            else:
                text = "No matching strings found"

            df.at[index, "Text"] = text
        # case 5:
        #     
        # case 6:
        #     
        # case 7:
        #     
        # case 8:
        #     
        # case 9:
        #     
        # case 10:
        #     
        # case 11:
        #     
        
    k+=1
    
    # Print the values
    # print(f"Image: {image_number}")
    # print(f"Text: {text}")
    # print("--------------------")
# Sort the DataFrame by the "Image" column in ascending order
df = df.sort_values(by="Image")



# # Check for specific strings in df
# specific_strings = {
#     1: ["Pathfinder", "string2", "string3"],
#     2: ["string4", "string5", "string6"],
#     3: ["string7", "string8", "string9"],
#     4: ["string10", "string11", "string12"],
#     5: ["string1", "string2", "string3"],
#     6: ["string4", "string5", "string6"],
#     7: ["string7", "string8", "string9"],
#     8: ["string10", "string11", "string12"],
#     9: ["string1", "string2", "string3"],
#     10: ["string4", "string5", "string6"],
#     11: ["string7", "string8", "string9"]
# }

# # Iterate over the specific_strings dictionary
# for key, strings in specific_strings.items():
#     # Get the column name based on the key
#     column_name = f"Text_{key}"
    
#     # Check if the column exists in the DataFrame
#     if column_name in df.columns:
#         # Check for the occurrence of the strings in the corresponding column
#         df[column_name] = df["Text"].apply(lambda x: any(string in x for string in strings))

# Print the DataFrame
print(df)

# Convert the DataFrame to JSON
json_data = df.to_json(orient="records")

# Write the JSON data to a file
json_file = "ocr_results.json"
with open(json_file, "w") as f:
    f.write(json_data)

print("JSON file created: ", json_file)