from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import DataRequired # validator field

#to create fields we need to import the fields of possible fields
# form login user class

class LoginForm(Form):
	#the first argument is the name of the field, the second is the validator
	username=StringField("username", validators=[DataRequired()])
	password=PasswordField("password", validators=[DataRequired()])
	remember_me=BooleanField("remenber me")
	