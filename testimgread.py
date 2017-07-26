import cv2

img = cv2.imread('Sid.jpg')

print img
cv2.imshow('HAHAHA', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
