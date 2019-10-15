from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:build-a-blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'y448kGbzs&zR4C'


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1000))

    def __init__(self, title, body):
        self.title = title
        self.body = body



@app.route('/newpost', methods=['POST', 'GET'])
def new_post():
    
    return render_template('newpost.html')

@app.route('/blog', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['content']
        new_blog = Blog(title, body)
        db.session.add(new_blog)
        db.session.commit()

    blogs = Blog.query.all()

    return render_template('blog.html', blogs=blogs)

if __name__ == '__main__':
    app.run()