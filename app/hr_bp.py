from flask import Blueprint, render_template, flash , redirect, url_for, request
from flask_login import login_required, current_user, logout_user
from .models import User, Jobs, AppliedJobs
from . import db 
from .forms import RegistrationForm, LoginForm, PasswordUpdateForm, AddNewJobForm
from datetime import datetime 

hr_bp = Blueprint('hr_bp', __name__)

@hr_bp.route('/hr')
@login_required
def index_hr():
	if current_user.role != 'hr':
		flash(f'You are not authorized to access this page','danger')
		logout_user()
		return redirect(url_for('app.login'))
	else:
		jobs = Jobs.query.all() 
		candidates = User.query.filter_by(role="candidate").all()
		applied_jobs = AppliedJobs.query.all()
		openings = 0
		active_users = 0
		applied_jobs_count = 0
		for i in range(len(jobs)):
			openings = openings + 1 
		for i in range(len(candidates)):
			active_users = active_users+1
		for i in range(len(applied_jobs)):
			applied_jobs_count = applied_jobs_count+1
		return render_template('hr/index.html', title="Human Resource Admin", 
			name=current_user.name,jobs=jobs,candidates=candidates, 
			openings=openings,active_users=active_users,applied_jobs_count=applied_jobs_count)

@hr_bp.route('/applicant')
@login_required
def applicant():
	users = User.query.filter_by(role="candidate").all()
	return render_template('hr/pages-applicant.html', name=current_user.name, title="Omnicontact| Applicant", users=users)


@hr_bp.route('/view-cv')
@login_required
def view_cv():
	return render_template('common/pages-invoice.html', name=current_user.name, title="Omnicontact|View CV")

@hr_bp.route('/applications')
@login_required
def applications():
	return render_template('hr/pages-applications.html', name=current_user.name, title="Omnicontact| Applications")


@hr_bp.route('/hr-chat')
@login_required
def hr_chat():
	return render_template('hr/chat.html', name=current_user.name, title="Omnicontact|Chat")


@hr_bp.route('/hr-settings', methods=['GET','POST'])
@login_required
def settings_hr():
	form = PasswordUpdateForm()
	x = str.split(current_user.name)
	first_name = x[0]
	last_name = x[1]
	if request.method == "POST":
			old_password = form.current_password.data
			new_password = form.new_password.data
			print(old_password, new_password)
	return render_template('hr/pages-settings.html', name=current_user.name, title="Omnicontact| Settings", first_name=first_name, last_name=last_name, form=form)

@hr_bp.route('/add_job', methods=['POST','GET'])
@login_required
def add_job():
	form = AddNewJobForm()
	title = form.title.data
	description = form.description.data
	key_responsibilites = form.key_responsibilities.data
	qualifications = form.qualifications.data 
	due_date = form.due_date.data
	date_posted = datetime.now().strftime("%x")
	user_id = current_user.id

	if form.validate_on_submit():
		job = Jobs.query.filter_by(title=title).first()
		if not job:
			job = Jobs(title=title,description=description,key_responsibilities=key_responsibilites,qualifications=qualifications,due_date=due_date,date_posted=date_posted,user_id=user_id)
			db.session.add(job)
			db.session.commit()
			flash(f'The job listing has been successfully posted.','success')
			return redirect(url_for('hr_bp.index_hr'))
		print(title,description,key_responsibilites,due_date,date_posted,user_id)
	return render_template('hr/add_job.html', name=current_user.name, title="Omnicontact| Add Job", form=form)


@hr_bp.route('/previous-jobs')
@login_required
def previous_jobs():
	return "Previous Jobs come here"

@hr_bp.route('/candidate_cv_view')
def candidate_cv_view():
	return "View candidate cv"

	



