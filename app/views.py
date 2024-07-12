from flask import Blueprint, render_template, request, redirect, url_for, session
import sqlite3

bp = Blueprint('views', __name__)

@bp.route('/')
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM produtos')
    produtos = c.fetchall()
    conn.close()
    print("Rendering index.html with products:", produtos)
    return render_template('index.html', produtos=produtos)

@bp.route('/compra/<int:produto_id>', methods=['GET', 'POST'])
def compra(produto_id):
    if 'username' not in session:
        return redirect(url_for('auth.login', next=url_for('views.compra', produto_id=produto_id)))

    if request.method == 'POST':
        quantidade = request.form['quantidade']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('SELECT * FROM produtos WHERE id = ?', (produto_id,))
        produto = c.fetchone()
        if produto:
            c.execute('INSERT INTO pedidos (cliente, produto, preco) VALUES (?, ?, ?)',
                      (session['username'], produto[1], produto[3]))
            conn.commit()
        conn.close()
        return redirect(url_for('views.compra_sucesso'))

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM produtos WHERE id = ?', (produto_id,))
    produto = c.fetchone()
    conn.close()

    if not produto:
        return 'Produto não encontrado', 404

    return render_template('compra.html', produto=produto)

@bp.route('/compra_sucesso')
def compra_sucesso():
    return render_template('compra_sucesso.html')
