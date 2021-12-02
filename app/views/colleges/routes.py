from . import college
from flask import Flask, render_template, url_for, flash, request, redirect
from app import mysql



#********** College **********


@college.route("/colleges")
def colleges():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM colleges")
    data = cur.fetchall()
    cur.close()
    return render_template('colleges.html', colleges=data)

@college.route('/college',methods=['POST','GET'])
def colleg():
    code = request.form['code']
    college = request.form['college']
    cur = mysql.connection.cursor()
    check = [code]
    count = cur.execute('select * from colleges where college_code=%s', check)

    if not code or not college:
        flash("All fields required", "error")
        return redirect(url_for('colleges'))

    if count == 0:
        if request.method == "POST":
            flash("Data Successfully Added", "success")
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO colleges (college_code, college) VALUES (%s, %s)", (code, college))
            mysql.connection.commit()
            return redirect(url_for('college.colleges'))
    else:
        flash("College Already Exist", "error")
        return redirect(url_for('college.colleges'))

@college.route('/delete_college/<string:collegeid>', methods = ['POST', 'GET'])
def delete_college(collegeid):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM colleges WHERE collegeid=%s", (collegeid,))
    mysql.connection.commit()
    flash("Record Has Been Deleted Successfully", "success")
    return redirect(url_for('college.colleges'))

@college.route('/update_college',methods=['POST','GET'])
def update_college():
    college_id = request.form['id']
    code = request.form['code']
    college = request.form['college']
    cur = mysql.connection.cursor()
    check = [code]
    count = cur.execute('select * from colleges where college_code=%s', check)

    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE colleges
            SET college_code=%s, college=%s
            WHERE collegeid=%s
            """, (code, college, college_id))
        mysql.connection.commit()
        flash("Data Updated Successfully", "success")
        return redirect(url_for('college.colleges'))

@college.route('/searchcollege', methods=['GET', 'POST'])
def searchcollege():
    field = request.form.get('college')
    user_input = request.form['searchInput']
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM colleges")
    colleges = cur.fetchall()
    keyword = user_input.upper()
    result = []
    
    if field == 'college':
        for college in colleges:    
            college_allcaps = [str(info).upper() for info in college]
            if keyword in college_allcaps[2]:
                result.append(college)
            result
    else:
        for college in colleges:    
            college_allcaps = [str(info).upper() for info in college]
            if keyword in college_allcaps[1]:
                result.append(college)
            result

    if not user_input or not field:
            flash("Please Input Search Data", "error")


    if len(result) !=0:
        return render_template('colleges.html', colleges=result)
    else:
        return redirect(url_for('college.colleges'))