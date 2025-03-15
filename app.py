from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user


app = Flask(__name__)

# Secret Key For Password Security
app.config["SECRET_KEY"] = "1122"

# Database setup using SQlite3
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///users.db"

# Making a pointer to the database and hashing passwords and login manager
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Making the default app route if the user is not logged in to point to that
login_manager.login_view = "login"

# User Model For the database

# My main index route
@app.route("/")
def home():
    return "Hello, Flask"


# Default app stuff
if __name__ == '__main__':
    app.run(debug=True)