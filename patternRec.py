import cv2
import numpy as np

def search_patterns(base_image, search_pattern):
    # Load the template image
    template = cv2.imread(search_pattern, 0)  # Load in grayscale

    # Load the input image
    img = cv2.imread(base_image,0)  # Load in grayscale

    # Perform template matching
    result = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED  )

    # Get the best match location
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Draw a rectangle around the detected symbol
    threshold = 0.78 # Set a threshold for matching confidence

    locations = np.where(result > threshold)

    w, h = template.shape[::-1]

    for pt in zip(*locations[::-1]):
        cv2.rectangle(img, (pt[0] - 40, pt[1] - h), (pt[0] - 40,pt[1] - int(h/2)), 0, 7)
    # if max_val > threshold:
    #     h, w = template.shape
    #     bottom_right = (max_loc[0], (max_loc[1] - int(h/2)))
    #     top_left = (max_loc[0] - 40, (max_loc[1] - (h)))
    #     #top_left = max_loc
    #     #bottom_right = (top_left[0] + w, top_left[1] + h)
    #     cv2.rectangle(img, top_left, bottom_right, 0, 7)

    # Display the result  

    cv2.imshow('Detected Symbol', img)
    cv2.imshow('searching for image', template)
    cv2.waitKey(0)
    cv2.destroyAllWindows()