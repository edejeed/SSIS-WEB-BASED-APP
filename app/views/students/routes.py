from . import student
from flask import Flask, render_template, url_for, flash, request, redirect
from app import mysql

#********** Student **********

@student.route("/")
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM student")
    cure = mysql.connection.cursor()
    cure.execute("SELECT  * FROM courses")
    data = cur.fetchall()
    course= cure.fetchall()
    cur.close()

    return render_template('index.html', students=data, cor = course)

@student.route('/insert', methods = ['POST'])
def insert():
    id = request.form['id']
    Firstname = request.form['first']
    Lastname = request.form['last']
    Course = request.form['course']
    Level = request.form['year']
    Gender = request.form['gender']
    cur = mysql.connection.cursor()
    check = [id]
    count = cur.execute('select * from student where id=%s', check)

    if not id or not Firstname or not Lastname or not Course or not Level or not Gender:
        flash("All fields required", "error")
        return redirect(url_for('student.home'))

    if count == 0:
        if request.method == "POST":
            flash("Data Successfully Added", "success")
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO student (id, Firstname, Lastname, Course, Level, Gender) VALUES (%s, %s, %s, %s, %s, %s)", (id, Firstname, Lastname, Course, Level, Gender ))
            mysql.connection.commit()
            return redirect(url_for('student.home'))
    else:
        flash("Student ID Already Exist", "error")
        return redirect(url_for('student.home'))

@student.route('/update_student',methods=['POST','GET'])
def update_student():

    if request.method == 'POST':
        student_id = request.form['studid']
        stud_id = request.form['id']
        Firstname = request.form['first']
        Lastname = request.form['last']
        Course = request.form['course']
        Level = request.form['year']
        Gender = request.form['gender']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE student
               SET id=%s, Firstname=%s, Lastname=%s, Course=%s, Level=%s,Gender=%s
               WHERE studid=%s
            """, (stud_id, Firstname, Lastname, Course, Level, Gender, student_id))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('student.home'))

@student.route('/delete_stud/<string:studid>', methods = ['POST', 'GET'])
def delete_stud(studid):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM student WHERE studid=%s", (studid,))
    mysql.connection.commit()
    flash("Record Has Been Deleted Successfully", "success")
    return redirect(url_for('student.home'))

@student.route('/searchstudent', methods=['GET', 'POST'])
def searchstudent():
    field = request.form.get('student')
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM student ")
    students = cur.fetchall()
    user_input = request.form['searchInput']
    keyword = user_input.upper()
    result = []

    if field == '0':
        for student in students:    
            student_allcaps = [str(info).upper() for info in student]
            if keyword in student_allcaps[1]:
                result.append(student)
            result
    elif field == '1':
        for student in students:    
            student_allcaps = [str(info).upper() for info in student]
            if keyword in student_allcaps[2]:
                result.append(student)
            result
    elif field == '2':
        for student in students:    
            student_allcaps = [str(info).upper() for info in student]
            if keyword in student_allcaps[3]:
                result.append(student)
            result
    elif field == '3':
        for student in students:    
            student_allcaps = [str(info).upper() for info in student]
            if keyword in student_allcaps[4]:
                result.append(student)
            result
    if field == '4':
        for student in students:    
            student_allcaps = [str(info).upper() for info in student]
            if keyword in student_allcaps[5]:
                result.append(student)
            result
    if field == '5':
        for student in students:    
            student_allcaps = [str(info).upper() for info in student]
            if keyword in student_allcaps[6]:
                result.append(student)
            result
    
    if not user_input or not field:
        flash("Input All fields", "Error")

    if len(result) !=0:
        return render_template('index.html', students=result)
    else:
        return redirect(url_for('student.home'))
