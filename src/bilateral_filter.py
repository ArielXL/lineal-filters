import cv2
from image import Image

def bilateral_filter(image):
    '''
    Muestra la imagen parametro con el filtro bilateral.
    '''

    # Image.show_image(image)
    bilateral_filter_image = cv2.bilateralFilter(image, 15, 80, 80)
    # Image.show_image(bilateral_filter_image)
    Image.show_images([image, bilateral_filter_image])

    Image.plt_show()

if __name__ == '__main__':

    image = Image.load_image('../img/cameraman.tif')
    bilateral_filter(image)
