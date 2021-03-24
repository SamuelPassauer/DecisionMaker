from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

"""
@app.route("/<name>")
def user(name):
    return f"Hello {name}"

#Route zu URL/admin, was passiert hier
@app.route("/wrong")
def wrong():
    #wenn URL/wrong eingegeben wird, direkt umleiten zu URL/home
    return redirect(url_for("home"))

#Routing zu admin Seite
@app.route("/admin")
def admin():
    #Direkte Eingabe für name Attribut
    return redirect(url_for("user", name="Admin"))
"""
#Einbinden HTML templates
@app.route("/")
def home():
    return render_template("page1.html", content="Testing")

if __name__ == "__main__":
    app.run(debug=True)