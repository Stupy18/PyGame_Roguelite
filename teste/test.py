from PythonFiles.pygame_functions import *


screenSize(1280,720)

rocket=makeSprite("E:\Probabilitati\Joc\stupy.png")
showSprite(rocket)
addSpriteImage(rocket,"E:\Probabilitati\Joc\linii.jpg")
for x in range(0,300):
    moveSprite(rocket,x,300)
    changeSpriteImage(rocket, x % 20 == 0)


endWait()
