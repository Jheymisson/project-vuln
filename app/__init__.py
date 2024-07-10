from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.secret_key = 'supersecretkey'

    with app.app_context():
        from . import database
        database.init_db()

        from . import views
        app.register_blueprint(views.bp)

        from . import autenticacao
        app.register_blueprint(autenticacao.bp, url_prefix='/auth')

        from .usuarios import admin
        app.register_blueprint(admin.bp)

        from .usuarios import vendedor
        app.register_blueprint(vendedor.bp)

        from .usuarios import cliente
        app.register_blueprint(cliente.bp)

        from . import compra
        app.register_blueprint(compra.bp)

    return app
