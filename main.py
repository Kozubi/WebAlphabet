from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    btnList = [i for i in range(1,11)]
    return render_template("home.html", btnList = btnList)

app.run(debug=True)