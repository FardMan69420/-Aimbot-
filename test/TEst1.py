import cv2
import numpy
import sys
import pyautogui
import win32api,win32con
import time
import keyboard

texte_image = input("Entrer le nom de l'image avec l'extension:")
fichierdetection = "haarcascade_frontalface_default.xml"

visage = cv2.CascadeClassifier(fichierdetection)

image = cv2.imread(texte_image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = visage.detectMultiScale(
    gray,
    scaleFactor=1.1, #Essayer 1.2 si bug
    minNeighbors=5,
    minSize=(30, 30))

print("{0} Tête trouvée".format(len(faces)))


def clique(event,x,y,flag,param):
    h2, w2, _ = image.shape
    h2 = h2/2
    w2 = w2/2
    if event == cv2.EVENT_LBUTTONDOWN:
        centre = pyautogui.locateCenterOnScreen(texte_image, region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
        pyautogui.moveTo(centre)
        (x1, y1, w1, h1) = faces[nombre]
        (x2, y2) = pyautogui.position()
        x3 = x2-w2
        y3 = (y2+8)-h2
        pyautogui.moveTo(x2-w2, y2-h2)
        pyautogui.moveTo(x3+x1,y3+y1, duration=0.2)
        cv2.rectangle(image, (x1, y1), (x1 + w1, y1 + h1), (255, 255, 0), 2)

cv2.namedWindow(texte_image)
cv2.setMouseCallback(texte_image,clique)
while True:
    cv2.imshow(texte_image, image)
    k = cv2.waitKey(1)
    if k == 27:
        cv2.destroyAllWindows()
        break