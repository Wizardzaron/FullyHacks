import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, abort, current_app

app = Flask(__name__)

@app.route('/')
@app.route('/blog', methods =['GET'])

def link():
    conn = sqlite3.connect('Point.db')

    cur = conn.cursor()

    get_data = '''SELECT info FROM evidence'''

    cur.execute(get_data)
    retrieve_data = cur.fetchall()
    return render_template('welcome.html', retrieve_data =retrieve_data)


if __name__ =="__main__":
    app.run()