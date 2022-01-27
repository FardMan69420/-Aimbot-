import cv2
import pyautogui
import time

texte_image = input("Entrer le nom de l'image avec l'extension:")
fichierdetection = "haarcascade_frontalface_default.xml"

visage = cv2.CascadeClassifier(fichierdetection)

image = cv2.imread(texte_image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = visage.detectMultiScale(            #Augmenter les valeurs en cas de tête trop grosse
    gray,
    scaleFactor=1.1,                        #Essayer 1.2 voir 1.3 si bug
    minNeighbors=5,
    minSize=(30, 30))

print("{0} Tête trouvée".format(len(faces)))


def milieu():
    centre = pyautogui.locateCenterOnScreen(texte_image, region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    pyautogui.moveTo(centre)


def coordonnees():
    nombre = len(faces) - 1
    h2, w2, _ = image.shape
    h2 = h2 / 2
    w2 = w2 / 2
    (x2, y2) = pyautogui.position()
    x3 = x2 - w2
    y3 = (y2 + 8) - h2
    for i in range(len(faces)):
        (x1, y1, w1, h1) = faces[nombre]
        pyautogui.moveTo(x2 - w2, y2 - h2)
        pyautogui.moveTo(x3 + x1, y3 + y1, duration=0.2)
        cv2.rectangle(image, (x1, y1), (x1 + w1, y1 + h1), (255, 255, 0), 2)
        cv2.imshow(texte_image, image)
        cv2.waitKey(0)
        time.sleep(0.1)
        nombre = nombre - 1


def clique(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        milieu()
        coordonnees()


cv2.namedWindow(texte_image)
cv2.setMouseCallback(texte_image, clique)

while True:
    cv2.imshow(texte_image, image)
    echap = cv2.waitKey(1)
    if echap == 27:
        cv2.destroyAllWindows()
        break
