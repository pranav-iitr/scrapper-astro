# AIzaSyDGtN4QtZ6s65awzu7jzgywvPpAbkELjsQ gemini
# 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 gpt

# C:\Users\prana\AppData\Local\Programs\Python\Python312\python.exe

import os
from PIL import Image
import pytesseract
from corrected_text import clean_and_correct_text
# Path to tesseract executable
# Update this path if you have tesseract installed in a custom directory
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows example

def apply_ocr_to_image(image_path):
    """Applies OCR to a given image and returns the extracted text."""
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return ""

def ocr_on_images_in_folder(folder_path, output_file):
    """Recursively apply OCR to all images in a folder and save results in a text file."""
    with open(output_file, 'a+') as f_out:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                try:
                    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
                        file_path = os.path.join(root, file)
                        print(f"Processing {file_path}")
                        ocr_text = apply_ocr_to_image(file_path)
                        f_out.write(f"--- OCR Results for {file_path} ---\n")
                        f_out.write( clean_and_correct_text(ocr_text) + "\n\n")
                except:
                    pass
    print(f"OCR data saved in {output_file}")

# Set the folder containing the images and the output text file path
image_folder_path = "./extract"
output_text_file = "ocr_results.txt"

# Perform OCR on images in the folder
ocr_on_images_in_folder(image_folder_path, output_text_file)
