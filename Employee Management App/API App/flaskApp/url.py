from flask import jsonify, request
from flaskApp.db import get_db
from werkzeug.security import generate_password_hash


def api_url(app):
    @app.route('/<data>')
    def search(data):
        regex_of_searched_data = f'%{data}%'
        db = get_db()
        mathced_name = db.execute(
            "SELECT FirstName, LastName, email_address,dateofbirth,phonenumber,address,employee_role,id from employee where FirstName LIKE ? OR address LIKE ? OR LastName LIKE ? order by employee.id desc",
            (regex_of_searched_data, regex_of_searched_data,regex_of_searched_data),).fetchall() 
        data = []
        for name in mathced_name:
            data.append([x for x in name])
        return jsonify(data)

    @app.route('/post',methods=['POST'])
    def save_data_from_main_app_to_api_db():
        first_name = request.json["FirstName"]
        last_name  = request.json["LastName"]
        password = request.json["password1"]
        confirm_password = request.json["password2"]
        email_address = request.json["email_address"]
        date_of_birth = request.json["DOB"]
        phone_number = request.json["PhoneNumber"]
        address = request.json["address"]
        db = get_db()
        db.execute(
                    "INSERT INTO employee (FirstName,LastName,email_address,dateofbirth,phonenumber,address,password) VALUES (?, ?, ?,?,?,?,?)",
                    (first_name,last_name,email_address,date_of_birth,phone_number,address , generate_password_hash(password)),
                )
        db.commit()
        return 'success'

    @app.route('/update',methods=['POST'])
    def update_data_from_main_app_to_api_db():
        first_name = request.json["FirstName"]
        last_name  = request.json["LastName"]
        email_address = request.json["email_address"]
        date_of_birth = request.json["DOB"]
        phone_number = request.json["PhoneNumber"]
        address = request.json["address"]
        role = request.json["employee-role"]
        db = get_db()
        db.execute(
                "UPDATE employee SET FirstName=?,LastName=?,email_address=?,dateofbirth=?,address=?,employee_role=?,phonenumber=? where email_address=?",(first_name,last_name,email_address,date_of_birth,address,role,phone_number,email_address,),
            )
        db.commit()
        return 'updated successfully'

    @app.route('/delete', methods=['POST'])
    def delete_data_from_main_app_to_api_db():
        email_address = request.json["email_address"]
        db = get_db()
        db.execute(
            "DELETE FROM employee WHERE employee.email_address = ?", (email_address,))
        db.commit()
        return 'deleted successfully'