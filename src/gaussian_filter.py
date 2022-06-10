import cv2
from image import Image

def gaussian_filter(image):
    '''
    Muestra la imagen parametro con el filtro gaussiano.
    '''

    # Image.show_image(image)
    gaussian_blur_filter_image = cv2.GaussianBlur(image, (5,5), sigmaX=0)
    # Image.show_image(gaussian_blur_filter_image)
    Image.show_images([image, gaussian_blur_filter_image])

    Image.plt_show()

if __name__ == '__main__':
    
    image = Image.load_image('../img/cameraman.tif')
    gaussian_filter(image)
