from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:blogz@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'y448kGbzs&zR4C'


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1000))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, body, owner):
        self.title = title
        self.body = body
        self.owner = owner

    def isValid(self):
        if self.title and self.body:
            return True
        else:
            return False

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    blogs = db.relationship('Blog', backref="owner")

    def __init__(self, email, password):
        self.email = email
        self.password = password

@app.before_request
def require_login():
    allowed_routes = ['index', 'blog_listing', 'login', 'signup']
    if request.endpoint not in allowed_routes and 'email' not in session:
        return redirect('/login')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and user.password == password: 
            session['email'] = email
            flash("Logged in")
            return redirect("/newpost")
        else:
            flash("User password incorrect, or user does not exist", 'error')
            
    return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify']

        
        existing_user = User.query.filter_by(email=email).first()
        if not existing_user:
            new_user = User(email, password)
            db.session.add(new_user)
            db.session.commit()
            session['email'] = email
            return redirect('/newpost')
        else: 
              
            return '<h1>Duplicate user</h1>'

    return render_template('signup.html')

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['content']
        owner = User.query.filter_by(email=session['email']).first()
        new_blog = Blog(title, body, owner)

        if new_blog.isValid():
            db.session.add(new_blog)
            db.session.commit() 
            return redirect('/blog?id=' + str(new_blog.id))

        else:
            flash("Please provide all content", 'error')
            return render_template('newpost.html', title=title, body=body, owner=owner)

    else:
        return render_template('newpost.html')

@app.route('/blog')
def blog_listing():

    if request.args.get('id'):
        blog_id = request.args.get('id')
        blog = Blog.query.get(blog_id)
        return render_template('entry.html', blog=blog)

    elif request.args.get('user'):
        user_id = request.args.get('user')
        user = User.query.get(user_id)
        blogs = Blog.query.filter_by(owner=user).all()
        return render_template('singleUser.html', blogs=blogs)

    blogs = Blog.query.all()
    return render_template('blog.html', blogs=blogs)

@app.route('/logout')
def logout():
    del session['email']
    return redirect('/blog')

@app.route('/', methods=['POST', 'GET'])
def index():
    authors = User.query.all()
    return render_template('index.html', authors=authors)

if __name__ == '__main__':
    app.run()