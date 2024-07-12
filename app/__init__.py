from flask import Flask
import os

def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
    app.secret_key = 'sup3rs3cr3tk3y'

    from .database import init_db
    with app.app_context():
        init_db()

    from app import admin
    app.register_blueprint(admin.bp, url_prefix='/admin')

    from app import vendedor
    app.register_blueprint(vendedor.bp, url_prefix='/vendedor')

    from app import cliente
    app.register_blueprint(cliente.bp, url_prefix='/cliente')

    from app import autenticacao
    app.register_blueprint(autenticacao.bp, url_prefix='/auth')

    from app.views import bp as views_bp
    app.register_blueprint(views_bp)

    from app import compra
    app.register_blueprint(compra.bp, url_prefix='/compra')

    return app
