# Image to PDF Converter

This Python script converts multiple image files (PNG, JPEG, JPG) into a single PDF document. It utilizes the Pillow and img2pdf libraries to handle image processing and PDF generation.

## Features

- Supports conversion of PNG, JPEG, and JPG image formats to PDF.
- Provides a simple command-line interface for converting images to PDF.
- Merges multiple PDFs into a single PDF file.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ethanux/image-to-pdf-converter.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script from the command line:

    ```bash
    python image_to_pdf.py image1.jpg image2.png
    ```

    Replace `image1.jpg`, `image2.png`, etc., with the paths to your image files.

2. Alternatively, you can run the script without arguments to convert all images in the current directory:

    ```bash
    python image_to_pdf.py
    ```

3. The generated PDF file will be saved as `new.pdf` in the `pdf` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

[Ethanux](https://github.com/ethanux)

## Acknowledgements

- [Pillow](https://python-pillow.org/) - Python Imaging Library (PIL) fork used for image processing.
- [img2pdf](https://github.com/josch/img2pdf) - Library used for converting images to PDF files.
