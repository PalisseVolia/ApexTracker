import os
import pytesseract
from PIL import Image
import pandas as pd
import json

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the directory containing the images
image_dir = "images"

# Initialize an empty list to store the OCR results
ocr_results = []

# Loop through each image file in the directory
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Load the image using PIL
        image_path = os.path.join(image_dir, filename)
        image = Image.open(image_path)

        # Perform OCR using pytesseract
        text = pytesseract.image_to_string(image)

        # Append the OCR result to the list
        ocr_results.append({"Image": filename, "Text": text})

# Create a pandas DataFrame from the OCR results
df = pd.DataFrame(ocr_results)

# Print the DataFrame
print(df)

# Convert the DataFrame to JSON
json_data = df.to_json(orient="records")

# Write the JSON data to a file
json_file = "ocr_results.json"
with open(json_file, "w") as f:
    f.write(json_data)

print("JSON file created: ", json_file)