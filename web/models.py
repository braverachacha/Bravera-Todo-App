from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import func

db = SQLAlchemy()

class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(150), nullable=False)
  note = db.Column(db.String(10000), nullable=False)
  date = db.Column(db.DateTime(timezone=True), default=func.now())
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
  id =db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(150), nullable=False)
  email = db.Column(db.String(100), nullable=False, unique=True)
  password = db.Column(db.String(200), nullable=False)
  notes = db.relationship('Note', lazy=True)
  
  def set_password(self, password):
    self.password = generate_password_hash(password)
    
  def check_password(self, password):
    return check_password_hash(self.password, password)
