from flask import Flask, redirect, url_for, render_template, request
from flaskext.mysql import MySQL
import mysql.connector
app = Flask(__name__)


conn = mysql.connector.connect(host="localhost",
                               user='root',
                               password='adesso',
                               database='vorgehensmodelle',
                               auth_plugin='mysql_native_password')

cursor = conn.cursor()

'''Kriterien und Ausprägung'''
auswahl_projektgroeße = ["Klein", "Mittel", "Groß"]
auswahl_projekttyp =[]
auswahl_technologielevel = ["Standardtechnologie", "Komplizierte Technologie", "Neue Technologie"]
auswahl_komplexitaet = ["Gering", "Mittel", "Hoch"]
auswahl_qualifikation = ["Wenig qualifiziert", "Qualifiziert", "Professionell"]
auswahl_projektdauer = []
auswahl_klarheit_anforderungen = ["Klar", "Unklar"]
auswahl_einsatz = ["Nebenamtlich", "Teilzeit", "Hauptamtlich"]
auswahl_teamgroeße = []
auswahl_erfahrungsgrad = ["Unter 1,5 Jahren", "Über 1,5 Jahren", "Über 4 Jahre", "Über 10 Jahre", "Über 15 Jahren"]
auswahl_bedeutung = ["Gering", "Groß", "Sehr groß"]
auswahl_zeitkritikalitaet = ["Gering", "Mittel", "Hoch"]
auswahl_verteilung = ["Zentral", "Dezentral"]
auswahl_stabilitaet_anforderungen = ["Stabil", "Volatil"]

'''Bausteine Vorgehensmodell'''

#Projekt starten
#Grobziele definieren

#Kundenanforderungen erheben
beobachtungstechnik_score = 0
befragungstechnik_score = 0
kreativitaetstechnik_score = 0

#Kundenanforderungen festhalten
initialer_product_backlog_score = 0
lastenheft_score = 0

#PM-Prozess festlegen

#Organisation festlegen
matrix_score = 0
stab_score = 0
reine_po_score = 0

#Rollen definieren

#Anforderungsspezifikation

#Anforderungen Priorisieren
bubble_sort_score = 0
numeral_assignment_score = 0
ahp_score = 0
cv_score = 0
msp_score = 0
hcv_score = 0

#Anforderungen dokumentieren
pflichtenheft_dokumentieren_score = 0
product_backlog_dokumentieren_score = 0

#Phasen und Meilensteine festlegen

#Inhalte planen
product_backlog_planen_score = 0
projektstrukturplan_score = 0

#Aufwände schätzen
experten_score = 0
algorithmisch_score = 0
tshirt_score = 0
planning_poker_score = 0

#Termine planen
gantt_termine_score = 0
netzplan_score = 0
product_backlog_termine = 0

#Iterative Detailplanung
sprint_backlog_score = 0
'''??'''

#Prozessmodell für Systementwicklung festlegen
agil_score = 0
klassisch_score = 0

#Fortschritt bestimmen
burndown_score = 0
gantt_fortschritt_score = 0

#Fortschritt analysieren
sprint_review_score = 0
eva_score = 0
meilensteintrend_score = 0

#Fortschritt steuern
sprint_retrospektive_score = 0
ressourcen_veraendern_score = 0

#Ergebnisse übergeben
finales_produkt_score = 0
inkrement_score = 0



def projektgroeße():
    projektgroeße = request.form.get("projektgroeße")
    if projektgroeße == "Klein":
        ahp_score += 1
        cv_score += 1
        bubble_sort_score += 1
        stab_score += 1
        product_backlog_planen_score += 1
    elif verteilung == "Mittel":
        msp_score += 1
        cv_score += 1
        numeral_assignment_score += 1
        matrix_score += 1
        projektstrukturplan_score += 1
    elif verteilung == "Groß":
        hcv_score += 1
        msp_score += 1
        reine_po_score += 1
        projektstrukturplan_score += 1

def inhalte_planen(product_backlog_planen_score, projektstrukturplan_score):
    if projektstrukturplan_score > initialer_product_backlog_score:
        print("Projektstrukturplan")
    elif product_backlog_planen_score > projektstrukturplan_score:
        print("Product Backlog")

def anforderungen_priorisieren(ahp_score, cv_score, bubble_sort_score, numeral_assignment_score,hcv_score, msp_score)
    anforderungen_priorisieren = [ahp_score, cv_score, bubble_sort_score, msp_score, numeral_assignment_score, hcv_score]
    print(max(anforderungen_priorisieren))


#Einbinden HTML templates
#Route von / nach /broetchenwahl
@app.route("/")
def home():
    return redirect("/multiple")

@app.route("/multiple")
def multiple():
    return render_template("multiple_forms.html", methods=["POST", "GET"], auswahl_verteilung=auswahl_verteilung, auswahl_einsatz=auswahl_einsatz, auswahl_bedeutung=auswahl_bedeutung)

@app.route("/auswahl")
def auswahl():
    choice_verteilung = request.form.get("verteilung")
    """score_baustein_eins = 0
    score_baustein_zwei = 0
    if choice_verteilung == "Zentral":
        score_baustein_eins += 1
    elif choice_verteilung == "Dezentral":
        score_baustein_zwei += 1

    baustein = verteilung(score_baustein_eins, score_baustein_zwei)
"""

    return render_template("auswahl.html", choice_verteilung=choice_verteilung)
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