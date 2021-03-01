from flask import Blueprint, render_template
from flask_login import login_required, current_user 

admin_bp = Blueprint('admin',__name__)

@admin_bp.route('/admin')
@login_required
def admin_index():
	if current_user.role != 'admin':
		flash(f'You are not authorized to access this page','danger')
		logout_user()
		return redirect(url_for('app.login'))
	else:
		return render_template('admin/index.html', name=current_user.name, title='Admin| Dashboard')

