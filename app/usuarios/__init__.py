from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'

    with app.app_context():
        from . import database
        database.init_db()

        from . import views
        app.register_blueprint(views.bp)

        from . import autenticacao
        app.register_blueprint(auth.bp)

        from app.usuarios import admin
        app.register_blueprint(admin.bp)

        from . import vendedor
        app.register_blueprint(vendedor.bp)

        from . import cliente
        app.register_blueprint(cliente.bp)

    return app
