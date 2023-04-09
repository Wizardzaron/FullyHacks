import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, abort, current_app

app = Flask(__name__, static_folder = 'images')

@app.route('/')
@app.route('/blog', methods =['GET'])

def link():
    conn = sqlite3.connect('Point.db')

    cur = conn.cursor()

    get_data = '''SELECT info FROM evidence'''

    cur.execute(get_data)
    retrieve_data = cur.fetchall()

    #file_path = '/Desktop/FullyHacks'
    image_files = ["/images/image1.jpg", "/images/image2.jpg", "/images/image3.jpg"]
    return render_template('welcome.html', retrieve_data = retrieve_data, image_files = image_files)


if __name__ =="__main__":
    app.run()