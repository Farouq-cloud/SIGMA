from flask import Blueprint, render_template, url_for, redirect, request,flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from models import User
from main import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('A user with that username  does not exist')
        return render_template('login.html')
    is_correct_password = check_password_hash(user.password, password)
    print(is_correct_password)
    if not is_correct_password:
        flash('Wrong Credentials')
        return render_template('login.html')
    flash('Log in successful')
    return redirect(url_for('auth.login'))






@auth.route('/')
def signup():
    return render_template("index.html")

@auth.route('/signup', methods=["POST"])
def signup_post():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if username is None or password is None or email is None or confirm_password is None:
            flash('username, email, password are required')
            return render_template('index.html')
    if ' ' in username:
            flash('Username should not contain spaces')
            return render_template('index.html')
    if password != confirm_password:
            flash("Passwords do not match")
            return render_template('index.html')
    else:
            user = User.query.filter_by(username=username).first()
            if user is not None:
                flash('A user with that username already exists')
                return render_template('index.html')
            user = User.query.filter_by(email=email).first()
            if user is not None:
                flash('A user with that email already exists')
                return render_template('index.html')

            new_user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))

