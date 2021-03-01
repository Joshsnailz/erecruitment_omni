from flask import Blueprint, render_template , redirect, url_for, request, flash 
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import login_user, current_user, logout_user, login_required
from .models import User, Jobs
from . import db 
from .forms import RegistrationForm, LoginForm, PasswordUpdateForm

app_bp = Blueprint('app',__name__)



@app_bp.route('/')
def home():
    form = LoginForm()
    jobs = Jobs.query.all()
    return render_template('base/home.html', form=form, jobs=jobs, title="OmniContact| Login ")


@app_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('candidate.candidate_index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            if user.role == 'candidate':
                login_user(user, remember=form.remember.data)
                return redirect(url_for('candidate.candidate_index'))
            elif user.role == 'hr':
                login_user(user, remember=form.remember.data)
                return redirect(url_for('hr_bp.index_hr'))
            else:
                login_user(user, remember=form.remember.data)
                return redirect(url_for('admin.admin_index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('base/home.html', title='Login', form=form)



@app_bp.route('/signup', methods=['POST','GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('candidate.candidate_index'))
    form = RegistrationForm()
    if form.validate_on_submit():
    	password = form.password.data
    	user = User.query.filter_by(email=form.email.data).first()
    	if not user:
    		user = User(name=form.name.data, email=form.email.data, password=generate_password_hash(password, method='sha256'), role="candidate")
    		db.session.add(user)
    		db.session.commit()
    		flash('Your account has been created! You are now able to log in', 'success')
    		return redirect(url_for('app.login'))
    	else:
    		flash(f'Email acccount already in use, kindly login! or choose another', 'danger')
    		return redirect(url_for('app.login'))

    return render_template('base/signup.html', title='Sign up', form=form)

@app_bp.route('/reset-password')
def reset_pass():
	return render_template('common/pages-reset-password.html')


@app_bp.route('/calendar')
def calendar():
	return render_template('common/calendar.html')

@app_bp.route('/jobs')
def job():
    jobs = Jobs.query.all()
    return render_template('base/jobs.html', job=jobs, title="OmniContact| Jobs")

def requires_role(role):
    if current_user.role == role:
        pass
    else:
        flash(f'You are not authorized to access that page, Kindly log in with a different account', 'danger')
        return redirect(url_for('app.login'))

@app_bp.route('/password-change')
@login_required
def update_password():
    form = PasswordUpdateForm()
    if form.validate_on_submit():
        email = current_user.email
        new_password = form.password.data 
        if check_password_hash(current_user.password,new_password):
            flash(f'Your password has been updated successfully', 'success')



@app_bp.route('/logout')
@login_required
def logout():
	logout_user()
	flash(f'You have successfully logged out', 'success')
	return redirect(url_for('app.home'))