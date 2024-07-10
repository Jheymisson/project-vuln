from flask import Blueprint, render_template, session
import sqlite3

bp = Blueprint('cliente', __name__)

@bp.route('/cliente')
def cliente_dashboard():
    if session.get('role') != 'cliente':
        return 'Acesso negado'

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM produtos')
    pedidos = c.fetchall()
    conn.close()

    return render_template('cliente.html', pedidos=pedidos)
