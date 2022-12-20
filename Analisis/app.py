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


@app.route('/perfil')
def cliente():
    clientes = recibir_clientes()
    for i in clientes:
        if i[0]==1:
            cliente = i
    ct = cliente[3] - cliente[4]
    return render_template("perfil.html", cliente=cliente, total = ct)

@app.route('/analisis')
def client():
    client = recibir_clientes()
    for i in client:
        if i[0]==1:
            client = i
    cct = client[3] - client[4]
    return render_template("analisis.html", client=client, total = cct)

if __name__ == '__main__':
    app.run(debug=True,port=9000)
