#!/usr/bin/env python3

"""Image to PDF Converter"""

# Importing required modules
from PIL import Image
from PyPDF2 import PdfMerger
import os
import img2pdf
import sys

def banner():
    """Display a banner."""
    blue = "\033[94m"
    ending = "\033[0m"
    banner_text = """
 _                            ____            _  __ 
(_)_ __ ___   __ _  __ _  ___|___ \ _ __   __| |/ _|
| | '_ ` _ \ / _` |/ _` |/ _ \ __) | '_ \ / _` | |_ 
| | | | | | | (_| | (_| |  __// __/| |_) | (_| |  _|
|_|_| |_| |_|\__,_|\__, |\___|_____| .__/ \__,_|_|  
                   |___/           |_|              
     """
    print(banner_text)

def get_args():
    """Get command line arguments."""
    args = sys.argv[1:]
    if len(sys.argv) > 1:
        for arg in args:
            try:
                filename, ext = arg.split('.')
                if ext.lower() not in ['jpg', 'jpeg', 'png']:
                    print("[-] Image file format not supported.")
                    print(f"[?] Supported formats: '.jpg', '.jpeg', '.png' (not '.{ext}')")
                    exit()
                else:
                    return sys.argv[1:]
            except ValueError:
                print(f"[-] Invalid syntax for argument '{arg}'. Must be a valid image file path.")
                print(f"[?] Example: '{arg}.jpg' or any standard image file format.")
                exit()
    else:
        print("[-] Missing arguments. Provide at least 1 argument.")
        exit()

def merge_pdf(pdfs):
    """
    Merge PDF files into a single PDF.

    Args:
        pdfs (list): List of PDF file paths to merge.

    Returns:
        str: File path of the merged PDF.
    """
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
        os.remove(pdf)
    file_path = os.path.join(os.getcwd(), 'pdf', 'new.pdf')
    merger.write(file_path)
    merger.close()
    return file_path

def image_pdf(list_img):
    """
    Convert images to PDF.

    Args:
        list_img (list): List of image file paths to convert.

    Returns:
        list: List of PDF file paths generated.
    """
    pdf_list = []
    for img_file in list_img:
        # Image file path
        img_path = img_file
        # PDF file path
        filename, _ext = os.path.splitext(img_path)
        pdf_path = os.path.join(os.getcwd(), 'pdf', filename + ".pdf")
        # Open image
        try:
            image = Image.open(img_path)
        except FileNotFoundError:
            print(f"[-] File '{img_path}' does not exist.")
            print("[-] Exiting...")
            exit()
        # Convert image to PDF chunks
        pdf_bytes = img2pdf.convert(image.filename)
        # Write PDF file
        with open(pdf_path, 'wb') as f:
            f.write(pdf_bytes)
        # Close image
        image.close()
        pdf_list.append(pdf_path)
        # Output success message
        print(f"[+] Successfully created PDF: {pdf_path}")
    return pdf_list

if __name__ == '__main__':
    # Display banner
    banner()
    # Merge PDFs
    merged_pdf_path = merge_pdf(image_pdf(get_args()))
    print(f"[+] PDF files merged successfully: {merged_pdf_path}")
