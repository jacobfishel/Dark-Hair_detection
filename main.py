import cv2
import numpy as np

#create the VideoCapture object
cap = cv2.VideoCapture(0)

while cap.isOpened():

    #read the frames
    ret, frame = cap.read()
    if not ret:
        break

    #apply a gaussian blue to reduce noise
    blur = cv2.GaussianBlur(frame, (7, 7), 0)
    
    #convert to grayscale
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)


    #threshold (Use regular to have full control over threshold value)
    # _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU)
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)


    #Open (erode, then dilate)
    kernel = np.ones((5, 5), np.uint8)
    open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Open", open)

    #adaptive threshold
    # adaptiveThresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 2)
    # cv2.imshow("Thresh", thresh)

    #get the coutours
    contours, _ = cv2.findContours(open, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    headcount = 0
    #loop through the contours and check the area
    for contour in contours:

        #calculate the contour area to get the rough area that hair would take up in frame
        area = cv2.contourArea(contour)

        #calculate perimeter and circular to check for circularity similar to hair shape
        perimeter = cv2.arcLength(contour, True)

        if perimeter == 0:
            continue

        circularity = (4 * np.pi * area) / (perimeter * perimeter)

        #AREA
        if 3500 < area < 19000:

            #CIRCULARITY
            if circularity > 0.1: 

                x, y, w, h = cv2.boundingRect(contour)
                aspectRatio = w / float(h)
            
                #ASPECT RATIO
                if 0.7 < aspectRatio < 1.3:

                    hull = cv2.convexHull(contour)
                    hullArea = cv2.contourArea(hull)

                    convexity = area / hullArea if hullArea > 0 else 0   

                    #CONVEXITY
                    if 0.3 < convexity < 0.9:

                        #if all conditions pass, increase head count, draw contours, bounding box and put text
                        headcount += 1
                        cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

                        cv2.putText(frame, f"Contour area: {area}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 0)
                        cv2.putText(frame, f"Circularity: {circularity}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 0)
                        cv2.putText(frame, f"Aspect ratio: {aspectRatio}", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 0)
                        cv2.putText(frame, f"Convexity : {convexity}", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 0)

                        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw bounding box



    cv2.putText(frame, f"Head Count: {headcount}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 0)

    #display webcam feed
    cv2.imshow("Head Detection", frame)

    #press q to terminate
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break