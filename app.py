from flask import Flask, render_template, request, redirect, url_for

from DB_operations import add_user

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("/index.html")


@app.route('/users', methods=['POST', 'GET'])
def user():
    if request.method == "POST":
        email = request.form["email"]
        psw = request.form["psw"]
        psw_repeat = request.form["psw_repeat"]

        # saving all the values to db
        add_new = add_user(email, psw, psw_repeat)
        return redirect(url_for('helloworld'))
    else:
        return render_template('index.html')
