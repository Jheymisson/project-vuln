from flask import Blueprint, render_template, request, redirect, url_for, session
import sqlite3

bp = Blueprint('vendedor', __name__)

@bp.route('/vendedor', methods=['GET'])
def vendedor_dashboard():
    if session.get('role') != 'vendedor':
        return 'Acesso negado'

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM produtos')
    produtos = c.fetchall()
    conn.close()

    return render_template('vendedor.html', produtos=produtos)

@bp.route('/vendedor/adicionar_produto', methods=['POST'])
def adicionar_produto():
    if session.get('role') != 'vendedor':
        return 'Acesso negado'

    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = request.form['preco']
    imagem = request.form['imagem']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO produtos (nome, descricao, preco, imagem) VALUES (?, ?, ?, ?)", (nome, descricao, preco, imagem))
    conn.commit()
    conn.close()

    return redirect(url_for('vendedor.vendedor_dashboard'))

@bp.route('/vendedor/remover_produto/<int:produto_id>', methods=['GET'])
def remover_produto(produto_id):
    if session.get('role') != 'vendedor':
        return 'Acesso negado'

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('vendedor.vendedor_dashboard'))
