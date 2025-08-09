import cv2
import numpy as np

def remove_background(image_path, output_path):
    image = cv2.imread(image_path)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    blurred = cv2.GaussianBlur(gray, (21, 21), 0)
    
    _, thresh = cv2.threshold(blurred, 125, 255, cv2.THRESH_BINARY_INV)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN)
    
    mask = np.zeros_like(image)
    
    for contour in contours:
        cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)
        
    result = cv2.bitwise_and(image, mask)
    
    cv2.imwrite(output_path, result)
    
    cv2.imshow("Original Image", image)
    cv2.imshow("Result Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# Usuage
remove_background("images.jpeg", "output_image.jpeg") 
    
        