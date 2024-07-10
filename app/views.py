from flask import Blueprint, render_template
import sqlite3

bp = Blueprint('views', __name__)

@bp.route('/')
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT nome, descricao, preco, imagem FROM produtos')
    produtos = c.fetchall()
    conn.close()
    return render_template('index.html', produtos=produtos)
