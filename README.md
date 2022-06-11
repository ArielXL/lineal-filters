# Filtros Lineales

## Autor

| **Nombre y Apellidos** |         **Correo**         |               **GitHub**               |
| :--------------------: | :------------------------: | :------------------------------------: |
|  Ariel Plasencia Díaz  | arielplasencia00@gmail.com | [@ArielXL](https://github.com/ArielXL) |

## Resumen

En esta pequeña investigación, hablaremos acerca de los filtros lineales sobre imágenes en escala de grises. Además, profundizaremos en la sintaxis de la función `cv2.bilateralFilter()` utilizada por la librería `OpenCV` provista por el lenguaje de programación python y llevaremos a cabo diferentes ejemplos para una mejor y mayor comprensión. Como estudiamos en conferencias, para realizar el suavizado de imágenes se pueden utilizar tres tipos de técnicas de filtrado: desenfoque promedio, desenfoque gaussiano y desenfoque medio. Estos métodos difuminan o suavizan todo, independiente de si se trata de ruido o bordes, por lo que existe una pérdida importante de información en las imágenes. Para superar estos contratiempos proponemos el método de filtrado bilateral. Para más información consulte nuestro [informe](./doc/report.pdf).

## Implementación

La implementación se encuentra totalmente en [python 3](https://es.wikipedia.org/wiki/Python). Es recomendable tener conocimientos avanzados de este lenguaje de programación para una mayor y mejor entendimiento de las implementaciones propuestas.

## Ejecución

En el archivo [makefile](./src/makefile) proveemos una manera fácil, sencilla y rápida para correr nuestra implementación. 

Para la ejecución, escriba las siguientes líneas en una terminal abierta en este directorio: 

```bash
cd src/
make run
```



