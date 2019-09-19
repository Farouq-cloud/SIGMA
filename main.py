from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'wejfnfewiufwifwefw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
    
db.init_app(app)


    # blueprint for auth routes in our app
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
