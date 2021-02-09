from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/1.html')
def subpage1():
    return render_template("1.html")
@app.route('/2.html')
def subpage2():
    return render_template("2.html")
@app.route('/3.html')
def subpage3():
    return render_template("3.html")



if __name__ == '__main__':
    app.run(debug = True)