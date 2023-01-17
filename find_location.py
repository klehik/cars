import cv2
import imutils

def find_car_location(image_path, filename, car_id, session):

    print('processing: ', image_path)
    image = cv2.imread(image_path)

    # convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # convert to binary image
    thresh = cv2.threshold(gray, 220, 255,cv2.THRESH_BINARY_INV)[1]
    
    # thresh = cv2.erode(thresh, None, iterations=2)

    # dilate
    dilate = cv2.dilate(thresh, None, iterations=2)

    # get contours
    contours = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    #contours = cv2.drawContours(image.copy(), contours, -1, (0, 0, 255), 3)
    
    # largest area of contours
    largest_area = max(contours, key=cv2.contourArea)

    # coordinates for extreme right of largest area
    max_xy = tuple(largest_area[largest_area[:, :, 0].argmax()][0])

    cv2.circle(image, max_xy, 8, (0, 0, 255), -1)
    cv2.line(image, (max_xy[0], 0), (max_xy[0], 1335), (0, 0, 255), 2)

    filename = f'./edited/{session}/{car_id}/xx{filename}'
    cv2.imwrite(filename, image)

    return max_xy

    





