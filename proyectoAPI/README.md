# Proyecto  API
en este proyecto uso una API suministrada por el[portal nacional de datos](https://www.datos.gov.co/) de colombia, la informacion que esta API nos suministra son datos referentes a personas contagiadas con covid-19. para el manejo de la API se usa la libreira [sodapy](https://pypi.org/project/sodapy/), y de esta libreria en especifico se importa la clase ***Socrata*** que es con la que se extraen los datos de la direccion, para esta extraccion tambien se hace uso de una *key* que se encuentra en el codigo.

El objetivo es crear un proyecto capaz de extraer la informacion de esta pagina, filtrar los datos y visualizar estos mismos en una tabla de manera eficiente. el cliente es quien debe de especificar los filtros necesarios para la visualizacion. el programa tambien es capaz de reconocer algunos errores como inexistencia de parametros en los filtros,desbordamiento de la capacidad de la API y algunos otros mas..

Los datos a evidenciar en la tabla son:
* Ciudad
* Departamento
* Edad
* Tipo
* Estado
* Procedencia

## API

En este archivo .py extraemos toda la informacion que la API nos proporciona, luego usamos la libreria [pandas](https://pandas.pydata.org/) para convertir el json que nos entrega la API a un dataframe mucho mas facil de manejar para posteriormente entregarle esta info a la interfaz. en este archivo tambien tenemos una funcion que nos filtra unicamente las columnas que especificamos al principio, puesto que la API entrega numerosa cantidad de columnas mas que no usaremos.

## UI

Este archivo se encarga de la interfaz, en este menu definimos los departamentos, creamos el menú, pedimos los parametros y visualizamos los datos que se solicitan. el menú que se usa es un menu repetitivo que interrumpe y cierra el programa cuando ya no se necesitan mas datos y se selecciona la opcion **"N"**, esta interfaz pide todos los datos que se necesitan ára la visualizacion a la seccion API previamente explicada.

## main

Solo se usa para la ejecucion del programa, este archivo solo requiere del UI y en realidad es innecesario, pues se podría ejecutar sin problemas desde el UI, solo lo usé para respetar los lineamientos de una buena arquitectura segun el libro ***"clean code"***.

## resultados

![alt text](https://github.com/juan-suarez/miniproyectos-python/blob/main/imagenes/unusual.jpg)
![alt text](https://github.com/juan-suarez/miniproyectos-python/blob/main/imagenes/usual.jpg)
