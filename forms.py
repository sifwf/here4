from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo



class Register_form(FlaskForm):
    name=StringField("name",validators=[DataRequired(),
                                                Length(min=3,max=15,
                                    message="name must be greater than 3 characters and less than 15")],
                                    render_kw={"placeholder":'name'})
    password=PasswordField("password",validators=[DataRequired(),
                                Length(min=4,max=16,
                                       message="password must be greater than 4 characters and less than 16")],render_kw={"placeholder":'password'})
    password2=PasswordField("repeat_password",validators=[EqualTo("password")],render_kw={"placeholder":'repeat password'})
    submit=SubmitField("submit")

class Login_form(FlaskForm):
    name=StringField("name",validators=[DataRequired(),Length(min=3,max=15,message="name must be greater than 3 characters and less than 15")],render_kw={"placeholder":'name'})
    password=PasswordField("password",validators=[DataRequired(),Length(min=4,max=16,message="name must be greater than 4 characters and less than 15")],render_kw={"placeholder":'password'})
    submit=SubmitField("submit")
