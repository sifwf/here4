from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,TextAreaField,DateField,FileField,SelectField
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

class Games_form(FlaskForm):
    name=StringField("name",validators=[DataRequired(),
                                                Length(min=3,
                                    message="name must be greater than 3 characters")],
                                    render_kw={"placeholder":'name'})
    price=StringField("price",validators=[DataRequired(),Length(min=1,max=5,message="too much")],render_kw={"placeholder":'price'})
    desc=TextAreaField("desc",validators=[DataRequired()])
    release=DateField("release",validators=[DataRequired()])
    photo=FileField("photo",validators=[DataRequired()])
    submit=SubmitField("submit")

class Edit_form(FlaskForm):

    price=StringField("price",validators=[Length(min=1,max=5,message="too much")],render_kw={"placeholder":'price'})
    desc=TextAreaField("desc",validators=[])
    release=DateField("release",validators=[])
    photo=FileField("photo",validators=[])
    submit=SubmitField("submit")
