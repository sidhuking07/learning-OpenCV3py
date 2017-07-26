import cv2

img = cv2.imread('2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 1)


cv2.imshow('HAHAHA', gaus)
cv2.imwrite('edited_2.jpg',gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()
