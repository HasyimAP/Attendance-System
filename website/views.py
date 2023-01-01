from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, RadioField, SubmitField
from wtforms.validators import DataRequired
from .models import *
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    role = ''
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if request.form.get('optionsRole') != None:
            role = request.form.get('optionsRole')
            
        if role == 'student':
            user = Users.query.filter_by(email=email, role = 'student').first()
            
            if user:
                if user.password == password:
                    flash('Logged in Successfully!', 'success')
                    login_user(user, remember=True)
                    return redirect(url_for('studentAuth.myAttendance'))
                else:
                    flash('Incorrect Password!', 'primary')
            else:
                flash('Email Does Not Exist!', 'primary')
                
        elif role == 'teacher':
            user = Users.query.filter_by(email=email, role = 'teacher').first()
            
            if user:
                if user.password == password:
                    flash('Logged in Successfully!', 'success')
                    login_user(user, remember=True)
                    return redirect(url_for('teacherAuth.studentAttendance'))
                else:
                    flash('Incorrect Password!', 'primary')
            else:
                flash('Email Does Not Exist!', 'primary')
                
        elif role == 'admin':
            user = Users.query.filter_by(email=email, role = 'admin').first()
            
            if user:
                if user.password == password:
                    flash('Logged in Successfully!', 'success')
                    login_user(user, remember=True) 
                    return redirect(url_for('adminAuth.addStudent'))
                else:
                    flash('Incorrect Password!', 'primary')
            else:
                flash('Email Does Not Exist!', 'primary')
    
    return render_template("login.html")
    
@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))
