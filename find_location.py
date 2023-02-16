import cv2
import imutils
import numpy as np
import os

def find_car_location(image_path, filename, car_id, session):

    image_number = filename.split('.')[0][-3:]
    identifier = f'{session}-{car_id}-{image_number}'
    image = cv2.imread(image_path)
    # blur
    blur = cv2.GaussianBlur(image,(5,5),cv2.BORDER_DEFAULT)
    # convert to grayscale
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    # convert to binary image
    thresh = cv2.threshold(gray, 215, 255,cv2.THRESH_BINARY_INV)[1]
    # dilate
    dilate = cv2.dilate(thresh, None, iterations=2)
    # get contours
    contours = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    
    contours = imutils.grab_contours(contours)
    """ m = 0
    for cnt in contours:
        perimeter = cv2.arcLength(cnt, True)
        if perimeter > m:
            m = perimeter
            
    print(m) """
    contours_img = cv2.drawContours(image.copy(), contours, -1, (0, 0, 255), 3)
    
    # largest area of contours
    largest_area = max(contours, key=cv2.contourArea)

    # coordinates for extreme right of largest area
    location = tuple(largest_area[largest_area[:, :, 0].argmax()][0])

    cv2.circle(image, location, 8, (0, 0, 255), -1)
    cv2.line(image, (location[0], 0), (location[0], 1335), (0, 0, 255), 2)
    
    cv2.putText(image, identifier, (2600, 1250), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 5)
    filename = f'./edited/{session}/{car_id}/xx{filename}'
    
    if os.environ['DEBUG'] == '1':
        cv2.imshow(filename, image)
        cv2.waitKey(0)
        cv2.imshow(filename, blur)
        cv2.waitKey(0)
        cv2.imshow(filename, thresh)
        #cv2.imshow(filename, dilate)
        cv2.waitKey(0)
        cv2.imshow(filename, contours_img)
        cv2.waitKey(0)
        
        cv2.destroyAllWindows()
        

    cv2.imwrite(filename, image)
    return location

    





