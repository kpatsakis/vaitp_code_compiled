# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 927_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1663 bytes
from flask import Flask, request, redirect
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SECRET_KEY"] = "super-secret"
app.config["SECURITY_REGISTERABLE"] = True
app.config["SECURITY_REDIRECT_BEHAVIOR"] = "spa"
db = SQLAlchemy(app)
roles_users = db.Table("roles_users", db.Column("user_id", db.Integer(), db.ForeignKey("user.id")), db.Column("role_id", db.Integer(), db.ForeignKey("role.id")))

class Role(db.Model, RoleMixin):
    id = db.Column((db.Integer()), primary_key=True)
    name = db.Column((db.String(80)), unique=True)


class User(db.Model, UserMixin):
    id = db.Column((db.Integer), primary_key=True)
    email = db.Column((db.String(255)), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.before_first_request
def create_user():
    db.create_all()
    if not User.query.first():
        user_datastore.create_user(email="user@example.com", password="password")
        db.session.commit()


@app.route("/")
@login_required
def home():
    return "Welcome! You are logged in."


@app.route("/login")
def login():
    next_url = request.args.get("next")
    if next_url:
        return redirect(next_url)
    return "Please log in."


if __name__ == "__main__":
    app.run(debug=True)

# okay decompiling 927_1.pyc
