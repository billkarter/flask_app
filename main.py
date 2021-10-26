from flask import flask
app= Flask(__name__)

@app.route('/<name>')
@app.route('/Hello/<name>')
def hello_world(name):
    return '<p>ПРИВЕТ {},</p>'.format(name)
