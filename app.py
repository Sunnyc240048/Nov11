from flask import Flask
from flask import render_template,request
import textblob

app = Flask("__name__")

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/",methods=["GET","POST"])
def main():
    name = request.form.get('q')
    return(render_template("main.html"))

@app.route("/SA",methods=["GET","POST"])
def SA():
    return(render_template("SA.html"))
def SA_result():
    q = request.form.get('q')
    r = textblob.TextBlob(q).sentiment
if __name__ == "__main__":
    app.run()
