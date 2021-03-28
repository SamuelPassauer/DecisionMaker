from flask import Flask, redirect, url_for, render_template, request
from flaskext.mysql import MySQL
app = Flask(__name__)

mysql = MySQL()

#MySQL config
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'adesso'
app.config['MYSQL_DATABASE_DB'] = 'vorgehensmodelle'

mysql.init_app(app)
con = mysql.connect()
cursor = con.cursor()


#Einbinden HTML templates
@app.route("/")
def home():
    return redirect("/erstesKriterium")

@app.route("/erstesKriterium", methods = ["GET", "POST"])
def erstesKriterium():
    cursor.execute("SELECT preference FROM vorgehensmodelle.broetchen;")
    preferenceList = cursor.fetchall()
    return render_template("erstesKriterium.html", preferenceList=preferenceList)

@app.route("/letztesKriterium", methods = ["GET", "POST"])
def letztesKriterium():
    if request.method == "POST":
        cursor.execute("SELECT preference2 FROM vorgehensmodelle.broetchen;")
        preferenceList = cursor.fetchall()
        return render_template("letztesKriterium.html", preferenceList=preferenceList)

@app.route("/alleKriterienUndEmpfehlung", methods = ["GET", "POST"])
def alleKriterienUndEmpfehlung():
    return render_template("alleKriterienUndEmpfehlung.html")


if __name__ == "__main__":
        app.run(debug=True)