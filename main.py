#Librerias
import numpy as np
import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':

    #Se obtiene la imagen con cv2
    print("Escribe el nombre de una imagen que este en la carpeta del proyecto:")
    image = cv2.imread(input())
    RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #convierte el espectro de color a RGB

    #Impresion de imagen
    plt.imshow(RGB_img, cmap='gray')
    plt.title("Imagen")
    plt.show()