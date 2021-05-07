import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt

# Función que multiplica la matriz de image con la de kernel y devuelve la suma de esta
def conv_helper(fragment, kernel):
    f_row, f_col = fragment.shape
    k_row, k_col = kernel.shape
    result = 0.0
    for row in range(f_row):
        for col in range(f_col):
            result += fragment[row,col] *  kernel[row,col]
    return result

# Función de convolución sin padding que devuelve la matriz resultante del mismo tamaño de la matriz image
def convolution(image, kernel):

    if len(image.shape) == 3:
        print("Found 3 Channels : {}".format(image.shape))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("Converted to Gray Channel. Size : {}".format(image.shape))
    else:
        print("Image Shape : {}".format(image.shape))

    print("Kernel Shape : {}".format(kernel.shape))

    # Impresión de matriz image
    print('Kernel')
    # Impresión de filtro kernel
    for row in kernel:
            for col in row:
                print(col ,end=' ')
            print(end='\n')

    image_row, image_col = image.shape # obtiene tupla con las medidas de alto y ancho de la imagen
    kernel_row, kernel_col = kernel.shape # obtiene tupla con las medidas de alto y ancho el filtro

    output = np.zeros(image.shape) # Matriz vacía del tamaño de la imágen para guardar el resultado

    pad_height = int((kernel_row - 1) / 2)
    pad_width = int((kernel_col - 1) / 2)

    padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))
    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image

    print("Padded image:")
    print(padded_image)

    # Mostrar el plot de la imágen con padding
    plt.imshow(padded_image, cmap='gray')
    plt.title("Padded Image of {}X{}".format(image_row, image_col))
    plt.show()

    for row in range(image_row):
        for col in range(image_col):
                output[row, col] = np.sum(kernel * padded_image[row:row + kernel_row, col:col + kernel_col])
    
    print("Output Image size : {}".format(output.shape))
    
    # Mostrar el plot del resultado con filtro
    plt.imshow(output, cmap='gray')
    plt.title("Output Image using {}X{} Kernel".format(kernel_row, kernel_col))
    plt.show()

    return output

if __name__ == '__main__':

    # Matriz de filtro Sobel
    filter = np.array([ [-1,0,1],
                        [-2,0,2],
                        [-1,0,1]])

    # obtiene la imagen de la linea de comando "python convolution_enrique.py -i naruto.png"
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path of image")
    args = vars(ap.parse_args())

    # cambia la imagen a formato numerico, matriz de 3 dimensiones rgb
    image = cv2.imread(args["image"])

    RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(RGB_img, cmap='gray')
    plt.title("Original Image")
    plt.show()

    # Se usa el print para ver la matriz resultante
    convolution(image, filter)