import cv2

haar_cascode = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cam = cv2.VideoCapture(0)

while True:
    _,img = cam.read()

    grayImg = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
    faces = haar_cascode.detectMultiScale(grayImg,1.3,4)

    for (x,y,w,h)in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Face Dectection ",img)
    key = cv2.waitKey(10)
    print(key)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
