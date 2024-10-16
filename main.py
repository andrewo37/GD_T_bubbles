from mlStructure import build_model
from pdfToPNG import pdf_to_png
from patternRec import search_patterns
from edgeDetection import detect_edges, show_edge_contour
import tensorflow as tf
import tensorflow.keras as ks
import cv2


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('Hello Moto')
    #print(tf.__version__)
    #print(ks.__version__)
    #pdf_to_png("4012696-1_Rev_L.pdf", "output_images")
    #search_patterns("./output_images/page_1.png", "./symbols/Picture10_new.png")
    #detect_edges("./output_images/page_1.png")
    #show_edge_contour("./output_images/page_1.png")
    build_model("C:/Users/andre/PycharmProjects/GD_T_bubbles/training/images", "C:/Users/andre/PycharmProjects/GD_T_bubbles/training/Annotations")
