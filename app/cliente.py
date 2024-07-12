from flask import Blueprint, render_template, session
import sqlite3

bp = Blueprint('cliente', __name__)

@bp.route('/cliente', methods=['GET'])
def cliente_dashboard():
    if session.get('role') != 'cliente':
        return 'Acesso negado'

    username = session.get('username')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM pedidos WHERE cliente = ?', (username,))
    pedidos = c.fetchall()
    conn.close()

    return render_template('cliente.html', pedidos=pedidos)
