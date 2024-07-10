from flask import Blueprint, render_template, session

bp = Blueprint('vendedor', __name__)

@bp.route('/vendedor')
def vendedor_dashboard():
    if session.get('role') != 'vendedor':
        return 'Acesso negado'
    return render_template('vendedor.html')
