from . import student
from flask import render_template, url_for, flash, request, redirect
from app import mysql
import os
import random
from cloudinary.uploader import upload, destroy
from app.views.students.forms import Uploader

#********** Student **********

@student.route("/", methods = ['POST', 'GET'])
def home():
    form = Uploader()
    if request.method == "POST":
        id = request.form['id']
        Firstname = request.form['first']
        Lastname = request.form['last']
        image = form.profile.data
        Course = request.form.get('course', False)
        Level = request.form.get('year', False)
        Gender = request.form.get('gender', False)
        cur = mysql.connection.cursor() 
        check = [id]
        count = cur.execute('select * from student where id=%s', check)

        if not id or not Firstname or not Lastname or not Course or not Level or not Gender:
            flash("All fields required", "error")
            return redirect(url_for('student.home'))
        
        if count == 0:
            if image:
                result = upload(image.read(),public_id='student/{}'.format(id))
                url = result.get('url')
                flash("Data Successfully Added", "success")
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO student (id, Firstname, Lastname, Course, Level, Gender, img_url) VALUES (%s, %s, %s, %s, %s, %s, %s)", (id, Firstname, Lastname, Course, Level, Gender, url ))
                mysql.connection.commit()
                return redirect(url_for('student.home'))
            else:
                flash("Please Select a File", "error")
        else:
            flash("Student ID Already Exist", "error")
            return redirect(url_for('student.home'))
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT  * FROM colleges")
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM student")
    cure = mysql.connection.cursor()
    cure.execute("SELECT  * FROM courses")
    data = cur.fetchall()
    course= cure.fetchall()
    college= cursor.fetchall()
    cur.close()

    return render_template('index.html', students=data, cor = course, form = form, college=college)

@student.route('/update_student',methods=['POST','GET'])
def update_student():
    form = Uploader()
    ran = random.randint(0,10)
    id = request.form['id']
    if request.method == 'POST':
        image = form.profile.data
        if image:
            result = upload(image.read(),public_id='student/{}'.format(id+ str(ran)))
            url = result.get('url')
            student_id = request.form['studid']
            stud_id = request.form['id']
            Firstname = request.form['first']
            Lastname = request.form['last']
            Course = request.form.get('course', False)
            Level = request.form.get('year', False)
            Gender = request.form.get('gender', False)
            cur = mysql.connection.cursor()
            cur.execute("""
                UPDATE student
                SET id=%s, Firstname=%s, Lastname=%s, Course=%s, Level=%s,Gender=%s, img_url=%s
                WHERE studid=%s
                """, (stud_id, Firstname, Lastname, Course, Level, Gender, url, student_id))
            flash("Data Updated Successfully" , "success")
            mysql.connection.commit()
            return redirect(url_for('student.home'))
        else:
            student_id = request.form['studid']
            stud_id = request.form['id']
            Firstname = request.form['first']
            Lastname = request.form['last']
            Course = request.form.get('course', False)
            Level = request.form.get('year', False)
            Gender = request.form.get('gender', False)
            cur = mysql.connection.cursor()
            cur.execute("""
                UPDATE student
                SET id=%s, Firstname=%s, Lastname=%s, Course=%s, Level=%s,Gender=%s
                WHERE studid=%s
                """, (stud_id, Firstname, Lastname, Course, Level, Gender, student_id))
            flash("Data Updated Successfully" , "success")
            mysql.connection.commit()
            return redirect(url_for('student.home'))

@student.route('/delete_stud/<string:id>', methods = ['POST', 'GET'])
def delete_stud(id):
    destroy(public_id="student/{}".format(id))
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM student WHERE id=%s", (id,))
    mysql.connection.commit()
    flash("Record Has Been Deleted Successfully", "success")
    return redirect(url_for('student.home'))

@student.route('/searchstudent', methods=['GET', 'POST'])
def searchstudent():
    form = Uploader()
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
        return render_template('index.html', students=result, form = form)
    else:
        return redirect(url_for('student.home'))
