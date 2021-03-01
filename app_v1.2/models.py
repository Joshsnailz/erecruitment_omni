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
	due_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
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
	applicant_email = db.Column(db.String, nullable=False)
	

	

