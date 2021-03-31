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
    firstChoice = request.form["choose"]
    cursor.execute("DELETE FROM wahl1;")
    con.commit()
    cursor.execute("INSERT INTO vorgehensmodelle.wahl1(wahl1) VALUES (" + "'" + firstChoice + "'" + ")")
    con.commit()
    cursor.execute("SELECT preference2 FROM vorgehensmodelle.broetchen;")
    preferenceList = cursor.fetchall()
    return render_template("letztesKriterium.html", preferenceList=preferenceList, firstChoice=firstChoice)
@app.route("/alleKriterienUndEmpfehlung", methods = ["GET", "POST"])
def alleKriterienUndEmpfehlung():
    if request.method == "POST":
        secondChoice = request.form["choose"]
        cursor.execute("DELETE FROM wahl2;")
        cursor.execute("INSERT INTO vorgehensmodelle.wahl2(wahl2) VALUES (" + "'" + secondChoice + "'" + ")")
        con.commit()
        cursor.execute("SELECT * FROM vorgehensmodelle.wahl1 LIMIT 1")
        first = cursor.fetchall()
        firstChoice = first[0][0]
        print(firstChoice)
        #Problem: (('Vollkorn',),) ist die Ausgabe
        #print("SELECT count(*) FROM vorgehensmodelle.broetchen WHERE preference ='" + str(firstChoice) + "' && preference2 =" + "'" + secondChoice + "';")

        if cursor.execute("SELECT count(*) FROM vorgehensmodelle.broetchen WHERE preference ='" + firstChoice + "' && preference2 =" + "'" + secondChoice + "';") == 1:
            cursor.execute("SELECT broetchen FROM vorgehensmodelle.broetchen WHERE preference ='" + firstChoice + "' && preference2 =" + "'" + secondChoice + "';")
            best = cursor.fetchall()
            cursor.execute("SELECT broetchen FROM vorgehensmodelle.broetchen WHERE preference ='" + firstChoice + "' && preference2 =" + "'" + secondChoice + "';")
            best1 = cursor.fetchone()
            bestFit = best[0][0]
            print("SELECT broetchen FROM vorgehensmodelle.broetchen WHERE preference ='" + firstChoice + "' && preference2 =" + "'" + secondChoice + "';")
            print(bestFit)
            print(best1)
            cursor.execute("SELECT broetchen FROM vorgehensmodelle.broetchen WHERE preference ='" + firstChoice + "' AND NOT broetchen = '" + bestFit + "';")
            print("SELECT broetchen FROM vorgehensmodelle.broetchen WHERE preference ='" + firstChoice + "';")
            alternativeOne = cursor.fetchone()
            cursor.execute("SELECT broetchen FROM vorgehensmodelle.broetchen WHERE preference2 ='" + secondChoice + "' AND NOT broetchen = '" + bestFit + "';")
            print("SELECT broetchen FROM vorgehensmodelle.broetchen WHERE preference2 ='" + secondChoice + "';")
            alternativeTwo = cursor.fetchone()
            recommendations = [best1, alternativeOne, alternativeTwo]
            print(recommendations)
            return render_template("alleKriterienUndEmpfehlung.html", recommendations=recommendations)


if __name__ == "__main__":
        app.run(debug=True)