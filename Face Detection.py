import cv2
faceDetect = cv2.CascadeClassifier('haarcascade file/haarcascade_frontalface_default.xml')

img_path="movie_img.png"
img=cv2.imread(img_path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceDetect.detectMultiScale(gray, 1.5, 5);
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
    pass
cv2.imshow("Face Detection on Photos",img)
