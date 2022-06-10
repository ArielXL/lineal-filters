import cv2
from image import Image

def median_filter(image):
    '''
    Muestra la imagen parametro con el filtro de la mediana.
    '''

    # Image.show_image(image)
    median_blur_filter_image = cv2.medianBlur(image, 5)
    # Image.show_image(median_blur_filter_image)
    Image.show_images([image, median_blur_filter_image])

    Image.plt_show()

if __name__ == '__main__':
    
    image = Image.load_image('../img/cameraman.tif')
    median_filter(image)
