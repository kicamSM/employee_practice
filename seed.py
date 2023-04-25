"""Seed file to make sample data for db"""

from models import Department, Employee, Project, EmployeeProjects, db 
from app import app

# create all tables 
# db.drop_all()
# db.create_all()

EmployeeProjects.query.delete()
Employee.query.delete()
Department.query.delete()
Project.query.delete()

d1 = Department(dept_code="mktg", dept_name="Marketing", phone="811-1111")
d2 = Department(dept_code="acct", dept_name="Accounting", phone="822-2222")
d3 = Department(dept_code="r&d", dept_name="Research and Development", phone="833-3333")
d4 = Department(dept_code="sales", dept_name="Sales", phone="444-4444")
d5 = Department(dept_code="it", dept_name="Information Technology", phone="555-5555")
d6 = Department(dept_code="Rndm", dept_name="Random")

river = Employee(name="River Bottom", state="NY", dept=d2)
mountain = Employee(name="Mountain Top", state="WY", dept=d1)
valley = Employee(name="Valley Low", state="CA", dept=d1)
cloud = Employee(name="Cloud High", state="CO", dept=d2)
rain = Employee(name="Rain Fall", state="CA", dept=d5)
rock = Employee(name="Rock Pick", state="WY", dept=d6)
snow = Employee(name="Snow Storm", state="CO", dept=d3)
tree = Employee(name="Tree Bark", state="CO")
no = Employee(name="Transient Fellow")

db.session.add_all([d1, d2, d3, d4, d5, d6, river, mountain, valley, cloud, rain, rock, snow, tree, no])
db.session.commit()

pc = Project(proj_code='car', proj_name='Design Car', assignments=[EmployeeProjects(emp_id=river.id, role='Chair'), EmployeeProjects(emp_id=mountain.id)])

ps = Project(proj_code='server', proj_name='Deploy Server', 
             assignments = [EmployeeProjects(emp_id=river.id), EmployeeProjects(emp_id=rain.id, role='Auditor')])

db.session.add([pc, ps])
db.session.commit()
