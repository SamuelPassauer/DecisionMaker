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
#Route von / nach /broetchenwahl
@app.route("/")
def home():
    return redirect("/multiple")

@app.route("/multiple")
def multiple():
    cursor.execute("SELECT preference FROM vorgehensmodelle.broetchen;")
    preferenceList = cursor.fetchall()
    cursor.execute("SELECT preference2 FROM vorgehensmodelle.broetchen;")
    preferenceList2 = cursor.fetchall()
    return render_template("multiple_forms.html", preferenceList=preferenceList, preferenceList2=preferenceList2)

'''#/broetchenwahl
@app.route("/broetchenwahl")
def broetchenwahl():
    cursor.execute("SELECT broetchen FROM broetchen")
    broetchenList = cursor.fetchall()
    return render_template("broetchenwahl.html", broetchenList=broetchenList)
#/aufstrichewahl, Anzeige: gewähltes Brötchen
@app.route("/aufstrichewahl", methods=["POST", "GET"])
def aufstrichewahl():
    if request.method == "POST":
        choiceBrötchen = request.form["choose"]
        print("INSERT INTO vorgehensmodelle.gewaehltbroetchen(gewaehltbroetchenrow) VALUES (" +"'" + choiceBrötchen +"'"+ ")")
        cursor.execute("INSERT INTO vorgehensmodelle.gewaehltbroetchen(gewaehltbroetchenrow) VALUES (" +"'" + choiceBrötchen +"'"+ ")")
        con.commit()
        cursor.execute("SELECT aufstriche FROM aufstriche")
        aufstricheList = cursor.fetchall()
    return "Your choice is " + choiceBrötchen + render_template("aufstrichewahl.html", aufstricheList=aufstricheList)

#/gesamtwahl - alle gewählten Optionen werden aus DB geladen
@app.route("/gesamtwahl", methods=["POST", "GET"])
def gesamtwahl():
    if request.method == "POST":
        choiceAufstrich = request.form["choose"]
        print("INSERT INTO vorgehensmodelle.gewaehltaufstrich(gewaelt) VALUES (" +"'" + choiceAufstrich +"'"+ ")")
        cursor.execute("INSERT INTO vorgehensmodelle.gewaehltaufstrich(gewaelt) VALUES (" +"'" + choiceAufstrich +"'"+ ")")
        con.commit()
        cursor.execute("SELECT gewaelt FROM vorgehensmodelle.gewaehltaufstrich")
        aufstrich = cursor.fetchone()
        cursor.execute("SELECT gewaehltbroetchenrow FROM vorgehensmodelle.gewaehltbroetchen")
        broetchen = cursor.fetchone()
    return broetchen[0] + aufstrich[0]

#/preferencesBrötchen
@app.route("/preferencesbroetchen")
def preferencesBroetchen():
    """cursor.execute("SELECT preference FROM broetchen")
    preferencesList = cursor.fetchall()
    cursor.execute("SELECT preference2 from broetchen")
    preferencesList2 =cursor.fetchall()"""
    return render_template("preferences.html")

@app.route("/auswahl")
def auswahl():
    if request.method == "POST":
        preference = request.form["choose"]
        #preference2 = request.form["choose2"]
        return preference + render_template('auswahl.html')
        if cursor.execute("SELECT count(*) FROM vorgehensmodelle.broetchen WHERE preference ='"+ preference +"' && preference2 =" + "'"+preference2+"';") == 1:
            auswahl = cursor.execute("SELECT * FROM vorgehensmodelle.broetchen WHERE preference ='"+ preference +"' && preference2 =" + "'"+preference2+"';")
            con.commit()
            return "Dieses Brötchen passt für dich: " + auswahl
        else:
            alternativeArt = cursor.execute("SELECT * FROM vorgehensmodelle.broetchen WHERE preference ='"+ preference +"';")
            alternativeGröße = cursor.execute("SELECT * FROM vorgehensmodelle.broetchen WHERE preference2 ='"+ preference2 +"';")
            con.commit()
            return "Hier eine Alternative in einer anderen Größe: "+alternativeArt[0] +" und hier eine Alternative mit anderer Teigart:" + alternativeGröße[0]'''
if __name__ == "__main__":
    app.run(debug=True)