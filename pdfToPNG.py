import fitz  # PyMuPDF
import cv2
import numpy as np

def pdf_to_png(pdf_path, output_folder):
    """
    Converts each page of a PDF file to a greyscale PNG image.

    Args:
        pdf_path (str): Path to the PDF file.
        output_folder (str): Path to the folder where PNG images will be saved.
    """
    pdf_document = fitz.open(pdf_path)
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]

        if isinstance(page, fitz.Page):
            pixmap = page.get_pixmap()

            # Convert pixmap to NumPy array (3D for color)
            img = np.frombuffer(pixmap.samples, dtype=np.uint8).reshape(pixmap.height, pixmap.width,3)

            # Convert to scale
            grey_img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY,0)

            # Create pixmap from greyscale image (use original pixmap dimensions)
            grey_pixmap = fitz.Pixmap(fitz.csGRAY, pixmap.width, pixmap.height, grey_img.tobytes(), 0)

            output_path = f"{output_folder}/{pdf_path}_{page_number + 1}.png"
            grey_pixmap.save(output_path)

# Example usage:
# pdf_to_png("D5437611-X02 (WING GEAR).pdf", "output_images")