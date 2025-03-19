from flask import Flask,render_template,request,redirect
import mysql.connector

app=Flask(__name__)
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="rcitas"
    )

@app.route("/")#ruta principal
def home():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tbl_citas JOIN tbl_es ON tbl_citas.Estado = tbl_es.id")
    citas=cursor.fetchall() 
    cursor.execute("SELECT * FROM tbl_es")
    ess = cursor.fetchall()   
    conn.close()
    return render_template('index.html',citas=citas,ess=ess)    




@app.route('/add',methods=['POST'])
def addas():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO tbl_citas (Nombre,Fecha,Hora,Estado,Descripcion) VALUES (%s, %s, %s,%s,%s)", 
                   (request.form['nombre'],request.form['fecha'],request.form['hora'],3,request.form['descripcion']))

    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def updateas(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tbl_citas SET Nombre = %s, Fecha= %s, Hora=%s,Estado=%s,Descripcion=%s WHERE id = %s", 
                   (request.form['nombre'], request.form['fecha'],request.form['hora'],request.form['estado'],request.form['descripcion'], id))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn=get_db_connection()
    cursor=conn.cursor()

    cursor.execute("DELETE FROM tbl_citas WHERE Id = %s",(id,))
    conn.commit()
    conn.close()
    return redirect('/')





"""
@app.route("/")#ruta principal
def home():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM materiales")
    mat=cursor.fetchall()
    conn.close()
    return render_template('index.html',materiales=mat)
@app.route('/add',methods=['POST'])
def add():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO materiales (materiales,cantidad,precio) VALUES (%s, %s, %s)", (request.form['material'],request.form['cant'],request.form['precio']))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM materiales WHERE Id = %s",(id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE materiales SET materiales = %s,cantidad = %s,precio = %s WHERE id = %s", (request.form['material'],request.form['cantmat'],request.form['precio'], id))
    conn.commit()
    conn.close()
    return redirect('/')
    """
