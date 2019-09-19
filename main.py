from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


app = Flask(__name__)

app.config['SECRET_KEY'] = 'wejfnfewiufwifwefw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ezyqtjaxdfzlqg:b75127d0400c2db636d5825b71abb6700e022a1eeb3e6cdf9fa5b2c0066f6dde@ec2-184-73-232-93.compute-1.amazonaws.com:5432/ddbrciohe0ij1q'
    
db.init_app(app)


    # blueprint for auth routes in our app
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
