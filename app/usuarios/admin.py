from flask import Blueprint, render_template, session

bp = Blueprint('admin', __name__)

@bp.route('/admin')
def admin_dashboard():
    if session.get('role') != 'admin':
        return 'Acesso negado'
    return render_template('admin.html')
