from flask import Blueprint, render_template

teacherAuth = Blueprint('teacherAuth', __name__)

@teacherAuth.route('/student-attendance')
def studentAttendance():
    return render_template('studentAttendance.html')

@teacherAuth.route('/student-list2')
def studentList2():
    return render_template('studentList2.html')

