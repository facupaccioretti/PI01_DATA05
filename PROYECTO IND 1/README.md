<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**'Proyecto individual Facundo Paccioretti - HENRY DTS-05'**</h1>

<p align="center">
<img src=""  height=300>
</p>



<hr>  

## **Introducción**



En el siguiente proyecto tuve como objetivo realizar distintas labores del area de data engineering. Las principales consignas eran: 
<p align=center>
Ingesta y normalización de datos
<p align=center>
Relacionar el conjunto de datos y crear la tabla necesaria para realizar consultas. Aquí se recomienda corroborar qué datos necesitarán en base a las consultas a realizar y concatenar las 4 tablas
<p align=center>
Leer documentación en links provistos e indagar sobre Uvicorn, FastAPI y Docker
<p align=center>
Crear la API en un entorno Docker → leer documentación en links provistos
<p align=center>
Realizar consultas solicitadas
<p align=center>
Realizar un video demostrativo


## **Ingesta y normalización**

En primer lugar realice la ingesta de datos con pandas y python. Con pandas cree diversos dataframes donde importe los csv y json que me brindaron. Luego tambien con pandas le realice ciertas transformaciones al dataframe para poder limpiar los datos, normalizarlos, trabajar con los datos faltantes y ordenar nuestro dataframe.
## **Querys**
Posteriormente genere ciertas consultas a nuestra base de datos con python y pandas.
Las consultas realizadas son:
+ get_max_duration(año, plataforma, [min o season]): Máxima duración según tipo de film (película/serie), por plataforma y por año:
  
+ get_count_plataform(plataforma): Cantidad de películas y series (separado) por plataforma
+ get_listedin('genero'): Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
+ get_actor(plataforma, año): Actor que más se repite según plataforma y año.
 
## **API: Uvicorn, fastAPI y docker**

Posteriormente indague en distintas fuentes sobre uvicorn, fastapi y docker. Estas eran las herramientas que debia utilizar para generar un ambiente sobre el cual se pudiera consultar mi base de datos.
Utilice docker para generar un contenedor y dentro de el cree una imagen de Docker desde cero. 
Utilice uvicorn para crear una implementación de servidor web ASGI con Python.
Luego utilice fastAPI (un marco web moderno, rápido y de alto rendimiento) y cree la api con python.
Allí se puede acceder y ejecutar las consultas.


## **Recursos y links provistos**

Imagen Docker con Uvicorn/Guinicorn para aplicaciones web de alta performance:

+ https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/ 

+ https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

Mogenius Deployment

+ https://mogenius.com/home  

FAST API Documentation:

+ https://fastapi.tiangolo.com/tutorial/

