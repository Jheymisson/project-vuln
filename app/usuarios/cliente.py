from flask import Blueprint, render_template, session

bp = Blueprint('cliente', __name__)

@bp.route('/cliente')
def cliente_dashboard():
    if session.get('role') != 'cliente':
        return 'Acesso negado'
    return render_template('cliente.html')
