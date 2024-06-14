# import module
import os
from pdf2image import convert_from_path


cwd = os.getcwd()



poppler_path = cwd + "\\poppler-24.02.0\\Library\\bin"

def get_images():
    # Store Pdf files in a list
    pdf_files = []


    # Find all pdf files in the current directory and add them to the list
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if file.endswith('.pdf'):
                pdf_files.append(file)

	#Adds folder if not there
    newpath = cwd + '\\output' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        
	#Goes through PDF files
    for file in pdf_files:
        images = convert_from_path(cwd + '/' + file, poppler_path= poppler_path)

        for i in range(len(images)):
            
            # Save pages as images in the pdf
            images[i].save('output\\page_'+ str(i) +'.jpg', 'JPEG')
