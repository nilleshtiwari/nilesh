from flask import Blueprint
from flask import flash
from flask import g,session
from flask import redirect
from flask import render_template, current_app
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from flaskApp.auth import login_required, admin_required
from flaskApp.db import get_db
from flask_paginate import Pagination, get_page_parameter
import requests
import json
import uuid
import time


bp = Blueprint("engine", __name__,)  # craeting the blueprint and naming it as engine

@bp.route('/home', methods=['GET'])
def home():
    return render_template('employee/home.html')


@bp.route('/', methods=('POST', 'GET'))
@bp.route('/employee',methods=("GET", "POST"))
@login_required
def index():
    """ The function index is resonsible for getting all the employee details from the database 
        shows in one the webpage """
    session["ctx"] = {'empId':session.get('user_id')}
    current_app.logger.info("A user visited the home page >>> %s", session["ctx"])
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)

    Employee = get_db().execute(
        "select * from  employee order by employee.id desc ",
    ).fetchall() #return a list of sqlit.Row objects which can be queried later

    pagination = Pagination(page=page, total=len(Employee), search=search, record_name='employee')

    if request.method == 'POST':
        error = None
        employee_email_to_update = request.form.get('employee-name')
        employee_email_to_delete = request.form.get('employee-delete')
        if employee_email_to_update:
            return redirect(url_for('engine.update', email_address=employee_email_to_update))
        elif employee_email_to_delete:
            return redirect(url_for('engine.delete',email_address=employee_email_to_delete))
        else:
            error = 'Something went wrong'
            flash(error)
            return render_template('employee/employee.html',employee=Employee,pagination=pagination,)

    if request.method=='GET':
        return render_template('employee/employee.html',employee=Employee,pagination=pagination,)




@bp.route('/employee/detail/<id>', methods=('POST', 'GET'))
@login_required
@admin_required
def employee_details(id):
    """ This function will give the details of single employee who is currently logged in """
    db = get_db()
    Employee =  db.execute(
            "SELECT * FROM employee WHERE employee.id = ?", (id,)
        ).fetchone()
    return render_template('employee/employee_detail.html', employee=Employee)

@bp.route('/employee/profile',methods=['GET','POST'])
@login_required
def profile():
    Employee = g.user
    return render_template('employee/details.html', employee=Employee)

@bp.route('/employee/update/<email_address>', methods=('POST','GET'))
@login_required
@admin_required
def update(email_address):
    """This function update a single employee details corresponding to its email id."""

    if request.method == "POST":
        error = None
        first_name = request.form["FirstName"]
        last_name  = request.form['LastName']
        email_address = request.form['email_address']
        date_of_birth = request.form['DOB']
        phone_number = request.form['PhoneNumber']
        address = request.form['address']
        role = request.form['employee-role']
        print(f'role={role}')
        print(f'address={address}')
        if not first_name:
            error = "First Name is required."
        elif not last_name:
            error = "Last Name is required"
        elif not date_of_birth:
            error = 'date of birth is required'
        elif not email_address:
            error = 'email address is required'
        elif not phone_number:
            error = "Phone number is required"
        elif not role:
            error = 'role is required'

        
        
        if error is None:
            db = get_db()
            db.execute(
                "UPDATE employee SET FirstName=?,LastName=?,email_address=?,dateofbirth=?,address=?,employee_role=?,phonenumber=? where email_address=?",(first_name,last_name,email_address,date_of_birth,address,role,phone_number,email_address,),
            )
            db.commit()
            data = request.form.to_dict(flat=True)
            update_api_db_data(data)
            message = "Details Saved Successfully"
            current_app.logger.info(f"A user updated the employee details >>> {session['ctx']}")
            if g.user['email_address'] == email_address and role.lower() != 'admin':
                message = 'Your admin status changed successfully logging you out from the current session'
                flash(message, category='danger')
                return redirect(url_for('auth.logout'))
        flash(message, category='success')

        return redirect(url_for('engine.index'))

    if request.method=='GET':  # To avoid confirmation on refreshing of the web page
        db = get_db()

        employee_object = db.execute(
            "SELECT * FROM employee WHERE employee.email_address = ?", (email_address,)).fetchone()

        return render_template('employee/update.html', employee=employee_object)


@bp.route('/employee/delete/<email_address>', methods=['GET', 'POST'])
@login_required
@admin_required
def delete(email_address):
    """ Takin the email address as an argument, delete it corresponding employee from the database"""

    if g.user['email_address'] == email_address:
        error = 'You cannot delete yourself from the database'
        flash(error,category='danger')
        return redirect(url_for('engine.index'))
    
    db = get_db()
    
    try:
        db.execute(
            "DELETE FROM employee WHERE employee.email_address = ?", (email_address,))
        db.commit()
        data = {'email_address':email_address}
        delete_api_db_data(data)
    except:
        message = 'Something Went Wrong!'  # if commit falis error message will popup
        flash(message,category='danger')
        return redirect(url_for('engine.index'))
    else:
        current_app.logger.warning(
        f"A user deleted the employee whose email address was {email_address} >>>{session['ctx']}"
    )
        message = f'Employee with email address {email_address} deleted successfully'
        flash(message, category='danger')
        return redirect(url_for('engine.index'))




@bp.route('/search', methods=['POST'])
@login_required
@admin_required
def search():
    if request.method == 'POST':
        Searched = request.form.get('searched')
        employee_email_to_delete = request.form.get('employee-delete')

        if employee_email_to_delete:
            return redirect(url_for('engine.delete',email_address=employee_email_to_delete))

        
        db = get_db()  # connecting with the database
        search = False
        q = request.args.get('q')
        if q:
            search = True

        page = request.args.get(get_page_parameter(), type=int, default=1)

        data_from_api = fetch_data_from_api(Searched)
        
        pagination = Pagination(page=page, total=len(data_from_api), search=search, record_name='Employee')

        current_app.logger.info(
        "A user performed a search. | query: %s >>> %s", Searched, session["ctx"]
    )


    return render_template('employee/search.html',employee_matched_result=data_from_api,searched=Searched,pagination=pagination,)


    
def fetch_data_from_api(url_data):
    data = requests.get("http://127.0.0.1:5001/"+url_data,proxies={"http": "http://api:5001/"}, verify=False)
    return data.json()

def update_api_db_data(data):
    response = requests.post("http://127.0.0.1:5001/update",proxies={"http": "http://api:5001/update"}, verify=False,json=data)
    print(response.text)




def delete_api_db_data(data):
    response = requests.post("http://127.0.0.1:5001/delete",proxies={"http": "http://api:5001/delete"}, verify=False,json=data)
    print(response.text)
