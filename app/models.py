from flask_login import UserMixin 
from datetime import datetime
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(100),unique=True,  nullable=False)
    image_file = db.Column(db.String(100), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20))

    def __repr__(self):
    	return f"User('{self.name}','{self.email}','{self.image_file}')"

    
    

class Jobs(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100),unique=True)
	description = db.Column(db.Text, nullable=False)
	key_responsibilities = db.Column(db.Text, nullable=False)
	qualifications = db.Column(db.Text, nullable=False)
	due_date = db.Column(db.String(100))
	date_posted = db.Column(db.String(100))
	user_id = db.Column(db.Integer,db.ForeignKey('hr_user.id'), nullable=False)

	def __repr__(self):
		return f"Jobs('{self.title}', '{self.date_posted}, '{self.due_date}')"



class Hr_user(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(1000), nullable=False)
	email = db.Column(db.String(100),unique=True, nullable=False)
	image_file = db.Column(db.String(100), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	jobs = db.relationship('Jobs',backref='author', lazy=True)

	def __repr__(self):
		return f"User('{self.name}','{self.email}','{self.image_file}')"


class Admin_user(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(1000), nullable=False)
	email = db.Column(db.String(100),unique=True, nullable=False)
	image_file = db.Column(db.String(100), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"User('{self.name}','{self.email}','{self.image_file}')"


class AppliedJobs(db.Model):
	job_id = db.Column(db.String, primary_key=True)
	email = db.Column(db.String, nullable=False)
	apply_date = db.Column(db.String, nullable=False)

	def __reper__(self):
		return f"AppliedJobs('{self.job_id}','{self.email}'.'{self.apply_date}')"


class JobsApplied(db.Model):
	job_id = db.Column(db.Integer, primary_key=True)
	candidate_id = db.Column(db.Integer,nullable=False)
	application_status = db.Column(db.String(20))
	comment = db.Column(db.String(100))


class AuditTrail(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.DateTime)
	time = db.Column(db.Time)
	activity = db.Column(db.String(400),nullable=False)


	

