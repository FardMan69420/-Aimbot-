import cv2
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

print("{0} Tête trouvée".format(len(faces)))

nombre = 0
def carre(nombre):
    (x,y,w,h) = faces[nombre]
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
    x1 = (x+y)/2
    y1 = (w+h)/2
    pyautogui.moveTo(x1, y1, duration=0.5)
    pyautogui.moveRel(x1, y1, duration=0.5)

def clique():
    pyautogui.click()

nbrtete = len(faces)
cv2.imshow("Tete trouvee", image)
while nombre<=nbrtete:
    carre(nombre)
    clique()
    if clique():
         nombre = nombre + 1
cv2.waitKey(0)
