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
    for i in clientes:
        if i[0]==1:
            cliente = i
    ct = cliente[3] - cliente[4]
    return render_template("perfil.html", cliente=cliente, total = ct)
    
@app.route('/login')
def login():
    
    return render_template("iniciosesion.html")

@app.route('/registro')
def registro():
    
    return render_template("registro.html")


@app.route('/analiza_empresas')
def analiza_empresas():
    return render_template('empresas.html')

 
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
