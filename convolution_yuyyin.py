import numpy as np   #numpy es una libreria de python
import cv2           #import cv2 libreria de python
import matplotlib.pyplot as plt #marplotlib.pyplot es otra de las librerias de python

def conv_helper(fragment, kernel):
    """ multiplica 2 matices y devuelve su suma"""
    
    f_row, f_col = fragment.shape
    k_row, k_col = kernel.shape 
    result = 0

    for row in range(f_row):
        for col in range(f_col):
            result += fragment[row,col] *  kernel[row,col]
    return result

def convolution(image, kernel):
    """Aplica una convolucion sin padding (valida) de una dimesion 
    y devuelve la matriz resultante de la operación
    """
#Se encuentra la dimencion de la imagen
    if len(image.shape) == 3: #De 3 dimenciones
        print("Dimenciones de imagen: {}".format(image.shape))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Se cambia a dos dimenciones
        print("Nuevas dimenciones: {}".format(image.shape))
    else:
        print("Dimenciones de imagen: {}".format(image.shape))

    image_row, image_col = image.shape #asigna alto y ancho de la imagen 
    kernel_row, kernel_col = kernel.shape #asigna alto y ancho del filtro
    
    output_x = (image_col - (kernel_col / 2) * 2) + 1 
    output_y = (image_row - (kernel_row / 2) * 2) + 1 
    
    output = np.zeros([int(output_y), int(output_x)]) #Matriz donde guardo el resultado

    for row in range(int(output_y)):
        for col in range(int(output_x)):
            output[row, col] = conv_helper(
                                image[row:row + kernel_row, 
                                col:col + kernel_col],kernel)
    plt.imshow(output, cmap='gray')
    plt.title("Filtro aplicado")
    plt.show()
    
    return output

if __name__ == '__main__':
#Imagen de prueba.
    image = cv2.imread("naruto.png")
#Filtro line detectition Horizontal.
    filter = np.array([[-1,-1,-1],
                    [2,2,2],
                    [-1,-1,-1]]) 

print("Filter: ")
print(filter) #Se impmrime la matriz de filtro.
convolution(image, filter) # Se manda a llamar la funcion.