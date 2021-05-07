#Librerias
import numpy as np
import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':

    #Se obtiene la imagen con cv2
    print("Escribe el nombre de una imagen con su extensión que esté en la carpeta del proyecto:")
    image = cv2.imread(input())
    RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #convierte el espectro de color a RGB.

    # Muestra la imagen original por un plot.
    plt.imshow(RGB_img)
    plt.title("Imagen Original")
    plt.show()

    # Menu
    filtros = """
Aplicar filtro
1.- Filtro 1 - David
2.- Filtro 2 - Enrique
3.- Filtro 3 - Uriel
4.- Cambiar de imagen
5.- Salir                 
            """

    pop = True #Breack del ciclo while.
    while pop == True: #Ciclo while para imprimir filtros, cambiar imagen o salir.
        print(filtros)
        print("Elige una opcion:")
        op = input()

        if op == "1":
            print('Filtro David')
        elif op == "2":
            print('Filtro Enrique')
        elif op == "3":
            print('Filtro Uriel')
        elif op == "4":
            print('Cambio de imagen')
        elif op == "5":
            pop = False
        else:
            print("Opción inválida")
    #Termina el ciclo while