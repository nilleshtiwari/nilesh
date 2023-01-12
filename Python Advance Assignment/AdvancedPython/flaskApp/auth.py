import functools
import requests

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from werkzeug.exceptions import abort

from flaskApp.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")


from flask import session
from functools import wraps






def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None: # since g is a global object thats why we are able to use it here
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view

def admin_required(view):
    """View decorator that shows employee user an error message"""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session['role'] != 'admin': # since g is a global object thats why we are able to use it here
            abort(403,'Unauthorised Access')

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request #this code will execute before the request is being made.
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = (
            get_db().execute("SELECT * FROM employee WHERE id = ?", (user_id,)).fetchone()
        )




@bp.route("/register", methods=("GET", "POST"))
def register():
    """Register a new user.
    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if g.user is not None and session['role'] != 'admin':
        error = 'Unauthorised Access'
        abort(403, error)

    if request.method == "POST":
        first_name = request.form.get("FirstName")
        last_name  = request.form.get("LastName")
        password = request.form.get("password1")
        confirm_password = request.form.get("password2")
        email_address = request.form.get("email_address")
        date_of_birth = request.form.get("DOB")
        phone_number = request.form.get("PhoneNumber")
        address = request.form.get("address")
        
        db = get_db()
        error = None

        if not first_name:
            error = "First Name is required."
        elif not last_name:
            error = "Last Name is required"
        elif not date_of_birth:
            error = 'date of birth is required'
        elif not email_address:
            error = 'email address is required'
        elif not password:
            error = "Password is required."
        elif not confirm_password:
            error = "Confirm Password is required"
        elif not phone_number:
            error = "Phone number is required"
        elif password != confirm_password:
            error = "New password mismatch with confirm password"
        elif not check_password_validity(password):
            error = "Password length shoud be greater than 8 characters and contains atleast 1 uppercase,1 lowercase and 1 special character and 1 integer"



        if error is None:
            try:
                db.execute(
                    "INSERT INTO employee (FirstName,LastName,email_address,dateofbirth,phonenumber,address,password) VALUES (?, ?, ?,?,?,?,?)",
                    (first_name,last_name,email_address,date_of_birth,phone_number,address , generate_password_hash(password)),
                )
                db.commit()
                data_to_save_in_api_db = request.form.to_dict(flat=True)
                del data_to_save_in_api_db['csrf_token']
                print(data_to_save_in_api_db)
                send_data_to_api_db(data_to_save_in_api_db)
                message = f'{first_name} is registered successfully'
                flash(message, category='success')

            except db.IntegrityError:
                # The username was already taken, which caused the
                # commit to fail. Show a validation error.
                error = f"User {email_address} is already registered."
            else:
                # Success, go to the login page.
                if g.user is not None:
                    return redirect(url_for('engine.index'))
                return redirect(url_for("auth.login"))

        flash(error)
    

    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""

    if g.user is not None:
        username = g.user['FirstName']
        message = f'You are already Logged in as {username}'
        flash(message, category='info')
        return redirect(url_for('engine.index'))

    if request.method == "POST":
        email_address = request.form["email_address"]
        password = request.form["password"]
        db = get_db()
        error = None
        user = db.execute(
            "SELECT * FROM employee WHERE employee.email_address = ?", (email_address,)
        ).fetchone() 

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if error is None:
            # store the user id and the role in a new session and return to the index
            db = get_db()
            session.clear()
            session["user_id"] = user["id"]
            role = db.execute("select role from employeeRole where employeeRole.id = ?", (user['employee_role'],),).fetchone()

            print(f"user id = {user['id']}")
            if role:
                session["role"] = role['role']
                print(f"session role {session['role']}")
            else:
                session['role'] = 'employee'  # by default setting role as employee at the time of login
            user_name = user['FirstName']  # Getting user's firstname from the user object
            message = f'You are logged in as {user_name}'  # if user regeistration done it shows successfull message
            flash(message, category='success')
            return redirect(url_for('engine.home'))

        flash(error)

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    flash('logged out successfully', category='success') 
    return redirect(url_for("index"))



def check_password_validity(s):
    l, u, p, d = 0, 0, 0, 0
    """Password length shoud be greater than 8 characters and contains atleast 1 uppercase,1 lowercase
    and 1 special character and 1 integer"""
    if (len(s) >= 8):
        for i in s:
    
            # counting lowercase alphabets
            if (i.islower()):
                l+=1           
    
            # counting uppercase alphabets
            if (i.isupper()):
                u+=1           
    
            # counting digits
            if (i.isdigit()):
                d+=1           
    
            # counting the mentioned special characters
            if(i=='@'or i=='$' or i=='_'):
                p+=1          
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
        return True
    else:
        return False

def send_data_to_api_db(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://127.0.0.1:5001/post",proxies={"http": "http://api:5001/post"}, verify=False,json=data,headers=headers)
    print(response.status_code)
    print(response.text)



