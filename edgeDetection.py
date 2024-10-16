import cv2
import numpy as np

def detect_edges(image_file):
    # Load the image
    img = cv2.imread(image_file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Edge detection
    edges = cv2.Canny(gray, 50, 150)

    # Morphological operations (optional)
    #kernel = np.ones((3, 3), np.uint8)
    #edges = cv2.dilate(edges, kernel, iterations=1)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, 250)

    cv2.imshow('Grayscale', gray)
    cv2.imshow('Edges', edges)

    x = 0
    if lines is not None:
        for i in range(len(lines)):
            print(f'row {i} Parallel lines')
            for j in range(i + 1, len(lines)):
                rho1, theta1 = lines[i][0]
                rho2, theta2 = lines[j][0]
                if (abs(theta1 - theta2) < 1e-1) and (abs(rho1 - rho2) < 20):  # Check for parallelism with tolerance
                    x += 1
                    # Convert polar coordinates to Cartesian coordinates
                    a1 = np.cos(theta1)
                    b1 = np.sin(theta1)
                    x01 = a1 * rho1
                    y01 = b1 * rho1
                    x11 = int(x01 + 1000 * (-b1))
                    y11 = int(y01 + 1000 * (a1))
                    x21 = int(x01 - 1000 * (-b1))
                    y21 = int(y01 - 1000 * (a1))


                    a2 = np.cos(theta2)
                    b2 = np.sin(theta2)
                    x02 = a2 * rho2
                    y02 = b2 * rho2
                    x12 = int(x02 + 1000 * (-b2))
                    y12 = int(y02 + 1000 * (a2))
                    x22 = int(x02 - 1000 * (-b2))
                    y22 = int(y02 - 1000 * (a2))


                    # Draw the lines on the image
                    cv2.line(img, (x11, y11), (x21, y21), (0,0,255), 2)
                    cv2.line(img, (x12, y12), (x22, y22), (0,0,255), 2)

    print(f'{x} Parallel lines found')

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # Analyze contours and edges together
    # for cnt in contours:
    #     # ... (contour analysis, e.g., check for circularity) ...
    #     perimeter = cv2.arcLength(cnt, True)
    #     area = cv2.contourArea(cnt)
    #     circularity = 4 * np.pi * area / (perimeter ** 2)
    #     if 0.004 < circularity < 1.2:  # Adjust threshold as needed
    #         cv2.drawContours(img, [cnt], -1, (0, 0, 0), 5)
    #
    #     # Analyze edges within the contour
    #     mask = np.zeros_like(gray)
    #     cv2.drawContours(mask, [cnt], -1, 0, -1)  # Create a mask for the contour
    #     contour_edges = cv2.bitwise_and(edges, edges, mask=mask)

    cv2.imshow('Detected Symbols', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

        # ... (analyze contour_edges for specific patterns, e.g., perpendicular lines) ...