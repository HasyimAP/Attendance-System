from flask import Blueprint, render_template

studentAuth = Blueprint('studentAuth', __name__)

@studentAuth.route('/my-attendance')
def myAttendance():
    return render_template('myAttendance.html')

@studentAuth.route('/student-list1')
def studentList1():
    return render_template('studentList1.html')

@studentAuth.route('/teacher-list1')
def teacherList1():
    return render_template('teacherList1.html')