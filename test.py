from tkinter import *
import pyautogui
import cv2
import pytesseract


#Metodo de captura de pantalla
def fScreenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png") #Guardar imagen.
    
#Metodo de procesamiento de imagen 
def fProesamiento():
    imgOriginal = cv2.imread("screenshot.png")
    imgProcesada = imgOriginal[180:638, 980:1353]
    cv2.imshow("IMG Procesada", imgProcesada) # solo para verificar si encuadra bien 
    cv2.imwrite('chat.png', imgProcesada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def fAnalizar():
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  
    img = cv2.imread("chat.png")

    #custom_config = r'--oem 3 --psm 6' # metodos de deteccion opcional
    text = pytesseract.image_to_string(img,lang = 'spa')
    guardarDatos(text)

    

def guardarDatos(text):
    datos=open("datos.txt","w") 
    datos.write(text) 
    datos.close() 

    #print(text)
    
root = Tk()
#estilo del boton
fuente="-weight bold"

Button(root, text="Screenshot",font=fuente,relief="flat", borderwidth=5,width=10, height=3,background="#AED6F1", command=fScreenshot).pack()
Button(root, text=" Procesar ",font=fuente,relief="flat", borderwidth=5,width=10, height=3,background="#85C1E9", command=fProesamiento).pack()
Button(root, text=" Analizar ",font=fuente,relief="flat", borderwidth=5,width=10, height=3,background="#5DADE2", command=fAnalizar).pack()

root.mainloop() 
#2ECC71