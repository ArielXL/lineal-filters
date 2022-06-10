import cv2
import matplotlib.pyplot as plt

class Image:

    @staticmethod
    def load_image(path):
        '''
        Carga la imagen en la ruta especificada.
        '''
        image = cv2.imread(path)
        return image

    @staticmethod
    def show_image(image):
        '''
        Carga la imagen especificada.
        '''
        plt.imshow(image, cmap='gray')
        # plt.show()

    @staticmethod
    def show_images(images):
        '''
        Carga las imagenes especificadas.
        '''
        count_image = len(images)
        fig, axs = plt.subplots(1, count_image)

        for i,image in enumerate(images):
            axs[i].imshow(image, cmap='gray')

        # plt.show()

    @staticmethod
    def plt_show():
        '''
        Muestra todas las imagenes cargadas.
        '''
        plt.show()

    @staticmethod
    def save_image(image, path):
        '''
        Guarda la imagen en la ruta especificada.
        '''
        cv2.imwrite(path, image)
