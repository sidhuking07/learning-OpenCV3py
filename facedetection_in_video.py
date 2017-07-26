import cv2

cam = cv2.VideoCapture(0)

face_csc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    _tf, img = cam.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_csc.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (230,240,255), 2)

    cv2.imshow("img", img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()
