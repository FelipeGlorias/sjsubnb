from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)  

    
    from app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    from app.main.routes import main_bp
    app.register_blueprint(main_bp)

    return app

