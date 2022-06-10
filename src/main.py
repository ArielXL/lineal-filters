from image import Image
from median_filter import median_filter
from gaussian_filter import gaussian_filter
from bilateral_filter import bilateral_filter

def print_options():
    print('SELECCIONA LA OPCION DESEADA:')
    print('1. Filtro Bilateral')
    print('2. Filtro Gaussiano')
    print('3. Filtro de la Mediana')
    option = input()
    return option

def main():

    image = Image.load_image('../img/cameraman.tif')
    option = print_options()
    if option == '1':
        bilateral_filter(image)
    elif option == '2':
        gaussian_filter(image)
    elif option == '3':
        median_filter(image)
    else:
        print('OPCION INVALIDA')

if __name__ == '__main__':
    main()