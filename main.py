# This is a sample Python script.
from pdfToPNG import pdf_to_png
from patternRec import search_patterns
from edgeDetection import detect_edges

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #pdf_to_png("D5437611-X02 (WING GEAR).pdf", "output_images")
    #search_patterns("./output_images/page_1.png", "./symbols/Picture10_new.png")
    detect_edges("./output_images/page_1.png")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
