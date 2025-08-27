from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from uuid import uuid4

# Functions
con = sqlite3.connect("db.db", check_same_thread=False)
cur = con.cursor()

# cur.execute("CREATE TABLE user(id, name, age)")

def vylistuj_uzivatelov():
    result = cur.execute("SELECT * from user")
    return result.fetchall()

def nacitaj_uzivatela(user_id):
    result = cur.execute(f"SELECT * from user WHERE id = '{user_id}'")
    return result.fetchone()

def pridaj_uzivatela(name, age):
    my_id = uuid4()
    cur.execute(f"INSERT INTO user VALUES ('{my_id}','{name}',{age})")
    con.commit()

def aktualizacia_uzivatela(my_id, name, age):
    query = "UPDATE user SET name = ?, age = ? WHERE id = ?"
    cur.execute(query, (name, age, my_id))
    con.commit()

def zmaz_uzivatela(my_id):
    cur.execute(f"DELETE FROM user WHERE id ='{my_id}'")
    con.commit()


# pridaj_uzivatela("Marek", 27)
app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

@app.route("/")
@app.route('/users/')
def get_users():
    uzivatelia = vylistuj_uzivatelov()
    return render_template('list.html', users=uzivatelia)


@app.route('/users/<id>')
def fetch_user(id):
    uzivatel = nacitaj_uzivatela(id)
    return render_template('detail.html', user=uzivatel)

@app.route('/users/new', methods=("GET", "POST"))
def create_user():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        if name and age:
            pridaj_uzivatela(name, int(age))
            return redirect(url_for('get_users'))
        else:
            error = "Please provide both name and age."
            return render_template('create_user.html', error=error)

    return render_template('create_user.html')


@app.route('/users/<id>/update', methods=("GET", "POST"))
def update_user(id):
    user = nacitaj_uzivatela(id)
    if not user:
        return "User not found", 404

    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        if name and age:
            try:
                aktualizacia_uzivatela(id, name, int(age))
                return redirect(url_for('fetch_user', id=id))
            except Exception as e:
                error = f"Failed to update user: {e}"
                return render_template('update_user.html', user=user, error=error)
        else:
            error = "Please provide both name and age."
            return render_template('update_user.html', user=user, error=error)

    return render_template('update_user.html', user=user)

@app.route('/users/<id>/delete', methods=["POST"])
def delete_user(id):
    zmaz_uzivatela(id)
    return redirect(url_for('get_users'))
