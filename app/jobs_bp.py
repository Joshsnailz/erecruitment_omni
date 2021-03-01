from flask import Blueprint, render_template , redirect, url_for, request, flash 
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import login_user, current_user, logout_user, login_required
from .models import User
from . import db 
from .forms import RegistrationForm, LoginForm, PasswordUpdateForm

jobs_bp = Blueprint('jobs_bp',__name__)



@jobs_bp.route('/jobs')
def index():
	return render_template('/jobs/index.html',jobs=jobs, title="OmniContact | Jobs")


