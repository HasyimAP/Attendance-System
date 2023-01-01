from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, EmailField, RadioField, DateTimeField, Form, FormField, FieldList
from wtforms.validators import DataRequired
from .models import *
from . import db
from flask_login import login_required, current_user

teacherAuth = Blueprint('teacherAuth', __name__)

@teacherAuth.route('/student-attendance', methods=['GET', 'POST'])
@login_required
def studentAttendance():
    students = Users.query.order_by(Users.user_id).filter_by(role = 'student')
    
    if request.method == 'POST':
        date = request.form.get('date')
        exist_date = Attendances.query.filter_by(date = date).all()
        
        if exist_date:
            for x in exist_date:
                delete_date = Attendances.query.get(x.att_id)
                db.session.delete(delete_date)
                db.session.commit()
        
        for student in students:
            if (request.form.get(student.email) != None):
                data = Attendances(student_id = student.user_id,
                                   name = student.name,
                                   batch = student.batch,
                                   semester = student.semester,
                                   email = student.email,date = date,
                                   status = request.form.get(student.email)
                                   )
                
                db.session.add(data)
                db.session.commit()
        
        flash("Form Submitted Successfully", 'success')
    
    role = current_user.role
    if role == 'student':
        flash('Login as teacher to access this page', 'primary')
        return redirect(url_for('studentAuth.myAttendance'))
    elif role == 'admin':
        flash('Login as teacher to access this page', 'primary')
        return redirect(url_for('adminAuth.addStudent'))
    else:    
        return render_template('studentAttendance.html',
                               students = students)

@teacherAuth.route('/student-list2')
@login_required
def studentList2():
    users = Users.query.order_by(Users.user_id).filter_by(role = 'student')
    role = current_user.role
    if role == 'student':
        flash('Login as teacher to access this page', 'primary')
        return redirect(url_for('studentAuth.myAttendance'))
    elif role == 'admin':
        flash('Login as teacher to access this page', 'primary')
        return redirect(url_for('adminAuth.addStudent'))
    else: 
        return render_template('studentList2.html',
                               users = users)
