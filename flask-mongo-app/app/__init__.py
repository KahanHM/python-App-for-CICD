from flask import Flask
from app.database import init_db

def create_app():
    app = Flask(__name__)
    init_db(app)
    
    from app.routes import user_bp
    app.register_blueprint(user_bp)
    
    return app
