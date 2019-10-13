from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://get-it-done:beproductive@localhost:8889/get-it-done'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Task(db.Model): 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __init__(self, name):
        self.name = name


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        task_name = request.form['task']
        new_task = Task(task_name)
        db.session.add(new_task)
        db.session.commit()

    tasks = Task.query.all()

    return render_template('todos.html', title="Get It Done!", tasks=tasks)

@app.route('/delete-task', methods=["POST"])
def delete_task():
    task_id = int(request.form['task_id'])
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run()