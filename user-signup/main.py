from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('input.html')

def isEmpty(user_input):
    if not user_input:
        return True
    else:
        return False

def hasSpace(user_input):
    if " " in user_input:
        return True
    else:
        return False

def invalid_length(user_input):
    if len(user_input) < 3 or len(user_input) > 20:
        return True
    else:
        return False

def valid_email(user_input):
    if user_input.count('@') == 1 and user_input.count('.') == 1:
        return True
    else: 
        return False

def password_match(pass1, pass2):
    if pass1 == pass2:
        return True
    else: return False


@app.route("/", methods=['POST'])
def validate_input():
    username = request.form['username']
    password = request.form['password-init']
    password_verify = request.form['password-verify']
    email = request.form['email']

    username_invalid = ""
    password_invalid = ""
    email_invalid = ""
 
    #username validation
    if isEmpty(username):
        username_invalid = "Please enter a username"
    elif hasSpace(username):
        username_invalid = "Username must contain only alphanumeric and special characters"
    elif invalid_length(username):
        username_invalid = "Username must be between 3 and 20 characters"
    else: 
        username = username

    #password validation
    if isEmpty(password) or isEmpty(password_verify):
        password_invalid = "Please enter a password"
    elif hasSpace(password):
        password_invalid = "Password must contain only alphanumeric and special characters"
    elif invalid_length(password):
        password_invalid = "Password must be between 3 and 20 characters"
    elif not password_match(password, password_verify):
        password_invalid = "Passwords do not match. Please reenter"
    

    #email validation
    if hasSpace(email):
        email_invalid = "email must contain only alphanumeric and special characters"
    elif invalid_length(email):
        email_invalid = "email must be between 3 and 20 characters"
    elif not valid_email(email):
        email_invalid = "email is not valid. Please reenter"
    else:
        email = email

    #welcome user or return errors
    if not username_invalid and not password_invalid and not email_invalid:
        welcome_msg = "Welcome, " + username + "!"
        return render_template('welcome.html', welcome_msg = welcome_msg)
    else:
        return render_template('input.html', username=username, email=email, username_invalid=username_invalid, password_invalid=password_invalid, email_invalid=email_invalid)


app.run()