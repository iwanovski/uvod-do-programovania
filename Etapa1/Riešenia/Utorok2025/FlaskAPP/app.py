from pydantic import BaseModel
import sqlite3
from uuid import uuid4
from flask import Flask, render_template, redirect, url_for, request

# Class
class User(BaseModel):
    id: str
    name: str
    surname: str
    age: int


# Functions
con = sqlite3.connect("db.db", check_same_thread=False)
cur = con.cursor()


# cur.execute("CREATE TABLE user(id, name, surname, age)")

def vylistuj_uzivatelov():
    result = cur.execute("SELECT * from user")
    return result.fetchall()

def nacitaj_uzivatela(user_id):
    result = cur.execute(f"SELECT * from user WHERE id = '{user_id}'")
    return result.fetchone()

def pridaj_uzivatela(name, surname, age):
    my_id = str(uuid4())
    user = User(id=my_id, name=name, surname=surname, age=age)
    cur.execute(f"INSERT INTO user VALUES ('{user.id}','{user.name}','{user.surname}',{user.age})")
    con.commit()
    

def aktualizacia_uzivatela(my_id, name, surname, age):
    User(id=my_id, name=name, surname=surname, age=age)
    query = "UPDATE user SET name = ?, surname = ?, age = ? WHERE id = ?"
    cur.execute(query, (name, surname, age, my_id))
    con.commit()

def zmaz_uzivatela(my_id):
    cur.execute(f"DELETE FROM user WHERE id ='{my_id}'")
    con.commit()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('hello.html')

@app.route("/sk")
def ahoj_svet():
    return "<p>Ahoj, Svet!</p>"

@app.route("/users")
def get_users():
    users = vylistuj_uzivatelov()
    return render_template('list.html', users=users)

@app.route("/users/<id>")
def fetch_user(id):
    user = nacitaj_uzivatela(id)
    return render_template('detail.html', user=user)

@app.route("/users/<id>/delete", methods=["POST"])
def delete_user(id):
    zmaz_uzivatela(id)
    # return redirect('/users')
    return redirect(url_for('get_users'))

# Nacitanie formularu
@app.route("/users/new")
def create_user_form():
    return render_template('create_user.html')

# Zmena dat na zaklade udajov z formularu
@app.route("/users/new", methods=["POST"])
def create_user():
    name = request.form.get('name')
    surname = request.form.get('surname')
    age = request.form.get('age')
    pridaj_uzivatela(name, surname, int(age))
    return redirect(url_for('get_users')) 
    
@app.route('/users/<id>/update', methods=("GET", "POST"))
def update_user(id):
    user = nacitaj_uzivatela(id)
    if not user:
        return "User not found", 404

    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        age = request.form.get("age")
        if name and age:
            try:
                aktualizacia_uzivatela(id, name, surname, int(age))
                return redirect(url_for('fetch_user', id=id))
            except Exception as e:
                error = f"Failed to update user: {e}"
                return render_template('update_user.html', user=user, error=error)
        else:
            error = "Please provide both name and age."
            return render_template('update_user.html', user=user, error=error)

    return render_template('update_user.html', user=user)

