import sqlite3 


def connect_db(app):
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db(app):
    conn=connect_db(app)
    with app.open_resource("db.sql",mode="r")as file:
        conn.cursor().executescript(file.read())
        conn.commit()
    conn.close()

def get_db(g,app):
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db(app)
    return g.link_db
