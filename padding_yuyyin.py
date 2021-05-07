#libreria para matrices "numpy".
import numpy as np

#Función del padding .
def pading(image,pad):

    irow,icol=image.shape  #Tamaño de la matriz.

    output = np.zeros(image.shape) #Matriz de 0.
    
    padded_image = np.zeros((irow + (2 * pad), icol + (2 * pad)))
    padded_image[pad:padded_image.shape[0] - pad, pad:padded_image.shape[1] - pad] = image
    
    print(padded_image)

if __name__ == '__main__':

#Matriz de prueba para la función.
    image = np.array([[1,3,43,1,2,3],
                    [7,0,0,9,1,12],
                    [0,1,2,16,17,20],
                    [0,0,0,7,100,22],
                    ])

    pad = 1 #Tamaño del pad.

pading(image,pad)  # Se llama la función.