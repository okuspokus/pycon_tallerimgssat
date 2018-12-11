<a href="https://eventos.python.org.ar/events/pyconar2018/activity/123/"><img src="https://pbs.twimg.com/profile_images/1025401970692186117/HFUmfob-_400x400.jpg" alt="PyCon Argentina" width="150px"></a>

# Imagenes satelitales en Python -- PyCon Argentina 2018

- Tipo: Taller
- Nivel: Principiante
- Disertantes: [Mariela Rajngewerc](https://github.com/okuspokus)
- Fork: [Pablo Sierra](https://github.com/pavelsjo)

**Resumen:** En este tutorial el objetivo será obtener un mapa de coberturas (suelo, agua, vegetación) a partir de una imagen satelital óptica. Comenzaremos seleccionando muestras de una imagen y analizando, mediante una comparación con firmas espectrales conocidas, a que cobertura pertecene cada muestra. Por último, utilizaremos las muestras para realizar una clasificación supervisada que dará como resultado el mapa buscado.



# Descripción Completa

Las imágenes satelitales cumplen un rol fundamental en el monitoreo terrestre, en particular en lugares de difícil acceso (humedales, glaciares, bosques, etc). En este tutorial trabajaremos con una imagen **Landsat8**. Este satelite monitorea constantemente la Tierra y tiene un tiempo de revisita de 16 días, o sea: una imagen cada 16 días. Estas imágenes son ópticas y gratuitas. 

El **objetivo principal** de este tutorial es mostrar con un ejemplo sencillo como clasificar una imagen satelital en Python. 

1. Para ello veremos como levantar una imagen satelital utilizando la librería **gdal**. 
2. Luego, seleccionaremos polígonos homogéneos de la imagen y graficaremos las firmas espectrales (la reflectancia reflejada en función la longitud de onda) de cada uno.
3. Compararemos las firmas calculadas con las firmas espectrales de las clases: agua, suelo y vegetación y decidiremos a qué clase representa cada polígono. 

Con esta información crearemos un dataset de datos etiquetados (a cada pıxel de cada polígono le asignamos la clase del polígono al que pertenece). Este será el conjunto de entrenamiento que utilizaremos para realizar una clasificación supervisada utilizando la librería sklearn. Por último obtendremos un mapa de cobertura.

# Datos

Realizaremos el taller utilizando la imagen [Landsat8: LC082250842018021301T1-SC20180427103449.tar](https://drive.google.com/file/d/1xggur3V0NFQLhu1L2gZx6rqnBYY1wh3g/view?usp=sharing)

Para abrir una imagen `.tif` en Python, hacemos lo siguiente:

```python
import gdal

gdal.Open('img.tif')
```

-----------------------------------------------------------------------------------------------

# Notebooks:

- [0.0-Taller-Imagenes-Python.ipynb](./notebook/0.0-Taller-Imagenes-Python.ipynb): para realizar el ejercicio.
- [0.1-Taller-Imagenes-Python-Soluciones.ipynb](./notebook/0.1-Taller-Imagenes-Python-Soluciones.ipynb): una posible solución.

Alternativa para realizar el ejercicio: [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pavelsjo/pycon_tallerimgssat/blob/master/taller_imgspython.ipynb\)

-------------------------------------------------------------------------------------------------
# Requisitos:

Este código ha sido probado con Python 3.7.1, y los paquetes necesarios para trabajar con este repositorio están listados en [requirements.txt](requirements.txt).

Para instalar los requerimientos en [conda](http://conda.pydata.org), ejecuta la siguiente línea de comandos en la terminal:

```
$ conda install --file requirements.txt
```

Si quieres crear un entorno aislado ``pycon_test`` con Python 3.5 y todos los paquetes requeridos, ejecuta el siguiente código:

```
$ conda create -n pycon_test python=3.7.1 --file requirements.txt
```

**Importante:** también utilizamos la libreria [roipoly.py](https://github.com/jdoepfert/roipoly.py)

---------------------------------------------------------------------