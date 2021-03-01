from flask import Blueprint, render_template, flash, redirect, url_for, logging, request
from flask_login import login_required, current_user ,logout_user
from .models import User,AppliedJobs, Jobs
from . import db 
from .forms import RegistrationForm, LoginForm, PasswordUpdateForm, ApplyJobForm
import os 
from datetime import datetime, date

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
	jobs = AppliedJobs.query.filter_by(email=current_user.email)
	real_jobs = Jobs.query.all()
	if not jobs:
		flash(f'You have not applied for any jobs', 'danger')

	else:
		for job in jobs:
			pass
	return render_template('candidate/my-jobs-applied.html', name=current_user.name, jobs=jobs)

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

@candidate_bp.route('/apply/<job_id>', methods=['GET','POST'])
@candidate_bp.route('/apply')
@login_required
def apply_job(job_id):
	jobs = Jobs.query.all()
	form = ApplyJobForm()
	email = current_user.email 
	job_id = form.job_id.data 
	apply_date = datetime.now().strftime("%x")
	cv_upload= form.cv_upload.data 
	if request.method == 'POST':
		print(apply_date, cv_upload, job_id, email)
		applied_job = AppliedJobs(job_id=job_id, email=email, apply_date=apply_date)
		db.session.add(applied_job)
		db.session.commit()
		flash(f'Your application has been submitted successfully', 'success')
		return redirect(url_for('candidate.candidate_index'))
	return render_template('candidate/apply.html',form=form, job=jobs ) 



