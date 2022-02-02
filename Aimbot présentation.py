import cv2
import pyautogui
import time

texte_image = input("Entrer le nom de l'image avec l'extension:")   #trouver le nom de l'image
fichierdetection = "haarcascade_frontalface_default.xml"

visage = cv2.CascadeClassifier(fichierdetection)        #Méthode pour détecter les visages/têtes en utilisant le fichier xml précisé en haut

image = cv2.imread(texte_image)                     #lire l'image et le mettre en données/chiffre
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)      #Pour transformer les couleurs noirs et blancs(nuances de gris) et simplifier la détection

faces = visage.detectMultiScale(            #Augmenter les valeurs en cas de tête trop grosse
    gray,
    scaleFactor=1.1,                        #Essayer 1.2 voir 1.3 si bug
    minNeighbors=5,
    minSize=(30, 30))

print("{0} Tête trouvée".format(len(faces)))


def milieu():           #Fonction servant a détecter une image sur l'écran puis trouver le milieu de l'image et aller dessus
    centre = pyautogui.locateCenterOnScreen(texte_image, region=(0, 0, 1920, 1080), grayscale=True, confidence=0.70)
    pyautogui.moveTo(centre)


def coordonnees():      
    nombre = len(faces) - 1
    h2, w2, _ = image.shape  #dimension de l'image
    h2 = h2 / 2                     #aller en haut a gauche de l'image donc la position h2-w2 w2-w2 = la position 0, 0 de l'image
    w2 = w2 / 2                     #car ce n'est pas la position sur l'écran de résolution 1920 1080
    (x2, y2) = pyautogui.position()
    x3 = x2 - w2
    y3 = (y2 + 8) - h2
    for i in range(len(faces)):         #mettre un carré puis montrer l'image a nouveau qui aura été actualisée
        (x1, y1, w1, h1) = faces[nombre]
        pyautogui.moveTo(x2 - w2, y2 - h2)
        pyautogui.moveTo(x3 + x1 +w1/2, y3 + y1+h1/2, duration=0.2)
        cv2.rectangle(image, (x1, y1), (x1 + w1, y1 + h1), (255, 255, 0), 2)
        cv2.imshow(texte_image, image)
        cv2.waitKey(0)
        time.sleep(0.1)
        nombre = nombre - 1


def clique(event, x, y, flag, param):       #Si clique gauche faire :
    if event == cv2.EVENT_LBUTTONDOWN:      #remplacer par cv2.EVENT_RBUTTONDOWN: pour clique droit
        milieu()
        coordonnees()


cv2.namedWindow(texte_image)            #renommer la fenetre dans laquelle l'image s'ouvre
cv2.setMouseCallback(texte_image, clique)       #détecter les mouvements de souris

while True:                 # Pouvoir fermer l'image en appuyant sur Echap
    cv2.imshow(texte_image, image)
    echap = cv2.waitKey(1)
    if echap == 27:
        cv2.destroyAllWindows()
        break
