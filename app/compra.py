from flask import Blueprint, render_template, request, redirect, url_for, session
import sqlite3

bp = Blueprint('compra', __name__)

@bp.route('/compra/<int:produto_id>', methods=['GET', 'POST'])
def compra(produto_id):
    if not session.get('username'):
        return redirect(url_for('auth.login', next=url_for('compra.compra', produto_id=produto_id)))

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT nome, descricao, preco, imagem FROM produtos WHERE id = ?', (produto_id,))
    produto = c.fetchone()
    conn.close()

    if request.method == 'POST':
        return redirect(url_for('views.index'))

    return render_template('compra.html', produto=produto)
