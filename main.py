from flask import Flask,render_template,request,abort,flash,g,make_response,url_for,redirect,session
import sqlite3
import logging
from config import menu
from database_control import Flaskdb
from forms import Register_form,Login_form,Games_form
from flask_db import get_db
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import login_user,logout_user,login_required,current_user,LoginManager
from login_user import LoginUser
logging.basicConfig(filename="index.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
app=Flask(__name__)

app.config["SECRET_KEY"]="qwertyuio12345678"
app.config["DATABASE"]="project.db"
dbase = None

lm=LoginManager(app)
lm.login_view="login"

@lm.user_loader
def load_user(user_id):
    return LoginUser().getUserFromDb(user_id, dbase)

@app.before_request
def before_request_func():
    global dbase
    db = get_db(g,app)
    dbase = Flaskdb(db)

@app.route("/")
def main():
    return render_template("main.html",menu=menu)   



@app.route("/delete")
@login_required
def delete():
    return render_template("delete.html",menu=menu)

@app.route("/add",methods=["POST","GET"])
@login_required
def add():
    form=Games_form()
    if form.validate_on_submit():
        name=request.form["name"]
        price=request.form["price"]
        desc=request.form["desc"]
        release=request.form["release"]
        photo=request.files["photo"]
        blob=photo.read()
        
    return render_template("add.html",menu=menu,form=form)

@app.route("/exit")
@login_required
def exit():
    logout_user()
    return redirect(url_for("login"))

@app.route("/my_games")
@login_required
def my_games():
    return render_template("my_games.html",menu=menu)

@app.route("/login",methods=["GET","POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("main"))


    form=Login_form()
    if form.validate_on_submit():
        name=request.form["name"]
        password=request.form["password"]

        user=dbase.get_user_by_name(name)
        if not user:
            flash("user with this name doesnt exists",category="fail")
            return redirect(url_for("login"))
        
        if check_password_hash(user["password"],password):
            log=LoginUser().create(user)
            login_user(log)
            return redirect(url_for("main"))
        else:
            flash("wrong password",category="fail")


    return render_template("login.html",menu=menu,form=form)

@app.route("/register",methods=["GET","POST"])
def register():
    form=Register_form()
    if form.validate_on_submit():
        name=form.name.data
        password=form.password.data
        hash_password=generate_password_hash(password)
        if not dbase.check_user(name):
            flash("user already exists",category="fail")
            return redirect(url_for("register"))

        dbase.add_user(name,hash_password)
        return redirect(url_for("login"))
    return render_template("register.html",menu=menu,form=form)

