from flask import Blueprint, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, EmailField, PasswordField
from wtforms.validators import DataRequired
from .models import *
from . import db
from flask_login import login_required, current_user

adminAuth = Blueprint('adminAuth', __name__)

@adminAuth.route('/add-student', methods=['GET', 'POST'])
@login_required
def addStudent():
    student_id = None
    name = None
    batch = None
    semester = None
    email = None
    password = None
    form = StudentForm()
    
    if form.validate_on_submit():
        user = Users.query.filter_by(email = form.email.data, role = 'student').first()
        if user is None:
            user = Users(user_id = form.student_id.data,
                            name = form.name.data,
                            batch = form.batch.data,
                            semester = form.semester.data,
                            email = form.email.data,
                            password = form.password.data,
                            role = 'student')
            db.session.add(user)
            db.session.commit()
            flash("Form Submitted Successfully", 'success')
            
            student_id = form.student_id.data
            form.student_id.data = None
            
            name = form.name.data
            form.name.data = None
            
            batch = form.batch.data
            form.batch.data = None
            
            semester = form.semester.data
            form.semester.data = None
            
            email = form.email.data
            form.email.data = None
            
            password = form.password.data
            form.password.data = None
        
        else:
            flash("Student already exist!", 'primary')
    
    role = current_user.role
    if role == 'teacher':
        flash('Login as admin to access this page', 'primary')
        return redirect(url_for('teacherAuth.studentAttendance'))
    elif role == 'student':
        flash('Login as admin to access this page', 'primary')
        return redirect(url_for('studentAuth.myAttendance'))
    else:
        return render_template('addStudent.html',
                            student_id = student_id,
                            name = name,
                            batch = batch,
                            semester = semester,
                            email = email,
                            password = password,
                            form = form)

@adminAuth.route('/add-teacher', methods=['GET', 'POST'])
@login_required
def addTeacher():
    teacher_id = None
    name = None
    email = None
    password = None
    form = TeacherForm()
    
    if form.validate_on_submit():
        user = Users.query.filter_by(email = form.email.data, role = 'teacher').first()
        if user is None:
            user = Users(user_id = form.teacher_id.data,
                            name = form.name.data,
                            email = form.email.data,
                            password = form.password.data,
                            role = 'teacher')
            db.session.add(user)
            db.session.commit()
            flash("Form Submitted Successfully", 'success')
            
            teacher_id = form.teacher_id.data
            form.teacher_id.data = None
            
            name = form.name.data
            form.name.data = ''
            
            email = form.email.data
            form.email.data = None
            
            password = form.password.data
            form.password.data = None
        
        else:
            flash("Teacher already exist!", 'primary')
    
    role = current_user.role
    if role == 'teacher':
        flash('Login as admin to access this page', 'primary')
        return redirect(url_for('teacherAuth.studentAttendance'))
    elif role == 'student':
        flash('Login as admin to access this page', 'primary')
        return redirect(url_for('studentAuth.myAttendance'))
    else:  
        return render_template('addTeacher.html',
                            teacher_id = teacher_id,
                            name = name,
                            email = email,
                            password = password,
                            form = form)

@adminAuth.route('/add-admin', methods=['GET', 'POST'])
@login_required
def addAdmin():
    admin_id = None
    email = None
    password = None
    form = AdminForm()
    
    if form.validate_on_submit():
        user = Users.query.filter_by(role = 'admin', email = form.email.data).first()
        if user is None:
            user = Users(user_id = form.admin_id.data,
                          email = form.email.data,
                          password = form.password.data,
                          role = 'admin')
            db.session.add(user)
            db.session.commit()
            flash("Form Submitted Successfully", 'success')
            
            admin_id = form.admin_id.data
            form.admin_id.data = None
            
            email = form.email.data
            form.email.data = None
            
            password = form.password.data
            form.password.data = None
            
        else:
            flash("Admin already exist!", 'primary')
    
    role = current_user.role
    if role == 'teacher':
        flash('Login as admin to access this page', 'primary')
        return redirect(url_for('teacherAuth.studentAttendance'))
    elif role == 'student':
        flash('Login as admin to access this page', 'primary')
        return redirect(url_for('studentAuth.myAttendance'))
    else:  
        return render_template('addAdmin.html',
                            admin_id = admin_id,
                            email = email,
                            password = password,
                            form = form)

@adminAuth.route('/student-list3')
@login_required
def studentList3():
    users = Users.query.order_by(Users.user_id).filter_by(role = 'student')
    role = current_user.role
    if role == 'teacher':
        flash('Login as admin to access this page', 'primary')
        return redirect(url_for('teacherAuth.studentAttendance'))
    elif role == 'student':
        flash('Login as admin to access this page', 'primary')
        return redirect(url_for('studentAuth.myAttendance'))
    else:
        return render_template('studentList3.html', 
                            users = users)

@adminAuth.route('/teacher-list2')
@login_required
def teacherList2():
    users = Users.query.order_by(Users.user_id).filter_by(role = 'teacher')
    role = current_user.role
    if role == 'teacher':
        flash('Login as admin to access this page', 'primary')
        return redirect(url_for('teacherAuth.studentAttendance'))
    elif role == 'student':
        flash('Login as admin to access this page', 'primary')
        return redirect(url_for('studentAuth.myAttendance'))
    else:
        return render_template('teacherList2.html',
                            users = users)
    
@adminAuth.route('/admin-list')
@login_required
def adminList():
    users = Users.query.order_by(Users.user_id).filter_by(role = 'admin')
    role = current_user.role
    if role == 'teacher':
        flash('Login as admin to access this page', 'primary')
        return redirect(url_for('teacherAuth.studentAttendance'))
    elif role == 'student':
        flash('Login as admin to access this page', 'primary')
        return redirect(url_for('studentAuth.myAttendance'))
    else:
        return render_template('adminList.html',
                            users = users)

@adminAuth.route('/delete-student/<int:db_id>')
@login_required
def delStudent(db_id):
    user = Users.query.get(db_id)
    user_id = user.user_id
    
    db.session.delete(user)
    db.session.commit()
    
    date_data = Attendances.query.filter_by(student_id = user_id).all()
    if date_data:
        for x in date_data:
            del_date = Attendances.query.get(x.att_id)
            db.session.delete(del_date)
            db.session.commit()
    
    flash('Student Deleted Successfully!', 'success')
    
    return redirect(url_for('adminAuth.studentList3'))

@adminAuth.route('/delete-teacher/<int:user_id>')
@login_required
def delTeacher(user_id):
    user = Users.query.get(user_id)
    
    db.session.delete(user)
    db.session.commit()
    flash('Teacher Deleted Successfully!', 'success')
    
    return redirect(url_for('adminAuth.teacherList2'))

@adminAuth.route('/delete-admin/<int:user_id>')
@login_required
def delAdmin(user_id):
    user = Users.query.get(user_id)
    
    db.session.delete(user)
    db.session.commit()
    flash('Admin Deleted Successfully!', 'success')
    
    return redirect(url_for('adminAuth.adminList'))


class StudentForm(FlaskForm):
    student_id = StringField('Student ID', validators=[DataRequired()])
    name = StringField('Student Full Name', validators=[DataRequired()])
    batch = IntegerField('Batch Year (ex. 2019)', validators=[DataRequired()])
    semester = IntegerField('Current Semester', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class TeacherForm(FlaskForm):
    teacher_id = StringField('Teacher ID', validators=[DataRequired()])
    name = StringField('Teacher Full Name', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    role = 'Teacher'
    submit = SubmitField('Submit')
    
class AdminForm(FlaskForm):
    admin_id = StringField('Admin ID', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    role = 'Admin'
    submit = SubmitField('Submit')