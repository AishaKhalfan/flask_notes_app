from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'aishakkk94'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    # app.register_blueprint(auth, url_prefix='/auth')
    # with the above we accesss it as 127.0.0.1:500/auth/
    app.register_blueprint(auth, url_prefix='/')

    return app
