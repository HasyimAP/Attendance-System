from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'CloudComputingSAOTeam1'

    from .views import views
    from .studentAuth import studentAuth
    from .teacherAuth import teacherAuth
    from .adminAuth import adminAuth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(studentAuth, url_prefix='/')
    app.register_blueprint(teacherAuth, url_prefix='/')
    app.register_blueprint(adminAuth, url_prefix='/')

    return app
