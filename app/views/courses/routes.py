from . import course
from flask import Flask, render_template, url_for, flash, request, redirect
from app import mysql


#********** Courses **********


@course.route("/courses")
def courses():
    cur = mysql.connection.cursor()
    cure = mysql.connection.cursor()
    cur.execute("SELECT  * FROM courses")
    cure.execute("SELECT  * FROM colleges")
    data = cur.fetchall()
    college = cure.fetchall()
    cur.close()

    return render_template('courses.html', courses=data, col =college)

@course.route('/course',methods=['POST','GET'])
def cours():
    code = request.form['code']
    course = request.form['course']
    college = request.form['college']
    cur = mysql.connection.cursor()
    check = [code]
    count = cur.execute('select * from courses where course_code=%s', check)

    if not code or not course or not college:
        flash("All fields required", "error")
        return redirect(url_for('course.courses'))

    if count == 0:
        if request.method == "POST":
            flash("Data Successfully Added", "success")
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO courses (course_code, course, college) VALUES (%s, %s, %s)", (code, course, college))
            mysql.connection.commit()
            return redirect(url_for('course.courses'))
    else:
        flash("Course Already Exist", "error")
        return redirect(url_for('course.courses'))

@course.route('/delete/<string:courseid>', methods = ['POST', 'GET'])
def delete(courseid):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM courses WHERE courseid=%s", (courseid,))
    mysql.connection.commit()
    flash("Record Has Been Deleted Successfully", "success")
    return redirect(url_for('course.courses'))

@course.route('/update_course',methods=['POST','GET'])
def update_course():

    if request.method == 'POST':
        course_id = request.form['id']
        code = request.form['code']
        course = request.form['course']
        college = request.form['college']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE courses
               SET course_code=%s, course=%s, college=%s
               WHERE courseid=%s
            """, (code, course, college, course_id))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('course.courses'))