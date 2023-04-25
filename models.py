"""Models for Employees."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class Department(db.Model):
    """Department Model"""
    __tablename__ = 'departments'
    
    dept_code = db.Column(db.Text, primary_key=True)
    dept_name = db.Column(db.Text, nullable=False, unique=True)
    phone = db.Column(db.Text)
    
    def __repr__(self):
        return f"<Department {self.dept_code} {self.dept_name} {self.phone}>"
    
    # employees = db.relationship('Employee')
    
class Employee(db.Model):
    """Employee Model"""
    __tablename__ = 'employees'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    state = db.Column(db.Text, nullable=True, default="None")
    dept_code = db.Column(db.Text, db.ForeignKey('departments.dept_code'))
    
    dept = db.relationship('Department', backref="employees")
    
    assignments = db.relationship('EmployeeProjects', backref=('employee')) 
    # note you can name the backreference what you want but have to remmember it for referencing 
    
    projects = db.relationship('Project', secondary="employees_projects", backref="employees")
    # can use this instead of the one above 
    
    def __repr__(self):
        return f"<Employee {self.name} {self.state} {self.dept_code} {self.id}>"
    
class Project(db.Model):
    """Project Model"""
    __tablename__ = "projects"
    
    proj_code = db.Column(db.Text, primary_key=True)
    proj_name = db.Column(db.Text, nullable=False, unique=True)
    
    assignments = db.relationship('EmployeeProjects', backref='project')
    
class EmployeeProjects(db.Model):
    """Employee Projects Model"""
    __tablename__ = "employees_projects"
    
    emp_id = db.Column(db.Integer, db.ForeignKey('employees.id'), primary_key=True)
    proj_code = db.Column(db.Text, db.ForeignKey('projects.proj_code'), primary_key=True)
    role = db.Column(db.Text)

    
    
def get_directory():
    all_emps = Employee.query.all()
    
    for emp in all_emps:
        if emp.dept is not None:
            print(emp.name, emp.dept.dept_name, emp.dept.phone)
        else:
            print(emp.name)
            
def get_directory_join():
    directory = db.session.query(Employee.name, Department.dept_name, Department.phone).join(Department).all()
    
    for name, department, phone in directory:
        print(name, department, phone)
        
def get_directory_join_class():
    directory = db.session.query(Employee, Department).join(Department).all()
    
    for emp, dept in directory:
        print(emp.name, dept.dept_name, dept.phone)
    
def get_directory_all_join():
    directory = db.session.query(Employee.name, Department.dept_name, Department.phone).outerjoin(Department).all()
    
    for name, dept, phone in directory:
        print(name, dept, phone)
    
    