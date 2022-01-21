import cv2
cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    success,img = cap.read()
    faces = faceCascade.detectMultiScale(img,1.2,4)
    for (x,y,w,h) in faces:
        oui = img[y:y+h,x:x+w]
        blur = cv2.GaussianBlur(oui,(91,91),0)
        img[y:y+h, x:x+h] = blur
    if faces==():
        cv2.putText(img,'Pas de tête trouvée!',(20,25),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    cv2.imshow('Face Blur',img)
    if cv2.waitKey(1) & 0xff==ord(' '):
        break
cap.release()
cv2.destroyAllWindows()