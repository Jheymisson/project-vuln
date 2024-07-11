from flask import Blueprint, render_template, request, redirect, url_for, session
import sqlite3

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    next_url = request.args.get('next')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['username'] = user[1]
            session['role'] = user[3]
            if next_url:
                return redirect(next_url)
            if user[3] == 'admin':
                return redirect(url_for('auth.admin_dashboard'))
            elif user[3] == 'vendedor':
                return redirect(url_for('auth.vendedor_dashboard'))
            elif user[3] == 'cliente':
                return redirect(url_for('auth.cliente_dashboard'))
        else:
            return 'Credenciais inválidas'
    return render_template('login.html', next=next_url)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

@bp.route('/admin_dashboard')
def admin_dashboard():
    if session.get('role') != 'admin':
        return 'Acesso negado'
    return render_template('admin_dashboard.html')

@bp.route('/vendedor_dashboard')
def vendedor_dashboard():
    if session.get('role') != 'vendedor':
        return 'Acesso negado'
    return render_template('vendedor_dashboard.html')

@bp.route('/cliente_dashboard')
def cliente_dashboard():
    if session.get('role') != 'cliente':
        return 'Acesso negado'
    return render_template('cliente_dashboard.html')
