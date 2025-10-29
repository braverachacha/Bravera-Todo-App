from flask import Blueprint, render_template
from flask_login import current_user, login_required


views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
  return render_template('index.html')
  
@views.route('/about')
def about():
  return render_template('about.html')