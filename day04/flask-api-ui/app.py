#jaumendes
# https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application
# 14 09 2023 


import sqlite3
from flask import Flask, render_template

from flask import request, url_for, flash, redirect, abort
# ...
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

# ...

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')

        elif not content:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))


def inserter(linhas):
    conn = get_db_connection()
    conn.execute('SELECT * FROM posts')
    
   
    conn.executemany("INSERT INTO materials VALUES(?, ?, ?)", linhas)
    conn.commit()  # Remember to commit the transaction after executing INSERT.

    for row in conn.execute("SELECT year, title FROM materials ORDER BY year"):
        print(row)



import requests
from bs4 import BeautifulSoup

# jaumendes
# https://dev.to/code_jedi/scrape-news-headlines-with-python-1go6
 #[
 #   ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
 #   ("Monty Python's The Meaning of Life", 1983, 7.5),
 #   ("Monty Python's Life of Brian", 1979, 8.0),
  #  ]

url='https://www.bbc.com/news'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h3')
for x in headlines:
    if "BBC World" not in x.text.strip():
        print ( x.text.strip())
rows = [("jose mendes",1988,1)]

##


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
    inserter(rows)
