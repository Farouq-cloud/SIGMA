from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


app = Flask(__name__)

app.config['SECRET_KEY'] = 'wejfnfewiufwifwefw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    
db.init_app(app)


    # blueprint for auth routes in our app
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
