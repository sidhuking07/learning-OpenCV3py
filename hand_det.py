import cv2
import numpy as np

cam = cv2.VideoCapture(0)

frame_dup = cv2.imread('frame_dup.jpg')
frame_dup = cv2.bitwise_not(frame_dup)

frame_backup = cv2.imread('frame_dup.jpg')
frame_backup = cv2.bitwise_not(frame_backup)

drawing = False

did = 0

lastcx =0
lastcy = 0


while True:
    tf, frame = cam.read()

    gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([130,150,130])
    upper_red = np.array([180,240,240])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    res = cv2.bitwise_and(frame,frame, mask= mask)
    res = cv2.medianBlur(res,5)

    resgs = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    imgret, mas = cv2.threshold(resgs, 30, 255, cv2.THRESH_BINARY_INV)
    im_,contours,hierarchy = cv2.findContours(mas, 1, 2)
    cnt = contours[0]

    M = cv2.moments(cnt)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

##    (x,y),radius = cv2.minEnclosingCircle(cnt)
##    center = (int(x),int(y))
##    radius = int(radius)
##    cv2.circle(mas,center,radius,(0,255,0),2)

    
    cv2.rectangle(frame, (10,10), (90,60), (255,0,0), -1)
    cv2.rectangle(frame, (100,10), (180,60), (0,0,255), -1)
    cv2.rectangle(frame, (190,10), (270,60), (0,255,0), -1)
    cv2.rectangle(frame, (300,10), (638,60), (255,255,255), 2)
    


    #cx = center[0]
    #cy = center[1]
    
    if not drawing:
        
        if cy >=10 and cy<=60:
            if cx>=10 and cx<=90:
                cv2.line(frame_dup, (cx,cy), (lastcx, lastcy), (255,0,0), 2, cv2.LINE_AA)
                did = 1
                drawing = True
            elif cx>=100 and cx<=180:
                cv2.line(frame_dup, (cx,cy), (lastcx, lastcy), (0,0,255), 2, cv2.LINE_AA)
                drawing = True
                did = 2
            elif cx>=190 and cx<=270:
                cv2.line(frame_dup, (cx,cy), (lastcx, lastcy), (0,255,0), 2, cv2.LINE_AA)
                drawing = True
                did = 3

    elif drawing:
        if cy >=10 and cy<=60:
            if cx>=10 and cx<=90:
                cv2.line(frame_dup, (cx,cy), (lastcx, lastcy), (255,0,0), 2, cv2.LINE_AA)
                did = 1
                drawing = True
            elif cx>=100 and cx<=180:
                cv2.line(frame_dup, (cx,cy), (lastcx, lastcy), (0,0,255), 2, cv2.LINE_AA)
                drawing = True
                did = 2
            elif cx>=190 and cx<=270:
                cv2.line(frame_dup, (cx,cy), (lastcx, lastcy), (0,255,0), 2, cv2.LINE_AA)
                drawing = True
                did = 3
        if cy>=10 and cy<=60 and cx>=300 and cx<=640:
            drawing = False
            frame_dup[:] = frame_backup[:]
            did = 0
        elif did == 1:
            cv2.line(frame_dup, (cx,cy), (lastcx, lastcy), (255,0,0), 2, cv2.LINE_AA)
        elif did == 2:
            cv2.line(frame_dup, (cx,cy), (lastcx, lastcy), (0,0,255), 2, cv2.LINE_AA)
        elif did == 3:
            cv2.line(frame_dup, (cx,cy), (lastcx, lastcy), (0,255,0), 2, cv2.LINE_AA)
    
    fin_frame = cv2.add(frame,  frame_dup)
    cv2.imshow('output', fin_frame)
    cv2.imshow('frame_dup', frame_dup)
##    cv2.imshow('mas', mas)
##    cv2.imshow('mask',mask)
    print cx,cy,"--",lastcx,lastcy

    lastcx = cx
    lastcy = cy

    k = cv2.waitKey(1)
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()
