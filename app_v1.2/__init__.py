from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__, template_folder ="./templates/")

    app.config['SECRET_KEY']= 'rtsu4g4hjkbg2chm3g2cj2rc3gh3vj2cgh23fhcj3hg3gc3'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///omnicontact.db'
    app.config['MAX_CONTENT_LENGTH'] = 3*1024*1024

    
    csrf.init_app(app)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'app.login'
    

    from .models import User 

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id)) 

    from .admin_bp import admin_bp as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from .candidate_bp import candidate_bp as candidate_blueprint
    app.register_blueprint(candidate_blueprint)

    from .hr_bp import hr_bp as hr_blueprint 
    app.register_blueprint(hr_blueprint)
    
    from .app_bp import app_bp as app_blueprint 
    app.register_blueprint(app_blueprint)


    return app 