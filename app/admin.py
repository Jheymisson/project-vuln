from flask import Blueprint, render_template, request, redirect, url_for, session
import sqlite3

bp = Blueprint('admin', __name__)

@bp.route('/admin', methods=['GET'])
def admin_dashboard():
    if session.get('role') != 'admin':
        return 'Acesso negado'

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    usuarios = c.fetchall()
    conn.close()

    return render_template('admin.html', usuarios=usuarios)

@bp.route('/admin/adicionar_usuario', methods=['POST'])
def adicionar_usuario():
    if session.get('role') != 'admin':
        return 'Acesso negado'

    username = request.form['username']
    password = request.form['password']
    role = request.form['role']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
    conn.commit()
    conn.close()

    return redirect(url_for('admin.admin_dashboard'))

@bp.route('/admin/remover_usuario/<int:user_id>', methods=['GET'])
def remover_usuario(user_id):
    if session.get('role') != 'admin':
        return 'Acesso negado'

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('admin.admin_dashboard'))
