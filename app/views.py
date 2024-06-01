from app import app
from flask import render_template
from flask import request
from resh import solution

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['GET', 'POST'])
def ovtet():
    if request.method == 'POST':
        a = float(request.form.get ('a'))
        b = float(request.form.get ('b'))
        c = float(request.form.get ('c'))
    return render_template("index.html", answer = solution(a,b,c))