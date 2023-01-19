from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = ''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
    db.init_app(app)

    from .views import views
    from .studentAuth import studentAuth
    from .teacherAuth import teacherAuth
    from .adminAuth import adminAuth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(studentAuth, url_prefix='/student')
    app.register_blueprint(teacherAuth, url_prefix='/teacher')
    app.register_blueprint(adminAuth, url_prefix='/admin')

    from .models import Attendances, Users

    if not path.exists('website/database.db'):
        with app.app_context():
            db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'views.home'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(db_id):
        return Users.query.get(db_id)

    return app
