from flask import Blueprint, render_template, flash, redirect, url_for
from .models import *
from flask_login import login_required, current_user

studentAuth = Blueprint('studentAuth', __name__)

@studentAuth.route('/my-attendance')
@login_required
def myAttendance():
    role = current_user.role
    name = current_user.name
    student_id = current_user.user_id
    
    if role == 'teacher':
        flash('Login as student to access this page', 'primary')
        return redirect(url_for('teacherAuth.studentAttendance'))
    elif role == 'admin':
        flash('Login as student to access this page', 'primary')
        return redirect(url_for('adminAuth.addStudent'))
    else:
        date_att = Attendances.query.order_by(Attendances.date).filter_by(student_id = current_user.user_id)
        return render_template('myAttendance.html',
                            date_att = date_att,
                            name = name,
                            student_id = student_id)

@studentAuth.route('/student-list1')
@login_required
def studentList1():
    role = current_user.role
    if role == 'teacher':
        flash('Login as student to access this page', 'primary')
        return redirect(url_for('teacherAuth.studentAttendance'))
    elif role == 'admin':
        flash('Login as student to access this page', 'primary')
        return redirect(url_for('adminAuth.addStudent'))
    else:
        users = Users.query.order_by(Users.user_id).filter_by(role = 'student')
        return render_template('studentList1.html',
                            users = users)

@studentAuth.route('/teacher-list1')
@login_required
def teacherList1():
    role = current_user.role
    if role == 'teacher':
        flash('Login as student to access this page', 'primary')
        return redirect(url_for('teacherAuth.studentAttendance'))
    elif role == 'admin':
        flash('Login as student to access this page', 'primary')
        return redirect(url_for('adminAuth.addStudent'))
    else:
        users = Users.query.order_by(Users.user_id).filter_by(role = 'teacher')
        return render_template('teacherList1.html', 
                            users = users)
    