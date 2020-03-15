import cv2

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture("elon.jpg")

res, img = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

cv2.imshow('Image',img)
k = cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()

#this is a new comment
