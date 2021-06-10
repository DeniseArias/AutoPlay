import pyautogui as auto
import time

canciones = ["El flautista", "Cien años"]
nav = 580,742
url = 387,64
busc = 389,111
video = 381,275
cerrar = 1344,17
duracion = 10

# funcion para mover mouse y dar click
def Abrir(posicion,clic=1):
    auto.moveTo(posicion)
    time.sleep(3)
    auto.click(clicks = clic)

# Abrir navegador
Abrir(nav,clic=1)
time.sleep(2)

# Asegurarnos de pantala completa
auto.hotkey('alt','space')
time.sleep(0.5)
auto.typewrite('x')

# Ubicarnos en el buscador
time.sleep(4)
Abrir(url)
auto.typewrite('www.youtube.com')
auto.hotkey('enter')
time.sleep(5)

# Reproducir canciones
for cancion in canciones:
    Abrir(busc, clic= 3)
    auto.typewrite(cancion)
    auto.hotkey('enter')
    time.sleep(2)
    Abrir(video)
    time.sleep(duracion)

Abrir(cerrar)
print('fin proceso')

