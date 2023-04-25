from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired
class AddSnackForm(FlaskForm):

    price = FloatField("Price in USD")
    name = StringField("Snack Name")
    # quantity = FloatField("Amount of Snacks")
    is_healthy = BooleanField("This is a healthy snack")
    quantity = IntegerField("how many?")
    # category = RadioField("Category", choices= [('ic', 'Icecream'), ('chips', 'potato chips'), ('candy', 'candy/sweets')])
    category = SelectField("Category", choices= [('ic', 'Icecream'), ('chips', 'potato chips'), ('candy', 'candy/sweets')])
        
class NewEmployeeForm(FlaskForm):
    
    name = StringField("Employee Name")
    state = StringField( "State")
    dept_code = SelectField("Department Code")