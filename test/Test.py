import matplotlib
import pyautogui
"""
img = matplotlib.image.imread("abba.png")
matplotlib.pyplot.imshow(img)
figure, ax = pyplot.subplots(1)

rect = patches.Rectangle((125,100),50,25, edgecolor='r', facecolor="none")


nombre = 0
def carre(nombre):
    (x,y,w,h) = faces[nombre]
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
    pyautogui.moveTo(x1, y1, duration=0.5)
    pyautogui.moveRel(x1, y1, duration=0.5)



while keyboard.is_pressed(' '):
    start = pyautogui.locateCenterOnScreen(texte_image,region=(0,0,1920,1080),grayscale=True,confidence=0.70)
    if start is not None:
        pyautogui.moveTo(start)

def clique():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(1)
"""
print(pyautogui.position())

"""131 130
0 = 56 55 75 75
3 = 354  78  74  74
"""

aaa = "abba.png"
while not keyboard.is_pressed(' '):
    centre = pyautogui.locateCenterOnScreen(aaa,region=(0,0,1920,1080),grayscale=True,confidence=0.70)
    if centre is not None:
        pyautogui.moveTo(centre)