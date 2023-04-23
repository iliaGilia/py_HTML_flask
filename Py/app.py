from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello.html")
def hello_world():
     return render_template('hello.html')
@app.route("/guy.html")
def contacts():
    return render_template('guy.html')

@app.route("/die.html")
def dingus():
    return render_template('die.html')

@app.route("/bye.html")
def bingus():
    return render_template('bye.html')


if __name__ == '__main__':
    app.run(debug=True)
