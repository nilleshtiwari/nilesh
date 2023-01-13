DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS employeeRole;
DROP TABLE IF EXISTS address


CREATE TABLE employeeRole (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  role TEXT UNIQUE NOT NULL
);


CREATE TABLE employee (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  FirstName TEXT NOT NULL,
  LastName TEXT NOT NULL,
  email_address TEXT UNIQUE NOT NULL ,
  dateofbirth DATE,
  phonenumber INTEGER NOT NULL,
  employee_role INTEGER,
  password TEXT NOT NULL,
  FOREIGN KEY (employee_role) REFERENCES employeeRole (id)
);

