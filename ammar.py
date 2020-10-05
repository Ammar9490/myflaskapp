from flask import Flask, render_template, request, redirect, url_for, session 

app = Flask(__name__)
app.secret_key = "Ammar1994"

@app.route('/')
def home():
    return "<h2>hello ammar</h2>"

@app.route('/login', methods= ["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form['nm']
        session['user'] = user
        return redirect(url_for("user"))
    else:
        return "render Go"

@app.route('/user')
def user():
    if "user" in session:
        user = session['user']
        return user
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)