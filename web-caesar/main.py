from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="/web-caesar" method="post">
        <label for="rot">Rotate by:</label>
        <input id="rot" name="rot" type="text" value="0" />
        <textarea name="text" id="text">{0}</textarea>
        <input type="submit"  />

      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/web-caesar", methods=['POST'])
def encrypt():
    rotate = int(request.form['rot'])
    new_text = request.form['text']
    msg = rotate_string(new_text, rotate)
    return form.format(msg)


app.run()