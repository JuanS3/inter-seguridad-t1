import sqlite3
import uvicorn
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse


app = FastAPI(title='Series Tiempo API', description='API para consultar series de tiempo')


DATABASE_PATH = 'db/series-tiempo.sqlite'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    print('Hola')
    return conn


@app.get('/')
async def get_hello():
    return {'message': 'INTER 2025-1 Taller 1 - Seguridad en Aplicaciones | SQL Injection'}


@app.get('/catalogo/{catalogo}')
async def get_catalogo(catalogo: str):
    try:
        conn = get_db_connection()
        query = f'''
        SELECT serie_id
             , catalogo_id
             , indice_tiempo_frecuencia
             , serie_titulo
             , serie_unidades
        FROM metadatos
        WHERE catalogo_id = "{catalogo}"
        '''
        catalogo = pd.read_sql_query(query, conn)
        conn.close()
        return HTMLResponse(catalogo.to_html())
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/serie_titulo')
async def get_serie_titulo(titulo: str):
    try:
        conn = get_db_connection()
        query = f'''
        SELECT serie_id
             , catalogo_id
             , indice_tiempo_frecuencia
             , serie_titulo
             , serie_unidades
        FROM metadatos
        WHERE serie_titulo = "{titulo}"
        '''
        series = pd.read_sql_query(query, conn)
        conn.close()
        return series
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/dataset/{data}")
async def get_full_data(data: str = ''):
    try:
        conn = get_db_connection()
        query = f'''
        SELECT *
        FROM metadatos
        WHERE dataset_id = '{data}'
        '''
        catalogo = pd.read_sql_query(query, conn)
        conn.close()
        return HTMLResponse(catalogo.to_html())
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)