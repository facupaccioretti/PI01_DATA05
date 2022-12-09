from fastapi import FastAPI
import pandas as pd
import numpy as np

df_films = pd.read_csv('Datasets/films_df.csv')

app = FastAPI()

@app.get('/')
async def read_root():
    return {'primera API 001'}

@app.get('/get_actor')
async def get_actor(plataforma, año):
    return {'hello world'}

@app.get('/getmaxduration')
async def getmaxduration():
    return {'hello world'}

## consulta numero 1: Máxima duración según tipo de film (película/serie), por plataforma y por año. 


app.get("/get_max_duration/")
async def get_max_duration(Año:int, Plataforma:str, Tipo:str):
    df3= df_films[((df_films['Plataforma'] == Plataforma) & (df_films['año_lanzamiento'] == Año)& (df_films['Tipo'] == Tipo))]
    maximo = df3.Duracion.max()
    film = df3[df3.Duracion == maximo]['Titulo']

    return 'El film de mayor duración es '+ film

## consulta numero 2: Cantidad de películas y series (separado) por plataforma.

@app.get("/Cantidad de films por plataforma/")
async def get_count_plataforma(plataforma:str):
    a = df_films[(df_films['Plataforma'].str.contains(plataforma) & (df_films['Tipo'].str.contains('Movie')))].shape[0]
    b = df_films[(df_films['Plataforma'].str.contains(plataforma) & (df_films['Tipo'].str.contains('TV Show')))].shape[0]
    return a,b


## consulta numero 3: Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
@app.get('/Cantidad de veces que se repite un genero y plataforma/')
async def get_listedin(genero:str):

    a=df_films[df_films['generos'].str.contains(genero) & (df_films['Plataforma'] == 'Amazon Prime')].shape[0]
    b=df_films[df_films['generos'].str.contains(genero) & (df_films['Plataforma'] == 'Disney Plus')].shape[0]
    c=df_films[df_films['generos'].str.contains(genero) & (df_films['Plataforma'] == 'Hulu')].shape[0]
    d=df_films[df_films['generos'].str.contains(genero) & (df_films['Plataforma'] == 'Netflix')].shape[0]
    
    maximo = max(a,b,c,d)
    if maximo == a:
        plataforma = 'Amazon Prime'
    elif maximo == b:
        plataforma = 'Disney Plus'
    elif maximo == c:
        plataforma = 'Hulu'
    elif maximo == d:
        plataforma = 'Netflix'


    return 'La plataforma en la que más se repite este género es en '+ plataforma
