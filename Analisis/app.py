from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

#conect database
def conectar():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    return db, cursor

#cerrar conexion
def cerrar(conn):
    conn.commit()
    conn.close()

# conectamos a la base y guardamos en una lista
def recibir_clientes():
    db, cursor = conectar()
    cursor.execute("SELECT * FROM clientes")
    clientes = (cursor.fetchall())
    cerrar(db)
    return clientes



@app.route('/')
def clientes():
    clientes = recibir_clientes()
    return render_template("lista.html", clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True,port=000)
