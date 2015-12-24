from flask import Flask, render_template
import string

app = Flask(__name__)

@app.route("/")
def home():
    btnList = [i for i in ("A","B","C","D","E")]
   # btnList = [i for i in (1,2,3,4,5)]
    return render_template("home.html", btnList = btnList)

app.run(debug=True)