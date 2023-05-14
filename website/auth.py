from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    # return "<p>Login</p>" b4 importing render_template
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign_up')
def sign_up():
    # return "<p>Sign Up</p>" b4 importing render_template
    return render_template('sign_up.html')
