from tkinter import *
import pyautogui
import cv2


#Metodo de captura de pantalla
def fScreenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png") #Guardar imagen.
    
#Metodo de procesamiento de imagen 
def fProcesamiento():
    imgOriginal = cv2.imread("screenshot.png")
    imgProcesada = imgOriginal[180:638, 980:1353]
    cv2.imshow("IMG Procesada", imgProcesada) # solo para verificar si encuadra bien 
    cv2.imwrite('chat.png', imgProcesada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
root = Tk()

Button(root, text="Screenshot", command=fScreenshot).pack()
Button(root, text="Procesar", command=fProcesamiento).pack()

root.mainloop() 