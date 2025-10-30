from flask import Flask
from flask_login import LoginManager
from web.models import db, User
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'chacha bomsjdj jdo bravera254'

    database_url = os.getenv('DATABASE_URL', 'sqlite:///database.db')

    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://")

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)


    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app