from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#defining the database
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'JNFDVBJK UIJGOKGN'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)    #initailize the app



    #def the blueprints 
    from .views import views
    from .auth  import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #ensure that the database has been created
    from .models import User, Note

    with app.app_context():
        create_database(app)

    login_manager = LoginManager()
    #where flask will direct us if we are not logged in
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #it looks for primary key by default

    return app

#checking if the database exist so we  do not overwritte it
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all()# tell flask which app db are we creating for
        print('Create Database!')