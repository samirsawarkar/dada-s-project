import pytesseract
from pdf2image import convert_from_path
import pandas as pd

def pdf_image_to_excel(pdf_path, excel_path):
    # Convert PDF to list of images
    images = convert_from_path(pdf_path)

    text_list = []
    for i, img in enumerate(images):
        # Extract text from each image using pytesseract
        text = pytesseract.image_to_string(img, lang='eng')
        text_list.append(text)

    # Create a DataFrame with the extracted text
    df = pd.DataFrame({'Text': text_list})

    # Save the DataFrame to an Excel file
    df.to_excel(excel_path, index=False)
    print(f'Successfully extracted text from PDF image and saved to Excel. Excel file saved at: {excel_path}')

# Example usage
pdf_file_path = "/Users/samir/python /dada's project/123.pdf"
excel_file_path = 'file.xlsx'
pdf_image_to_excel(pdf_file_path, excel_file_path)
