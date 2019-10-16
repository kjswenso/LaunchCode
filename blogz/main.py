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

    def __init__(self, title, body):
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

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():

    #owner = User.query.filter_by(email=session['email']).first()

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['content']
        new_blog = Blog(title, body)

        if new_blog.isValid():
            db.session.add(new_blog)
            db.session.commit() 
            return redirect('/blog?id=' + str(new_blog.id))

        else:
            flash("Please provide all content", 'error')
            return render_template('newpost.html', title=title, body=body)

    else:
        return render_template('newpost.html')

@app.route('/blog')
def blog_listing():

    blog_id = request.args.get('id')

    if blog_id:
        blog = Blog.query.get(blog_id)
        return render_template('entry.html', blog=blog)

    blogs = Blog.query.all()
    return render_template('blog.html', blogs=blogs)

@app.route('/', methods=['POST', 'GET'])
def index():

    return redirect('/blog')

if __name__ == '__main__':
    app.run()