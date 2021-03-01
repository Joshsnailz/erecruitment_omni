from flask import Blueprint, render_template, flash , redirect, url_for
from flask_login import login_required, current_user, logout_user
from .models import User
from . import db 
from .forms import RegistrationForm, LoginForm, PasswordUpdateForm

hr_bp = Blueprint('hr_bp', __name__)

@hr_bp.route('/hr')
@login_required
def index_hr():
	if current_user.role != 'hr':
		flash(f'You are not authorized to access this page','danger')
		logout_user()
		return redirect(url_for('app.login'))
	else: 
		return render_template('hr/index.html', title="Human Resource Admin", name=current_user.name)

@hr_bp.route('/applicant')
@login_required
def applicant():
	users = User.query.all()
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
	return render_template('common/pages-chat.html', name=current_user.name, title="Omnicontact|Chat")


@hr_bp.route('/hr-settings', methods=['GET','POST'])
@login_required
def settings_hr():
	form = PasswordUpdateForm()
	x = str.split(current_user.name)
	first_name = x[0]
	last_name = x[1]
	return render_template('hr/pages-settings.html', name=current_user.name, title="Omnicontact| Settings", first_name=first_name, last_name=last_name, form=form)

@hr_bp.route('/add_job')
@login_required
def add_job():
	return render_template('hr/add_job.html', name=current_user.name, title="Omnicontact| Add Job")

	



