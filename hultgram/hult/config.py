import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    
    SECRET_KEY = os.environ.get("SECRET_KEY") or "supersecretkey"
    
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"
    
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
    
    
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
