from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user ,logout_user
from .models import User
from . import db 
from .forms import RegistrationForm, LoginForm, PasswordUpdateForm, ApplyJobForm
import os 
from .app_bp import jobs 

candidate_bp = Blueprint('candidate',__name__)

@candidate_bp.route('/candidate')
@login_required
def candidate_index(): 
	if current_user.role != 'candidate':
		flash(f'You are not authorized to access this page','danger')
		logout_user()
		return redirect(url_for('app.login'))
	else:
		return render_template('candidate/index.html', name=current_user.name, title ='Candidate | Home')



@candidate_bp.route('/profile/')
@login_required
def profile():
	name = current_user.name
	return render_template('candidate/profile.html', name=name)

@candidate_bp.route('/settings')
@login_required
def settings():
	name = current_user.name
	return render_template('candidate/candidate-settings.html', name=name)

@candidate_bp.route('/my-jobs')
@login_required
def my_jobs_applied():
	return render_template('candidate/my-jobs-applied.html', name=current_user.name)

@candidate_bp.route('/cv')
@login_required
def my_cv():
	return render_template('candidate/my-cv.html',name=current_user.name)

@candidate_bp.route('/favorite-jobs')
@login_required
def my_jobs_favorite():
	return render_template('candidate/my-jobs-favorite.html', name=current_user.name)


@candidate_bp.route('/chat')
@login_required
def chat():
	return render_template('candidate/chat.html', name=current_user.name)

@candidate_bp.route('/tasks')
@login_required
def tasks():
	return render_template('candidate/tasks.html',name=current_user.name)

@candidate_bp.route('/apply', methods=['GET','POST'])
@login_required
def apply_job():
	form = ApplyJobForm()
	email = current_user.email 
	job_id = form.job_id.data 
	apply_date = form.apply_date.data 
	cv_upload= form.cv_upload.data 
	if form.validate_on_submit():
		if request.method == 'POST':
			print(email,job_id,apply_date,cv_upload)
	return render_template('candidate/apply.html',form=form, job=jobs ) 



