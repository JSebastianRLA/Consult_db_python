from flask import Flask, render_template
import asyncio
import aiomysql

app = Flask(__name__)

@app.route('/')
async def mostrar_registros():
    registros = await obtener_registros()
    return render_template('registros.html', registros=registros)

async def obtener_registros():
    conn = await aiomysql.connect(host='localhost', user='prueba_conecction', password='Aa123.', db='IMSI', autocommit=True)
    async with conn.cursor() as cur:
        await cur.execute("SELECT * FROM ImsiMigrations")
        rows = await cur.fetchall()
    conn.close()
    return rows

if __name__ == '__main__':
    app.run(host='192.168.0.196', port=5000)
