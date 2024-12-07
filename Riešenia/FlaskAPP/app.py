from flask import Flask, render_template
import sqlite3

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


# pridaj_uzivatela("Ivan", 25)
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)


@app.route('/users/')
def get_users():
    uzivatelia = vylistuj_uzivatelov()
    return render_template('list.html', users=uzivatelia)


@app.route('/users/<id>')
def fetch_user(id):
    uzivatel = nacitaj_uzivatela(id)
    return render_template('detail.html', user=uzivatel)
