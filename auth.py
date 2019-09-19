from flask import Blueprint, render_template, url_for, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from main import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/')
def signup():
    return render_template("index.html")

@auth.route('/signup', methods=["POST"])
def signup_post():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    user = User.query.filter_by(email=email).first()

    if not user:
        if password == confirm_password:
            new_user = User(email=email, username=username, password=password, confirm_password=confirm_password)
            db.session.add(new_user)
            db.session.commit()

    return redirect(url_for('auth.login'))




@auth.route('/logout')
def logout():
    return 'Logout'