import cv2
import win32api, win32con
import pyautogui

texte_image = input("Entrer le nom de l'image avec l'extension:")
image_voulue =texte_image
cascPath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(image_voulue)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1, #Essayer 1.2 si bug
    minNeighbors=5,
    minSize=(30, 30))

def carre():
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)

def souris(x,y):
    pyautogui.moveTo(x,y,duration=0.5)
    pyautogui.moveRel(x,y,duration=0.5)

def clique():
    pyautogui.click()

print("{0} Tête trouvée".format(len(faces)))



cv2.imshow("Tete trouvee", image)
cv2.waitKey(0)