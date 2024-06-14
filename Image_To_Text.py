import pytesseract
import PDF_To_Image
from tqdm import tqdm
from PIL import Image
from os import listdir

pytesseract.pytesseract.tesseract_cmd = PDF_To_Image.cwd + "\\Tesseract-OCR\\tesseract.exe" # Path to the tesseract executable

def image_to_text(path: str):
    text = ""
    text += pytesseract.image_to_string(Image.open(path))
    return text

def main():

    text = "" # Text to be written to the output file

    loading_bar = tqdm(listdir('output'))


    # loop through the files in the output directory and convert them to text
    for index, file in enumerate(loading_bar):
        
        text += f"File {index + 1}\n\n"
        text += image_to_text('output/' + file)

    # Write the text to the output file
    output = open('output.txt', 'w')
    output.write(text)
    output.close()


if __name__ == "__main__":
    PDF_To_Image.get_images()
    main()
    
