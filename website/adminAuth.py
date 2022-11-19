from flask import Blueprint, render_template

adminAuth = Blueprint('adminAuth', __name__)

@adminAuth.route('/add-student')
def addStudent():
    return render_template('addStudent.html')

@adminAuth.route('/add-teacher')
def addTeacher():
    return render_template('addTeacher.html')

@adminAuth.route('/student-list3')
def studentList3():
    return render_template('studentList3.html')

@adminAuth.route('/teacher-list2')
def teacherList2():
    return render_template('teacherList2.html')

