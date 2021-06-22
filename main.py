from flask import Flask, redirect, url_for, render_template, request
from flaskext.mysql import MySQL
app = Flask(__name__)

''' ---------------------------------------------------------------- KRITERIEN UND AUSPRÄGUNG ---------------------------------------------------------------- '''
#Speichern der Werte aller Kriterien welche auf der Auswahlseite angezeigt werden
auswahl_projektgroeße = ["Klein", "Mittel", "Groß"]
auswahl_teamgroeße = ["Klein", "Mittel", "Groß"]
auswahl_komplexitaet = ["Gering", "Mittel", "Hoch"]
auswahl_qualifikation = ["Wenig qualifiziert", "Qualifiziert", "Professionell"]
auswahl_projektdauer = ["Kurz", "Mittel", "Lang"]
auswahl_klarheit_anforderungen = ["Klar", "Unklar"]
auswahl_einsatz = ["Nebenamtlich", "Teilzeit", "Hauptamtlich"]
auswahl_erfahrungsgrad = ["Unter 1,5 Jahren", "Über 1,5 Jahren", "Über 4 Jahre", "Über 10 Jahre", "Über 15 Jahren"]
auswahl_bedeutung = ["Gering", "Groß", "Sehr groß"]
auswahl_zeitkritikalitaet = ["Gering", "Mittel", "Hoch"]
auswahl_verteilung = ["Zentral", "Dezentral"]
auswahl_stabilitaet_anforderungen = ["Stabil", "Volatil"]
auswahl_technologielevel_messen = ["Neue Technologie", "Standardtechnologie", "Komplizierte Technologie"]
auswahl_projekttyp = ["Original Design", "Parametric Design", "Configuration Design", "Redesign Project", "Selection Design"]

kriterienauswahl = {"Projektgröße": auswahl_projektgroeße,
                    "Teamgröße": auswahl_teamgroeße,
                    "Komplexität": auswahl_komplexitaet,
                    "Projektdauer": auswahl_projektdauer,
                    "Klarheit der Anforderungen": auswahl_klarheit_anforderungen,
                    "Einsatzzeit der Mitarbeiter": auswahl_einsatz,
                    "Höchste Erfahrungsstufe im Team": auswahl_erfahrungsgrad,
                    "Bedeutung für das Unternehmen": auswahl_bedeutung,
                    "Zeitkritikalität": auswahl_zeitkritikalitaet,
                    "Verteilung der Projektbeteiligten": auswahl_verteilung,
                    "Stabilität der Anforderungen": auswahl_stabilitaet_anforderungen,
                    "Qualifikation der Mitarbeiter": auswahl_qualifikation,
                    "Technologielevel": auswahl_technologielevel_messen,
                    "Projekttyp": auswahl_projekttyp}

beschreibung = {"Projektgröße": "Die Projektgröße richtet sich nach der Anzahl der Anforderungen und dem Aufwand für Managament und Koordination.",
                "Teamgröße": "Die Teamgröße ist die Anzahl der im Projektteam arbeitenden Personen.",
                "Komplexität": "Die Komplexität setzt sich aus sozialer und inhaltlicher Komplexität zusammen. "
                               "Somit steigt die Komplexität, wenn die Anzahl der Beteiligten am Projekt steigt und wenn die Vernetzung der Elemente im Projekt und deren Dynamik steigt.",
                "Projektdauer": "Die Projektdauer stellt die Dauer des Projekts dar.",
                "Klarheit der Anforderungen": "Die Klarheit der Anforderungen soll zu Projektbeginn abgeschätzt werden. Sind die Anforderungen unklar, so muss im Projekt mehr Aufwand investiert werden, um Klarheit über die Anforderungen zu erlangen.",
                "Einsatzzeit der Mitarbeiter": "Das Einsatzzeit der Mitarbeiter wird an deren Einsatz am Projekt gemessen.",
                "Höchste Erfahrungsstufe im Team": "Die höchste Erfahrungsstufe im Team richtet sich nach der Person im Team mit der höchsten Erfahrung. Die Erfahrung dieser Person dient als Wert für die Einschätzung.",
                "Bedeutung für das Unternehmen": "Die Bedeutung für das Unternehmen richtet sich nach der strategischen Bedeutung für das Unternehmen, die Sichtbarkeit des Projekts in der Organisation und dem Einfluss auf andere Bereiche innerhalb der Organisation und soll anhand dieser Variablen bestimmt werden.",
                "Zeitkritikalität": "Die Zeitkritikalität wird bestimmt anhand der Dringlichkeit und ob ein Projekt mit einer strikten Deadline versehen ist. Je höher die Zeitkritikalität ist, desto schneller werden Ergebnisse aus dem Projekt erwartet.",
                "Verteilung der Projektbeteiligten": "Die Verteilung der Projektbeteiligten bezieht sich auf die geographische Verteilung der beteiligten Personen im Projekt. Sie gilt bereits als dezentral, sobald die Beteiligten auf mehrere Gebäude verteilt sind.",
                "Stabilität der Anforderungen": "Die Stabilität der Anforderungen wird vor dem Projekt abgeschätzt und wird maßgeblich durch die Änderungswahrscheinlichkeit der Anforderungen bestimmt.",
                "Qualifikation der Mitarbeiter": "Die Qualifikation der Mitarbeiter bezieht sich auf das gesamte Projektteam inklusive Projektleitung -/ Management.",
                "Technologielevel": "Das Technologielevel bestimmt den Vertrautheits- und Bekanntheitsgrad der im Projekt geplanten Technologie zur Lösung des Problems.",
                "Projekttyp": "Der Projekttyp ist ein Kriterium, um herauszufinden, in welchem Umfang ein Projekt durchgeführt wird. "
                              "Original Design durchläuft den gesamten Entwicklungszyklus. "
                              "Parametric Design ist die Anpassung von Parametern an die Anforderungen. "
                              "Beim Configuration Design werden existierende Module und Komponenten ausgewählt und zusammengesetzt. "
                              "Beim Redesign Project wird ein existierendes Produkt an neue Anforderungen angepasst. "
                              "Bei Selection Design wird eine Standardkomponente aus einem Katalog ausgewählt. "}

""" ---------------------------------------------------------------- BAUSTEINE ---------------------------------------------------------------- """


#Projekt starten
#Grobziele definieren

#Kundenanforderungen erheben
beobachtungstechnik_score = 0
befragungstechnik_score = 0
kreativitaetstechnik_score = 0

def kundenanforderungen_erheben_funktion(beobachtungstechnik_score, kreativitaetstechnik_score, befragungstechnik_score):
    k = komplexitaet_messen(befragungstechnik_score, kreativitaetstechnik_score, matrix_score,
                            stab_score, reine_po_score, pflichtenheft_dokumentieren_score,
                            projektstrukturplan_score, netzplan_score, formale_score,
                            uml_score, natürlichsprachig_score, product_backlog_termine_score,
                            gantt_termine_score, phasen_vorgehen, agiles_vorgehen)
    z = zeitkritikalitaet_messen(ahp_score, bubble_sort_score, cv_score,
                                 numeral_assignment_score, hcv_score, msp_score,
                                 beobachtungstechnik_score, befragungstechnik_score, initialer_product_backlog_score,
                                 stab_score, reine_po_score, matrix_score,
                                 burndown_score, netzplan_score, product_backlog_termine_score,
                                 gantt_termine_score, phasen_vorgehen, agiles_vorgehen)
    q = qualifikation_messen(beobachtungstechnik_score, matrix_score, stab_score,
                             reine_po_score, experten_score, algorithmisch_score,
                             formale_score, uml_score, natürlichsprachig_score,
                             netzplan_score, product_backlog_termine_score, gantt_termine_score)
    pd = projektdauer_messen(befragungstechnik_score, beobachtungstechnik_score, stab_score,
                             matrix_score, reine_po_score, planning_poker_score,
                             netzplan_score, product_backlog_termine_score, gantt_termine_score)
    ka = klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score,
                                       projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score,
                                       initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score,
                                       burndown_score, eva_score, meilensteintrend_score, phasen_vorgehen, agiles_vorgehen)
    e = einsatz_messen(beobachtungstechnik_score, stab_score, reine_po_score, matrix_score)
    er = erfahrung_messen(beobachtungstechnik_score, reine_po_score, matrix_score,
                          stab_score, experten_score, formale_score,
                          uml_score, natürlichsprachig_score)
    b = bedeutung_messen(stab_score, matrix_score, pflichtenheft_dokumentieren_score,
                     projektstrukturplan_score, tshirt_score, kreativitaetstechnik_score,
                     reine_po_score, formale_score, uml_score, natürlichsprachig_score)
    v = verteilung_messen(beobachtungstechnik_score, natürlichsprachig_score, phasen_vorgehen, agiles_vorgehen)
    t = technologielevel_messen(kreativitaetstechnik_score, initialer_product_backlog_score, product_backlog_dokumentieren_score,
                            product_backlog_planen_score, algorithmisch_score, tshirt_score,
                            product_backlog_termine_score, gantt_fortschritt_score, meilensteintrend_score,
                            reine_po_score, stab_score, matrix_score,
                            lastenheft_score, pflichtenheft_dokumentieren_score, netzplan_score,
                            eva_score, projektstrukturplan_score, phasen_vorgehen,
                            agiles_vorgehen)
    pt = projekttyp_messen(kreativitaetstechnik_score, product_backlog_planen_score, initialer_product_backlog_score,
                      gantt_fortschritt_score, burndown_score, sprint_review_score,
                      befragungstechnik_score, lastenheft_score, projektstrukturplan_score,
                      algorithmisch_score, netzplan_score, eva_score,
                      meilensteintrend_score)

    beobachtungstechnik_score = z[8] + q[0] + pd[1] + e[0] + er[0] + v[0]
    befragungstechnik_score = z[7] + k[0] + pd[0] + ka[0] + pt[6]
    kreativitaetstechnik_score = k[1] + ka[5] + b[5] + t[0] + pt[0]

    kundenanforderungen_erheben = {"Beobachtungstechnik": beobachtungstechnik_score,
                                   "Befragungstechnik": befragungstechnik_score,
                                   "Kreativitätstechnik": kreativitaetstechnik_score}

    return max(kundenanforderungen_erheben, key=kundenanforderungen_erheben.get)



#Kundenanforderungen festhalten
initialer_product_backlog_score = 0 #z[8]
lastenheft_score = 0

def kundenanforderungen_festhalten_funktion(initialer_product_backlog_score, lastenheft_score):
    z = zeitkritikalitaet_messen(ahp_score, bubble_sort_score, cv_score,
                                 numeral_assignment_score, hcv_score, msp_score,
                                 beobachtungstechnik_score, befragungstechnik_score, initialer_product_backlog_score,
                                 stab_score, reine_po_score, matrix_score,
                                 burndown_score, netzplan_score, product_backlog_termine_score,
                                 gantt_termine_score, phasen_vorgehen, agiles_vorgehen)
    ka = klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score,
                                       projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score,
                                       initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score,
                                       burndown_score, eva_score, meilensteintrend_score, phasen_vorgehen,
                                       agiles_vorgehen)
    t = technologielevel_messen(kreativitaetstechnik_score, initialer_product_backlog_score, product_backlog_dokumentieren_score,
                                product_backlog_planen_score, algorithmisch_score, tshirt_score,
                                product_backlog_termine_score, gantt_fortschritt_score, meilensteintrend_score,
                                reine_po_score, stab_score, matrix_score,
                                lastenheft_score, pflichtenheft_dokumentieren_score, netzplan_score,
                                eva_score, projektstrukturplan_score, phasen_vorgehen,
                                agiles_vorgehen)
    pt = projekttyp_messen(kreativitaetstechnik_score, product_backlog_planen_score, initialer_product_backlog_score,
                           gantt_fortschritt_score, burndown_score, sprint_review_score,
                           befragungstechnik_score, lastenheft_score, projektstrukturplan_score,
                           algorithmisch_score, netzplan_score, eva_score,
                           meilensteintrend_score)
    initialer_product_backlog_score = z[8] + ka[6] + t[1] + pt[2]
    lastenheft_score = ka[1] + t[12] + pt[2]

    kundenanforderungen_festhalten = {"Initialer Product Backlog": initialer_product_backlog_score,
                                      "Lastenheft": lastenheft_score}

    return max(kundenanforderungen_festhalten, key=kundenanforderungen_festhalten.get)


#PM-Prozess festlegen
phasen_vorgehen = 0
agiles_vorgehen = 0

def pm_prozess_festlegen_methode(phasen_vorgehen, agiles_vorgehen):
    s = stabilitaet_messen(projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score,
                           product_backlog_planen_score, burndown_score, meilensteintrend_score,
                           product_backlog_termine_score, phasen_vorgehen, agiles_vorgehen)
    v = verteilung_messen(beobachtungstechnik_score, natürlichsprachig_score, phasen_vorgehen, agiles_vorgehen)
    ka = klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score,
                                       projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score,
                                       initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score,
                                       burndown_score, eva_score, meilensteintrend_score,
                                       phasen_vorgehen, agiles_vorgehen)
    k = komplexitaet_messen(befragungstechnik_score, kreativitaetstechnik_score, matrix_score,
                            stab_score, reine_po_score, pflichtenheft_dokumentieren_score,
                            projektstrukturplan_score, netzplan_score, formale_score,
                            uml_score, natürlichsprachig_score, product_backlog_termine_score,
                            gantt_termine_score, phasen_vorgehen, agiles_vorgehen)
    tg = teamgroeße(product_backlog_planen_score, projektstrukturplan_score, phasen_vorgehen,
                    agiles_vorgehen)
    z = zeitkritikalitaet_messen(ahp_score, bubble_sort_score, cv_score,
                                 numeral_assignment_score, hcv_score, msp_score,
                                 beobachtungstechnik_score, befragungstechnik_score, initialer_product_backlog_score,
                                 stab_score, reine_po_score, matrix_score,
                                 burndown_score, netzplan_score, product_backlog_termine_score,
                                 gantt_termine_score, phasen_vorgehen, agiles_vorgehen)
    t = technologielevel_messen(kreativitaetstechnik_score, initialer_product_backlog_score, product_backlog_dokumentieren_score,
                                product_backlog_planen_score, algorithmisch_score, tshirt_score,
                                product_backlog_termine_score, gantt_fortschritt_score, meilensteintrend_score,
                                reine_po_score, stab_score, matrix_score,
                                lastenheft_score, pflichtenheft_dokumentieren_score, netzplan_score,
                                eva_score, projektstrukturplan_score, phasen_vorgehen,
                                agiles_vorgehen)
    phasen_vorgehen = s[7] + v[2] + ka[12] + k[13] + tg[2] + z[16] + t[17]
    agiles_vorgehen = s[8] + v[3] + ka[13] + k[14] + tg[3] + z[17] + t[18]

    pm_prozess_festlegen = {"Phasenmodell": phasen_vorgehen,
                            "Agiles Vorgehen": agiles_vorgehen}

    return max(pm_prozess_festlegen, key=pm_prozess_festlegen.get)


#Organisation festlegen
matrix_score = 0
stab_score = 0
reine_po_score = 0


def organisation_festlegen_methode(matrix_score, reine_po_score, stab_score):
    p = projektgroeße(ahp_score, bubble_sort_score, stab_score,
                      product_backlog_planen_score, cv_score, numeral_assignment_score,
                      matrix_score, projektstrukturplan_score, hcv_score,
                      msp_score, reine_po_score, netzplan_score,
                      gantt_termine_score)
    z = zeitkritikalitaet_messen(ahp_score, bubble_sort_score, cv_score,
                                 numeral_assignment_score, hcv_score, msp_score,
                                 beobachtungstechnik_score, befragungstechnik_score, initialer_product_backlog_score,
                                 stab_score, reine_po_score, matrix_score,
                                 burndown_score, netzplan_score, product_backlog_termine_score,
                                 gantt_termine_score, phasen_vorgehen, agiles_vorgehen)
    k = komplexitaet_messen(befragungstechnik_score, kreativitaetstechnik_score, matrix_score,
                            stab_score, reine_po_score, pflichtenheft_dokumentieren_score,
                            projektstrukturplan_score, netzplan_score, formale_score,
                            uml_score, natürlichsprachig_score, product_backlog_termine_score,
                            gantt_termine_score, phasen_vorgehen, agiles_vorgehen)
    q = qualifikation_messen(beobachtungstechnik_score, matrix_score, stab_score,
                             reine_po_score, experten_score, algorithmisch_score,
                             formale_score, uml_score, natürlichsprachig_score,
                             netzplan_score, product_backlog_termine_score, gantt_termine_score)
    pd = projektdauer_messen(befragungstechnik_score, beobachtungstechnik_score, stab_score,
                             matrix_score, reine_po_score, planning_poker_score,
                             netzplan_score, product_backlog_termine_score, gantt_termine_score)
    e = einsatz_messen(beobachtungstechnik_score, stab_score, reine_po_score, matrix_score)
    er = erfahrung_messen(beobachtungstechnik_score, reine_po_score, matrix_score,
                          stab_score, experten_score, formale_score,
                          uml_score, natürlichsprachig_score)
    b = bedeutung_messen(stab_score, matrix_score, pflichtenheft_dokumentieren_score,
                     projektstrukturplan_score, tshirt_score, kreativitaetstechnik_score,
                     reine_po_score, formale_score, uml_score, natürlichsprachig_score)
    t = technologielevel_messen(kreativitaetstechnik_score, initialer_product_backlog_score, product_backlog_dokumentieren_score,
                                product_backlog_planen_score, algorithmisch_score, tshirt_score,
                                product_backlog_termine_score, gantt_fortschritt_score, meilensteintrend_score,
                                reine_po_score, stab_score, matrix_score,
                                lastenheft_score, pflichtenheft_dokumentieren_score, netzplan_score,
                                eva_score, projektstrukturplan_score, phasen_vorgehen,
                                agiles_vorgehen)
    matrix_score = p[6] + z[11] + k[2] + q[1] + pd[3] + e[3] + er[2] + b[1] + t[11]
    reine_po_score = p[10] + z[10] + k[4] + q[3] + pd[4] + e[2] + er[1] + b[6] + t[9]
    stab_score = p[2] + z[9] + k[3] + q[2] + pd[2] + e[1] + er[3] + b[0] + t[10]

    organisation_festlegen = {"Matrix Projektorganisation": matrix_score,
                              "Staborganisation": stab_score,
                              "Reine Projektorganisation": reine_po_score}

    return max(organisation_festlegen, key=organisation_festlegen.get)


#Rollen definieren

#Anforderungsspezifikation
formale_score = 0
uml_score = 0
natürlichsprachig_score = 0

def anforderungsspezifikation_methode(formale_score, uml_score, natürlichsprachig_score):
    k = komplexitaet_messen(befragungstechnik_score, kreativitaetstechnik_score, matrix_score,
                            stab_score, reine_po_score, pflichtenheft_dokumentieren_score,
                            projektstrukturplan_score, netzplan_score, formale_score,
                            uml_score, natürlichsprachig_score, product_backlog_termine_score,
                            gantt_termine_score, phasen_vorgehen, agiles_vorgehen)
    q = qualifikation_messen(beobachtungstechnik_score, matrix_score, stab_score,
                             reine_po_score, experten_score, algorithmisch_score,
                             formale_score, uml_score, natürlichsprachig_score,
                             netzplan_score, product_backlog_termine_score, gantt_termine_score)
    er = erfahrung_messen(beobachtungstechnik_score, reine_po_score, matrix_score,
                          stab_score, experten_score, formale_score,
                          uml_score, natürlichsprachig_score)
    b = bedeutung_messen(stab_score, matrix_score, pflichtenheft_dokumentieren_score,
                     projektstrukturplan_score, tshirt_score, kreativitaetstechnik_score,
                     reine_po_score, formale_score, uml_score, natürlichsprachig_score)
    v = verteilung_messen(beobachtungstechnik_score, natürlichsprachig_score, phasen_vorgehen, agiles_vorgehen)
    formale_score = k[8] + q[6] + er[5] + b[7]
    uml_score = k[9] + q[7] + er[6] + b[8]
    natürlichsprachig_score = k[10] + q[8] + er[7] + b[9] + v[1]

    anforderungsspezifikation = {"Formale Spezifikation": formale_score,
                              "Grafische Spezifikation mit UML": uml_score,
                              "Natürlichsprachige Spezifikation mit Sprachschablonen": natürlichsprachig_score}

    return max(anforderungsspezifikation, key=anforderungsspezifikation.get)



#Anforderungen Priorisieren
bubble_sort_score = 0
numeral_assignment_score = 0
ahp_score = 0
cv_score = 0
msp_score = 0
hcv_score = 0

def anforderungen_priorisieren(ahp_score, cv_score, bubble_sort_score, numeral_assignment_score,hcv_score, msp_score):
    p = projektgroeße(ahp_score, bubble_sort_score, stab_score,
                      product_backlog_planen_score, cv_score, numeral_assignment_score,
                      matrix_score, projektstrukturplan_score, hcv_score,
                      msp_score, reine_po_score, netzplan_score,
                      gantt_termine_score)
    z = zeitkritikalitaet_messen(ahp_score, bubble_sort_score, cv_score,
                                 numeral_assignment_score, hcv_score, msp_score,
                                 beobachtungstechnik_score, befragungstechnik_score, initialer_product_backlog_score,
                                 stab_score, reine_po_score, matrix_score,
                                 burndown_score, netzplan_score, product_backlog_termine_score,
                                 gantt_termine_score, phasen_vorgehen, agiles_vorgehen)
    ahp_score = p[0] + z[0]
    bubble_sort_score = p[1] + z[1]
    cv_score = p[5] + z[3]
    numeral_assignment_score = p[6] + z[4]
    hcv_score = p[9] + z[5]
    msp_score = p[10] + z[6]
    anforderungen_priorisieren = {
        "Analytical Hierarchy Process" : ahp_score,
        "Cumulative Voting" : cv_score,
        "Bubble sort" : bubble_sort_score,
        "Minimal spanning tree" : msp_score,
        "Numeral assignment" : numeral_assignment_score,
        "Hierarchical cumulative voting" : hcv_score}
    return max(anforderungen_priorisieren, key=anforderungen_priorisieren.get)


#Anforderungen dokumentieren
pflichtenheft_dokumentieren_score = 0
product_backlog_dokumentieren_score = 0

def anforderungen_dokumentieren_methode(pflichtenheft_dokumentieren_score, product_backlog_dokumentieren_score):
    k = komplexitaet_messen(befragungstechnik_score, kreativitaetstechnik_score, matrix_score,
                            stab_score, reine_po_score, pflichtenheft_dokumentieren_score,
                            projektstrukturplan_score, netzplan_score, formale_score,
                            uml_score, natürlichsprachig_score, product_backlog_termine_score,
                            gantt_termine_score, phasen_vorgehen, agiles_vorgehen)
    ka = klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score,
                                       projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score,
                                       initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score,
                                       burndown_score, eva_score, meilensteintrend_score, phasen_vorgehen,
                                       agiles_vorgehen)
    b = bedeutung_messen(stab_score, matrix_score, pflichtenheft_dokumentieren_score,
                     projektstrukturplan_score, tshirt_score, kreativitaetstechnik_score,
                     reine_po_score, formale_score, uml_score, natürlichsprachig_score)
    s = stabilitaet_messen(projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score,
                           product_backlog_planen_score, burndown_score, meilensteintrend_score,
                           product_backlog_termine_score, phasen_vorgehen, agiles_vorgehen)
    t = technologielevel_messen(kreativitaetstechnik_score, initialer_product_backlog_score, product_backlog_dokumentieren_score,
                                product_backlog_planen_score, algorithmisch_score, tshirt_score,
                                product_backlog_termine_score, gantt_fortschritt_score, meilensteintrend_score,
                                reine_po_score, stab_score, matrix_score,
                                lastenheft_score, pflichtenheft_dokumentieren_score, netzplan_score,
                                eva_score, projektstrukturplan_score, phasen_vorgehen,
                                agiles_vorgehen)
    pflichtenheft_dokumentieren_score = k[5] + ka[2] + b[2] + t[13]
    product_backlog_dokumentieren_score = ka[7] + s[1] + t[2]

    anforderungen_dokumentieren = {"Pflichtenheft": pflichtenheft_dokumentieren_score,
                                   "Product Backlog": product_backlog_dokumentieren_score}

    return max(anforderungen_dokumentieren, key=anforderungen_dokumentieren.get)

#Phasen und Meilensteine festlegen

#Inhalte planen
product_backlog_planen_score = 0 #p[3]
projektstrukturplan_score = 0

def inhalte_planen_methode(product_backlog_planen_score, projektstrukturplan_score):
    k = komplexitaet_messen(befragungstechnik_score, kreativitaetstechnik_score, matrix_score,
                            stab_score, reine_po_score, pflichtenheft_dokumentieren_score,
                            projektstrukturplan_score, netzplan_score, formale_score,
                            uml_score, natürlichsprachig_score, product_backlog_termine_score,
                            gantt_termine_score, phasen_vorgehen, agiles_vorgehen)
    p = projektgroeße(ahp_score, bubble_sort_score, stab_score,
                      product_backlog_planen_score, cv_score, numeral_assignment_score,
                      matrix_score, projektstrukturplan_score, hcv_score,
                      msp_score, reine_po_score, netzplan_score,
                      gantt_termine_score)
    ka = klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score,
                                       projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score,
                                       initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score,
                                       burndown_score, eva_score, meilensteintrend_score, phasen_vorgehen,
                                       agiles_vorgehen)
    b = bedeutung_messen(stab_score, matrix_score, pflichtenheft_dokumentieren_score,
                     projektstrukturplan_score, tshirt_score, kreativitaetstechnik_score,
                     reine_po_score, formale_score, uml_score, natürlichsprachig_score)
    s = stabilitaet_messen(projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score,
                           product_backlog_planen_score, burndown_score, meilensteintrend_score,
                           product_backlog_termine_score, phasen_vorgehen, agiles_vorgehen)
    t = technologielevel_messen(kreativitaetstechnik_score, initialer_product_backlog_score, product_backlog_dokumentieren_score,
                                product_backlog_planen_score, algorithmisch_score, tshirt_score,
                                product_backlog_termine_score, gantt_fortschritt_score, meilensteintrend_score,
                                reine_po_score, stab_score, matrix_score,
                                lastenheft_score, pflichtenheft_dokumentieren_score, netzplan_score,
                                eva_score, projektstrukturplan_score, phasen_vorgehen,
                                agiles_vorgehen)
    pt = projekttyp_messen(kreativitaetstechnik_score, product_backlog_planen_score, initialer_product_backlog_score,
                           gantt_fortschritt_score, burndown_score, sprint_review_score,
                           befragungstechnik_score, lastenheft_score, projektstrukturplan_score,
                           algorithmisch_score, netzplan_score, eva_score,
                           meilensteintrend_score)
    tg = teamgroeße(product_backlog_planen_score, projektstrukturplan_score, phasen_vorgehen,
                    agiles_vorgehen)
    product_backlog_planen_score = p[3] + s[3] + t[3] + pt[1] + tg[0]
    projektstrukturplan_score = k[6] + ka[3] + b[3] + s[0] + t[16] + pt[8] + tg[1]

    inhalte_planen = {"Projektstrukturplan": projektstrukturplan_score,
                      "Product Backlog": product_backlog_planen_score}

    return max(inhalte_planen, key=inhalte_planen.get)


#Aufwände schätzen
experten_score = 0
algorithmisch_score = 0
tshirt_score = 0
planning_poker_score = 0

def aufwaende_schaetzen_methode(experten_score, algorithmisch_score, tshirt_score, planning_poker_score):
    q = qualifikation_messen(beobachtungstechnik_score, matrix_score, stab_score,
                             reine_po_score, experten_score, algorithmisch_score,
                             formale_score, uml_score, natürlichsprachig_score,
                             netzplan_score, product_backlog_termine_score, gantt_termine_score)
    pd = projektdauer_messen(befragungstechnik_score, beobachtungstechnik_score, stab_score,
                             matrix_score, reine_po_score, planning_poker_score,
                             netzplan_score, product_backlog_termine_score, gantt_termine_score)
    ka = klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score,
                                       projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score,
                                       initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score,
                                       burndown_score, eva_score, meilensteintrend_score, phasen_vorgehen,
                                       agiles_vorgehen)
    er = erfahrung_messen(beobachtungstechnik_score, reine_po_score, matrix_score,
                          stab_score, experten_score, formale_score,
                          uml_score, natürlichsprachig_score)
    b = bedeutung_messen(stab_score, matrix_score, pflichtenheft_dokumentieren_score,
                     projektstrukturplan_score, tshirt_score, kreativitaetstechnik_score,
                     reine_po_score, formale_score, uml_score, natürlichsprachig_score)
    s = stabilitaet_messen(projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score,
                           product_backlog_planen_score, burndown_score, meilensteintrend_score,
                           product_backlog_termine_score, phasen_vorgehen, agiles_vorgehen)
    t = technologielevel_messen(kreativitaetstechnik_score, initialer_product_backlog_score, product_backlog_dokumentieren_score,
                                product_backlog_planen_score, algorithmisch_score, tshirt_score,
                                product_backlog_termine_score, gantt_fortschritt_score, meilensteintrend_score,
                                reine_po_score, stab_score, matrix_score,
                                lastenheft_score, pflichtenheft_dokumentieren_score, netzplan_score,
                                eva_score, projektstrukturplan_score, phasen_vorgehen,
                                agiles_vorgehen)
    pt = projekttyp_messen(kreativitaetstechnik_score, product_backlog_planen_score, initialer_product_backlog_score,
                           gantt_fortschritt_score, burndown_score, sprint_review_score,
                           befragungstechnik_score, lastenheft_score, projektstrukturplan_score,
                           algorithmisch_score, netzplan_score, eva_score,
                           meilensteintrend_score)
    experten_score = q[4] + er[4]
    algorithmisch_score = q[5] + t[4] + pt[9]
    tshirt_score = ka[8] + b[4] + s[2] + t[5]
    planning_poker_score = pd[5]

    aufwaende_schaetzen = {"Expertenschätzung": experten_score,
                           "Algorithmische Schätzung" : algorithmisch_score,
                           "T-Shirt Sizing" : tshirt_score,
                           "Planning Poker" : planning_poker_score}

    return max(aufwaende_schaetzen, key=aufwaende_schaetzen.get)

#Termine planen
gantt_termine_score = 0
netzplan_score = 0
product_backlog_termine_score = 0

def termine_planen_methode(gantt_termine_score, netzplan_score, product_backlog_termine_score):
    k = komplexitaet_messen(befragungstechnik_score, kreativitaetstechnik_score, matrix_score,
                            stab_score, reine_po_score, pflichtenheft_dokumentieren_score,
                            projektstrukturplan_score, netzplan_score, formale_score,
                            uml_score, natürlichsprachig_score, product_backlog_termine_score,
                            gantt_termine_score, phasen_vorgehen, agiles_vorgehen)
    s = stabilitaet_messen(projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score,
                           product_backlog_planen_score, burndown_score, meilensteintrend_score,
                           product_backlog_termine_score, phasen_vorgehen, agiles_vorgehen)
    p = projektgroeße(ahp_score, bubble_sort_score, stab_score,
                      product_backlog_planen_score, cv_score, numeral_assignment_score,
                      matrix_score, projektstrukturplan_score, hcv_score,
                      msp_score, reine_po_score, netzplan_score,
                      gantt_termine_score)
    q = qualifikation_messen(beobachtungstechnik_score, matrix_score, stab_score,
                             reine_po_score, experten_score, algorithmisch_score,
                             formale_score, uml_score, natürlichsprachig_score,
                             netzplan_score, product_backlog_termine_score, gantt_termine_score)
    z = zeitkritikalitaet_messen(ahp_score, bubble_sort_score, cv_score,
                                 numeral_assignment_score, hcv_score, msp_score,
                                 beobachtungstechnik_score, befragungstechnik_score, initialer_product_backlog_score,
                                 stab_score, reine_po_score, matrix_score,
                                 burndown_score, netzplan_score, product_backlog_termine_score,
                                 gantt_termine_score, phasen_vorgehen, agiles_vorgehen)
    pd = projektdauer_messen(befragungstechnik_score, beobachtungstechnik_score, stab_score,
                             matrix_score, reine_po_score, planning_poker_score,
                             netzplan_score, product_backlog_termine_score, gantt_termine_score)
    t = technologielevel_messen(kreativitaetstechnik_score, initialer_product_backlog_score, product_backlog_dokumentieren_score,
                                product_backlog_planen_score, algorithmisch_score, tshirt_score,
                                product_backlog_termine_score, gantt_fortschritt_score, meilensteintrend_score,
                                reine_po_score, stab_score, matrix_score,
                                lastenheft_score, pflichtenheft_dokumentieren_score, netzplan_score,
                                eva_score, projektstrukturplan_score, phasen_vorgehen,
                                agiles_vorgehen)
    pt = projekttyp_messen(kreativitaetstechnik_score, product_backlog_planen_score, initialer_product_backlog_score,
                           gantt_fortschritt_score, burndown_score, sprint_review_score,
                           befragungstechnik_score, lastenheft_score, projektstrukturplan_score,
                           algorithmisch_score, netzplan_score, eva_score,
                           meilensteintrend_score)
    netzplan_score = k[7] + p[11] + q[9] + z[13] + pd[6] + t[12] + pt[10]
    product_backlog_termine_score = s[6] + k[11]+ q[10] + z[14] + pd[7] + t[6]
    gantt_termine_score = p[12] +k[12]+ q[11] + z[15] + pd[8]

    termine_planen = {"Netzpläne": netzplan_score,
                      "Product Backlog": product_backlog_termine_score,
                      "Gantt Diagramm" : gantt_termine_score}

    return max(termine_planen, key=termine_planen.get)

#Iterative Detailplanung
sprint_backlog_score = 0
'''??'''

#Prozessmodell für Systementwicklung festlegen
agil_score = 0
klassisch_score = 0

#Fortschritt bestimmen
burndown_score = 0
gantt_fortschritt_score = 0
def fortschritt_bestimmen_methode(burndown_score, gantt_fortschritt_score):
    ka = klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score,
                                       projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score,
                                       initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score,
                                       burndown_score, eva_score, meilensteintrend_score, phasen_vorgehen,
                                       agiles_vorgehen)
    s = stabilitaet_messen(projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score,
                           product_backlog_planen_score, burndown_score, meilensteintrend_score,
                           product_backlog_termine_score, phasen_vorgehen, agiles_vorgehen)
    t = technologielevel_messen(kreativitaetstechnik_score, initialer_product_backlog_score, product_backlog_dokumentieren_score,
                                product_backlog_planen_score, algorithmisch_score, tshirt_score,
                                product_backlog_termine_score, gantt_fortschritt_score, meilensteintrend_score,
                                reine_po_score, stab_score, matrix_score,
                                lastenheft_score, pflichtenheft_dokumentieren_score, netzplan_score,
                                eva_score, projektstrukturplan_score, phasen_vorgehen,
                                agiles_vorgehen)
    pt = projekttyp_messen(kreativitaetstechnik_score, product_backlog_planen_score, initialer_product_backlog_score,
                           gantt_fortschritt_score, burndown_score, sprint_review_score,
                           befragungstechnik_score, lastenheft_score, projektstrukturplan_score,
                           algorithmisch_score, netzplan_score, eva_score,
                           meilensteintrend_score)
    burndown_score = ka[9] + s[4] + pt[4]
    gantt_fortschritt_score = ka[4] + t[7] + pt[3]

    fortschritt_bestimmen = {"Burndown Chart": burndown_score,
                             "Gantt Diagramm": gantt_fortschritt_score}

    return max(fortschritt_bestimmen, key=fortschritt_bestimmen.get)

#Fortschritt analysieren
sprint_review_score = 0
eva_score = 0
meilensteintrend_score = 0

def fortschritt_analysieren_methode(sprint_review_score, eva_score, meilensteintrend_score):
    ka = klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score,
                                       projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score,
                                       initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score,
                                       burndown_score, eva_score, meilensteintrend_score, phasen_vorgehen,
                                       agiles_vorgehen)
    s = stabilitaet_messen(projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score,
                           product_backlog_planen_score, burndown_score, meilensteintrend_score,
                           product_backlog_termine_score, phasen_vorgehen, agiles_vorgehen)
    t = technologielevel_messen(kreativitaetstechnik_score, initialer_product_backlog_score, product_backlog_dokumentieren_score,
                                product_backlog_planen_score, algorithmisch_score, tshirt_score,
                                product_backlog_termine_score, gantt_fortschritt_score, meilensteintrend_score,
                                reine_po_score, stab_score, matrix_score,
                                lastenheft_score, pflichtenheft_dokumentieren_score, netzplan_score,
                                eva_score, projektstrukturplan_score, phasen_vorgehen,
                                agiles_vorgehen)
    pt = projekttyp_messen(kreativitaetstechnik_score, product_backlog_planen_score, initialer_product_backlog_score,
                           gantt_fortschritt_score, burndown_score, sprint_review_score,
                           befragungstechnik_score, lastenheft_score, projektstrukturplan_score,
                           algorithmisch_score, netzplan_score, eva_score,
                           meilensteintrend_score)
    sprint_review_score = pt[5]
    eva_score = ka[10] + t[15] + pt[11]
    meilensteintrend_score = ka[11] + s[5] + t[8] + pt[12]

    fortschritt_analysieren = {"Sprint Review": sprint_review_score,
                             "Earned Value Analyse" : eva_score,
                             "Meilensteintrendanalyse" : meilensteintrend_score}

    return max(fortschritt_analysieren, key=fortschritt_analysieren.get)

""" ---------------------------------------------------------------- KRITERIEN ---------------------------------------------------------------- """
# Kriterium Stabilität der Anforderungen
def stabilitaet_messen(projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score, product_backlog_planen_score, burndown_score, meilensteintrend_score, product_backlog_termine_score, phasen_vorgehen, agiles_vorgehen):
    stabilitaet = request.form["Stabilität der Anforderungen"]
    if stabilitaet == "Stabil":
        projektstrukturplan_score += 1
        phasen_vorgehen += 1
    if stabilitaet == "Volatil":
        product_backlog_dokumentieren_score += 1
        tshirt_score += 1
        product_backlog_planen_score += 1
        burndown_score += 1
        meilensteintrend_score += 1
        product_backlog_termine_score += 1
        agiles_vorgehen += 1
    return [projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score,
            product_backlog_planen_score, burndown_score, meilensteintrend_score,
            product_backlog_termine_score, phasen_vorgehen, agiles_vorgehen]
#Kriterium Verteilung der Projektbeteiligten
def verteilung_messen(beobachtungstechnik_score, natürlichsprachig_score, phasen_vorgehen, agiles_vorgehen):
    verteilung = request.form["Verteilung der Projektbeteiligten"]
    if verteilung == "Zentral":
        agiles_vorgehen
    if verteilung == "Dezentral":
        beobachtungstechnik_score -= 1
        natürlichsprachig_score += 1
        phasen_vorgehen
    return [beobachtungstechnik_score, natürlichsprachig_score, phasen_vorgehen, agiles_vorgehen]
#Kriterium Bedeutung für das Unternehmen
def bedeutung_messen(stab_score, matrix_score, pflichtenheft_dokumentieren_score, projektstrukturplan_score, tshirt_score, kreativitaetstechnik_score, reine_po_score, formale_score, uml_score, natürlichsprachig_score):
    bedeutung = request.form["Bedeutung für das Unternehmen"]
    if bedeutung == "Gering":
        stab_score += 1
    if bedeutung == "Groß":
        matrix_score += 1
        pflichtenheft_dokumentieren_score += 1
        projektstrukturplan_score += 1
        tshirt_score -= 1
    if bedeutung == "Sehr Groß":
        kreativitaetstechnik_score += 1
        reine_po_score += 1
        pflichtenheft_dokumentieren_score += 1
        projektstrukturplan_score += 1
        tshirt_score -= 1
        formale_score -= 1
        natürlichsprachig_score += 1
        uml_score += 1
    return [stab_score, matrix_score, pflichtenheft_dokumentieren_score,
            projektstrukturplan_score, tshirt_score, kreativitaetstechnik_score,
            reine_po_score, formale_score, uml_score, natürlichsprachig_score]
#Kriterium Höchste Erfahrungsstufe im Team
def erfahrung_messen(beobachtungstechnik_score, reine_po_score, matrix_score, stab_score, experten_score, formale_score, uml_score, natürlichsprachig_score):
    erfahrung = request.form["Höchste Erfahrungsstufe im Team"]
    if erfahrung == "0 Jahre":
        beobachtungstechnik_score -= 1
        reine_po_score += 1
        natürlichsprachig_score += 1
        formale_score -= 1
    if erfahrung == "1,5+ Jahre":
        beobachtungstechnik_score -= 1
        matrix_score += 1
        uml_score += 1
        formale_score -= 1
    if erfahrung == "4+ Jahre":
        matrix_score += 1
        uml_score += 1
        formale_score -= 1
    if erfahrung == "7+ Jahre":
        stab_score += 1
        experten_score += 1
        uml_score += 1
        formale_score -= 1
    if erfahrung == "10+ Jahre":
        stab_score += 1
        experten_score += 1
        uml_score += 1
        formale_score -= 1
    if erfahrung == "15+ Jahre":
        stab_score += 1
        experten_score += 1
        uml_score += 1
        formale_score += 1
    return [beobachtungstechnik_score, reine_po_score, matrix_score,
            stab_score, experten_score, formale_score,
            uml_score, natürlichsprachig_score]
#Kriterium Einsatz(-zeit)
def einsatz_messen(beobachtungstechnik_score,stab_score, reine_po_score, matrix_score):
    einsatz = request.form["Einsatzzeit der Mitarbeiter"]
    if einsatz == "Nebenamtlich":
        beobachtungstechnik_score -= 1
        stab_score += 1
    if einsatz == "Hauptamtlich":
        reine_po_score += 1
        beobachtungstechnik_score += 1
    if einsatz == "Teilzeit":
        beobachtungstechnik_score -= 1
        matrix_score += 1
    return [beobachtungstechnik_score, stab_score, reine_po_score, matrix_score]
#Kriterium Klarheit der Anforderungen
def klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score, projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score, initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score, burndown_score, eva_score, meilensteintrend_score, phasen_vorgehen, agiles_vorgehen):
    klarheit_anforderungen = request.form["Klarheit der Anforderungen"]
    if klarheit_anforderungen == "Klar":
        befragungstechnik_score +=1
        lastenheft_score +=1
        pflichtenheft_dokumentieren_score +=1
        projektstrukturplan_score +=1
        gantt_fortschritt_score +=1
        phasen_vorgehen += 1
    if klarheit_anforderungen == "Unklar":
        kreativitaetstechnik_score +=1
        initialer_product_backlog_score +=1
        product_backlog_dokumentieren_score +=1
        tshirt_score +=1
        burndown_score +=1
        eva_score -=1
        meilensteintrend_score -=1
        agiles_vorgehen += 1
    return [befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score,
            projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score,
            initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score,
            burndown_score, eva_score, meilensteintrend_score,
            phasen_vorgehen, agiles_vorgehen]

def projektdauer_messen(befragungstechnik_score, beobachtungstechnik_score, stab_score, matrix_score, reine_po_score, planning_poker_score, netzplan_score, product_backlog_termine_score, gantt_termine_score):
    projektdauer = request.form["Projektdauer"]
    if projektdauer == "Kurz":
        befragungstechnik_score -= 1
        beobachtungstechnik_score -= 1
        stab_score += 1
        product_backlog_termine_score += 1
        gantt_termine_score += 1
    if projektdauer == "Mittel":
        matrix_score += 1
        product_backlog_termine_score += 1
        gantt_termine_score += 1
    if projektdauer == "Lang":
        matrix_score += 1
        reine_po_score += 1
        planning_poker_score += 1
        netzplan_score += 1
    return [befragungstechnik_score, beobachtungstechnik_score, stab_score,
            matrix_score, reine_po_score, planning_poker_score,
            netzplan_score, product_backlog_termine_score, gantt_termine_score]
#Kriterium Qualifikation der Mitarbeiter
def qualifikation_messen(beobachtungstechnik_score, matrix_score, stab_score, reine_po_score, experten_score, algorithmisch_score, formale_score, uml_score, natürlichsprachig_score, netzplan_score, product_backlog_termine_score, gantt_termine_score):
    qualifikation = request.form["Qualifikation der Mitarbeiter"]
    if qualifikation == "Professionell":
        beobachtungstechnik_score += 1
        reine_po_score += 1
        experten_score += 1
        formale_score += 1
        netzplan_score += 1
        product_backlog_termine_score += 1
    if qualifikation == "Qualifiziert":
        beobachtungstechnik_score += 1
        matrix_score += 1
        uml_score += 1
        formale_score -= 1
        product_backlog_termine_score += 1
    if qualifikation == "Wenig qualifiziert":
        stab_score += 1
        algorithmisch_score += 1
        natürlichsprachig_score += 1
        formale_score -= 1
        gantt_termine_score += 1
        netzplan_score -= 1
    return [beobachtungstechnik_score, matrix_score, stab_score,
            reine_po_score, experten_score, algorithmisch_score,
            formale_score, uml_score, natürlichsprachig_score,
            netzplan_score, product_backlog_termine_score, gantt_termine_score]


#Kriterium Komplexität
def komplexitaet_messen(befragungstechnik_score, kreativitaetstechnik_score, matrix_score,stab_score, reine_po_score, pflichtenheft_dokumentieren_score,projektstrukturplan_score, netzplan_score, formale_score, uml_score ,natürlichsprachig_score, product_backlog_termine_score, gantt_termine_score, phasen_vorgehen, agiles_vorgehen):
    komplexitaet = request.form["Komplexität"]
    if komplexitaet == "Gering":
        stab_score += 1
        natürlichsprachig_score += 1
        formale_score -= 1
        gantt_termine_score += 1
        product_backlog_termine_score += 1
        phasen_vorgehen += 1
    if komplexitaet == "Mittel":
        matrix_score += 1
        gantt_termine_score += 1
    if komplexitaet == "Hoch":
        reine_po_score += 1
        kreativitaetstechnik_score += 1
        befragungstechnik_score += 1
        pflichtenheft_dokumentieren_score -= 1
        projektstrukturplan_score += 1
        netzplan_score += 1
        formale_score += 1
        natürlichsprachig_score -= 1
        uml_score += 1
        agiles_vorgehen += 1
    return [befragungstechnik_score, kreativitaetstechnik_score, matrix_score,
            stab_score, reine_po_score, pflichtenheft_dokumentieren_score,
            projektstrukturplan_score, netzplan_score, formale_score,
            uml_score ,natürlichsprachig_score, product_backlog_termine_score,
            gantt_termine_score, phasen_vorgehen, agiles_vorgehen]

#Kriterium Projektgröße
def projektgroeße(ahp_score, bubble_sort_score, stab_score, product_backlog_planen_score, cv_score, numeral_assignment_score, matrix_score, projektstrukturplan_score, hcv_score, msp_score, reine_po_score, netzplan_score, gantt_termine_score):
    projektgroeße = request.form["Projektgröße"]
    if projektgroeße == "Klein":
        ahp_score += 1
        cv_score += 1
        bubble_sort_score += 1
        stab_score += 1
        product_backlog_planen_score += 1
        gantt_termine_score += 1
    if projektgroeße == "Mittel":
        msp_score += 1
        cv_score += 1
        numeral_assignment_score += 1
        matrix_score += 1
        projektstrukturplan_score += 1
    if projektgroeße == "Groß":
        hcv_score += 1
        msp_score += 1
        reine_po_score += 1
        projektstrukturplan_score += 1
        netzplan_score += 1
    return [ahp_score, bubble_sort_score, stab_score,
            product_backlog_planen_score, cv_score, numeral_assignment_score,
            matrix_score, projektstrukturplan_score, hcv_score,
            msp_score, reine_po_score, netzplan_score,
            gantt_termine_score]

def teamgroeße(product_backlog_planen_score, projektstrukturplan_score, phasen_vorgehen, agiles_vorgehen):
    teamgroeße = request.form["Teamgröße"]
    if teamgroeße == "Klein":
        product_backlog_planen_score += 1
        agiles_vorgehen += 1
    if teamgroeße == "Mittel":
        product_backlog_planen_score += 1
    if teamgroeße == "Groß":
        projektstrukturplan_score += 1
        phasen_vorgehen += 1
    return [product_backlog_planen_score, projektstrukturplan_score, phasen_vorgehen,
            agiles_vorgehen]

def zeitkritikalitaet_messen(ahp_score, bubble_sort_score, cv_score, numeral_assignment_score, hcv_score, msp_score, beobachtungstechnik_score, befragungstechnik_score, initialer_product_backlog_score, stab_score, reine_po_score, matrix_score, burndown_score, netzplan_score, product_backlog_termine_score, gantt_termine_score, phasen_vorgehen, agiles_vorgehen):
    zeitkritikalitaet = request.form["Zeitkritikalität"]
    if zeitkritikalitaet == "Gering":
        ahp_score += 1
        befragungstechnik_score += 1
        beobachtungstechnik_score += 1
        stab_score += 1
        netzplan_score += 1
        phasen_vorgehen += 1
    if zeitkritikalitaet == "Mittel":
        numeral_assignment_score +=1
        bubble_sort_score +=1
        matrix_score += 1
        gantt_termine_score += 1
        agiles_vorgehen += 1
    if zeitkritikalitaet == "Hoch":
        msp_score += 1
        cv_score += 1
        hcv_score += 1
        befragungstechnik_score -= 1
        beobachtungstechnik_score -= 1
        initialer_product_backlog_score += 1
        reine_po_score += 1
        burndown_score += 1
        netzplan_score -= 1
        product_backlog_termine_score += 1
        agiles_vorgehen += 1
    return [ahp_score, bubble_sort_score, cv_score,
            numeral_assignment_score, hcv_score, msp_score,
            befragungstechnik_score, beobachtungstechnik_score, initialer_product_backlog_score,
            stab_score, reine_po_score, matrix_score,
            burndown_score, netzplan_score, product_backlog_termine_score,
            gantt_termine_score, phasen_vorgehen, agiles_vorgehen]


##new
def projekttyp_messen(kreativitaetstechnik_score, product_backlog_planen_score, initialer_product_backlog_score, gantt_fortschritt_score, burndown_score, sprint_review_score, befragungstechnik_score, lastenheft_score, projektstrukturplan_score, algorithmisch_score, netzplan_score, eva_score,meilensteintrend_score):
    projekttyp = request.form["Projekttyp"]
    if projekttyp == "Original Design":
        kreativitaetstechnik_score += 1
        initialer_product_backlog_score += 1
        product_backlog_planen_score += 1
        gantt_fortschritt_score -= 1
        burndown_score += 1
        sprint_review_score += 1
    if projekttyp == "Parametric Design":
        befragungstechnik_score += 1
        lastenheft_score += 1
        projektstrukturplan_score += 1
        algorithmisch_score += 1
        netzplan_score += 1
        gantt_fortschritt_score += 1
        eva_score += 1
        meilensteintrend_score += 1
    if projekttyp == "Configuration Design":
        befragungstechnik_score += 1
        lastenheft_score += 1
        projektstrukturplan_score += 1
        algorithmisch_score += 1
        netzplan_score += 1
        gantt_fortschritt_score += 1
        eva_score += 1
        meilensteintrend_score += 1
    if projekttyp == "Redesign Projekt":
        befragungstechnik_score += 1
        lastenheft_score += 1
        projektstrukturplan_score += 1
        algorithmisch_score += 1
        netzplan_score += 1
        gantt_fortschritt_score += 1
        eva_score += 1
        meilensteintrend_score += 1
    if projekttyp == "Selection Design":
        befragungstechnik_score += 1
        lastenheft_score += 1
        projektstrukturplan_score += 1
        algorithmisch_score += 1
        gantt_fortschritt_score += 1
        eva_score += 1
        meilensteintrend_score += 1

    return [kreativitaetstechnik_score, product_backlog_planen_score, initialer_product_backlog_score,
            gantt_fortschritt_score, burndown_score, sprint_review_score,
            befragungstechnik_score, lastenheft_score, projektstrukturplan_score,
            algorithmisch_score, netzplan_score, eva_score,
            meilensteintrend_score]

def technologielevel_messen(kreativitaetstechnik_score, initialer_product_backlog_score, product_backlog_dokumentieren_score, product_backlog_planen_score, algorithmisch_score, tshirt_score, product_backlog_termine_score, gantt_fortschritt_score, meilensteintrend_score, reine_po_score, stab_score, matrix_score,lastenheft_score, pflichtenheft_dokumentieren_score, netzplan_score, eva_score, projektstrukturplan_score, phasen_vorgehen, agiles_vorgehen):
    technologielevel = request.form["Technologielevel"]
    if technologielevel == "Neue Technologie":
        kreativitaetstechnik_score += 1
        initialer_product_backlog_score += 1
        product_backlog_dokumentieren_score += 1
        product_backlog_planen_score += 1
        algorithmisch_score -= 1
        tshirt_score += 1
        product_backlog_termine_score += 1
        gantt_fortschritt_score -= 1
        meilensteintrend_score += 1
        reine_po_score += 1
        agiles_vorgehen += 1
    if technologielevel == "Standardtechnologie":
        lastenheft_score += 1
        pflichtenheft_dokumentieren_score += 1
        algorithmisch_score += 1
        netzplan_score += 1
        gantt_fortschritt_score += 1
        eva_score += 1
        stab_score += 1
        phasen_vorgehen += 1
    if technologielevel == "Komplizierte Technologie":
        pflichtenheft_dokumentieren_score += 1
        projektstrukturplan_score += 1
        algorithmisch_score += 1
        netzplan_score += 1
        gantt_fortschritt_score += 1
        meilensteintrend_score += 1
        matrix_score += 1
        agiles_vorgehen += 1
    return [kreativitaetstechnik_score, initialer_product_backlog_score, product_backlog_dokumentieren_score,
            product_backlog_planen_score, algorithmisch_score, tshirt_score,
            product_backlog_termine_score, gantt_fortschritt_score, meilensteintrend_score,
            reine_po_score, stab_score, matrix_score,
            lastenheft_score, pflichtenheft_dokumentieren_score, netzplan_score,
            eva_score, projektstrukturplan_score, phasen_vorgehen,
            agiles_vorgehen]


''' ---------------------------------------------------------------- Einbinden HTML templates ---------------------------------------------------------------- '''
#Route nach Kriterienwahl
@app.route("/")
def home():
    return redirect("/kriterienwahl")


@app.route("/kriterienwahl", methods = ["POST","GET"])
def kriterienwahl():
    #Werte für Kriterien über POST bekommen
    if request.method == "POST":
        projektgroeße = request.form["Projektgröße"]
        teamgroeße = request.form["Teamgröße"]
        komplexitaet = request.form["Komplexität"]
        projektdauer = request.form["Projektdauer"]
        klarheit_anforderungen = request.form["Klarheit der Anforderungen"]
        einsatz = request.form["Einsatzzeit der Mitarbeiter"]
        erf = request.values.getlist("Höchste Erfahrungsstufe im Team")
        erfahrung = erf[0]
        bedeutung = request.form["Bedeutung für das Unternehmen"]
        zeitkritikalitaet = request.form["Zeitkritikalität"]
        verteilung = request.form["Verteilung der Projektbeteiligten"]
        stabilitaet = request.form["Stabilität der Anforderungen"]
        qualifikation = request.form["Qualifikation der Mitarbeiter"]
        technologielevel = request.form["Technologielevel"]
        projekttyp = request.form["Projekttyp"]

        #Methoden zum Berechnen der Vorgehensbausteine
        pm_prozess = pm_prozess_festlegen_methode(phasen_vorgehen, agiles_vorgehen)
        erheben = kundenanforderungen_erheben_funktion(beobachtungstechnik_score, kreativitaetstechnik_score,
                                                       befragungstechnik_score)
        organisation = organisation_festlegen_methode(matrix_score, reine_po_score, stab_score)
        priorisieren = anforderungen_priorisieren(ahp_score, cv_score, bubble_sort_score,
                                                  numeral_assignment_score, hcv_score, msp_score)
        t_planen = termine_planen_methode(gantt_termine_score, netzplan_score, product_backlog_termine_score)
        festhalten = kundenanforderungen_festhalten_funktion(initialer_product_backlog_score, lastenheft_score)
        dokumentieren = anforderungen_dokumentieren_methode(pflichtenheft_dokumentieren_score,
                                                            product_backlog_dokumentieren_score)
        i_planen = inhalte_planen_methode(product_backlog_planen_score, projektstrukturplan_score)
        schaetzen = aufwaende_schaetzen_methode(experten_score, algorithmisch_score, tshirt_score, planning_poker_score)
        bestimmen = fortschritt_bestimmen_methode(burndown_score, gantt_fortschritt_score)
        analysieren = fortschritt_analysieren_methode(sprint_review_score, eva_score, meilensteintrend_score)
        spezifikation = anforderungsspezifikation_methode(formale_score, uml_score, natürlichsprachig_score)

        #Werte für Vorgehensbausteine in vorgehensmodell Dictionnary einfügen
        vorgehensmodell = {"Kundenanforderungen erheben": erheben,
                           "Kundenanforderungen festhalten": festhalten,
                           "PM-Prozess wählen": pm_prozess,
                           "Organisation festlegen": organisation,
                           "Anforderungsspezifikation": spezifikation,
                           "Anforderungen priorisieren": priorisieren,
                           "Anforderungen dokumentieren": dokumentieren,
                           "Inhalte planen": i_planen,
                           "Aufwände schätzen": schaetzen,
                           "Termine planen": t_planen,
                           "Fortschritt bestimmen": bestimmen,
                           "Fortschritt analysieren": analysieren
                           }
        #Zu anzeige.html navigieren, ausgerechnete Werte für vorgehensmodell ausgeben
        return render_template("anzeige.html", komplexitaet=komplexitaet, projektgroeße=projektgroeße, teamgroeße=teamgroeße,
                               projektdauer=projektdauer, klarheit_anforderungen=klarheit_anforderungen,
                               einsatz=einsatz, erfahrung=erfahrung, bedeutung=bedeutung,
                               zeitkritikalitaet=zeitkritikalitaet, pm_prozess=pm_prozess,
                               verteilung=verteilung, stabilitaet=stabilitaet, qualifikation=qualifikation,
                               technologielevel=technologielevel, projekttyp=projekttyp, vorgehensmodell=vorgehensmodell)

    else:
        return render_template("kriterienwahl.html", kriterienauswahl=kriterienauswahl, beschreibung=beschreibung)

@app.route("/anzeige", methods = ["POST","GET"])
def anzeige():
    if request.method == "POST":
        projektgroeße = request.form["Projektgröße"]
        teamgroeße = request.form["Teamgröße"]
        komplexitaet = request.form["Komplexität"]
        projektdauer = request.form["Projektdauer"]
        klarheit_anforderungen = request.form["Klarheit der Anforderungen"]
        einsatz = request.form["Einsatzzeit der Mitarbeiter"]
        erfahrung = request.form["Höchste Erfahrungsstufe im Team"]
        bedeutung = request.form["Bedeutung für das Unternehmen"]
        zeitkritikalitaet = request.form["Zeitkritikalität"]
        verteilung = request.form["Verteilung der Projektbeteiligten"]
        stabilitaet = request.form["Stabilität der Anforderungen"]
        qualifikation = request.form["Qualifikation der Mitarbeiter"]
        technologielevel = request.form["Technologielevel"]
        projekttyp = request.form["Projekttyp"]

        pm_prozess = pm_prozess_festlegen_methode(phasen_vorgehen, agiles_vorgehen)
        erheben = kundenanforderungen_erheben_funktion(beobachtungstechnik_score, kreativitaetstechnik_score, befragungstechnik_score)
        organisation = organisation_festlegen_methode(matrix_score, reine_po_score, stab_score)
        priorisieren = anforderungen_priorisieren(ahp_score, cv_score, bubble_sort_score,
                                   numeral_assignment_score, hcv_score, msp_score)
        t_planen = termine_planen_methode(gantt_termine_score, netzplan_score, product_backlog_termine_score)
        festhalten = kundenanforderungen_festhalten_funktion(initialer_product_backlog_score, lastenheft_score)
        dokumentieren = anforderungen_dokumentieren_methode(pflichtenheft_dokumentieren_score, product_backlog_dokumentieren_score)
        i_planen = inhalte_planen_methode(product_backlog_planen_score, projektstrukturplan_score)
        schaetzen = aufwaende_schaetzen_methode(experten_score, algorithmisch_score, tshirt_score, planning_poker_score)
        bestimmen = fortschritt_bestimmen_methode(burndown_score, gantt_fortschritt_score)
        analysieren = fortschritt_analysieren_methode(sprint_review_score, eva_score, meilensteintrend_score)
        spezifikation = anforderungsspezifikation_methode(formale_score, uml_score, natürlichsprachig_score)

        vorgehensmodell = {"Kundenanforderungen erheben": erheben,
                           "Kundenanforderungen festhalten": festhalten,
                           "PM-Prozess wählen": pm_prozess,
                           "Organisation festlegen": organisation,
                           "Anforderungsspezifikation": spezifikation,
                           "Anforderungen priorisieren": priorisieren,
                           "Anforderungen dokumentieren": dokumentieren,
                           "Inhalte planen": i_planen,
                           "Aufwände schätzen": schaetzen,
                           "Termine planen": t_planen,
                           "Fortschritt bestimmen": bestimmen,
                           "Fortschritt analysieren": analysieren
                           }
        return render_template("anzeige.html", komplexitaet=komplexitaet, projektgroeße=projektgroeße, projektdauer=projektdauer, klarheit_anforderungen=klarheit_anforderungen,
                               einsatz=einsatz, erfahrung=erfahrung, bedeutung=bedeutung, zeitkritikalitaet=zeitkritikalitaet, teamgroeße=teamgroeße,
                               verteilung=verteilung, stabilitaet=stabilitaet, qualifikation=qualifikation, technologielevel=technologielevel, projekttyp=projekttyp, vorgehensmodell=vorgehensmodell)
    else:
        return render_template("anzeige.html")

@app.route("/Kreativitätstechnik", methods = ["POST","GET"])
def kreativitaetstechnik():

    return render_template("kreativitätstechnik.html")

@app.route("/Beobachtungstechnik", methods = ["POST","GET"])
def beobachtungstechnik():

    return render_template("beobachtungstechnik.html")

@app.route("/Befragungstechnik", methods = ["POST","GET"])
def befragungstechnik():

    return render_template("befragungstechnik.html")

@app.route("/Initialer_Product_Backlog", methods = ["POST","GET"])
def i_product_backlog():

    return render_template("Initialer Product Backlog.html")

@app.route("/Lastenheft", methods = ["POST","GET"])
def lastenheft():

    return render_template("Lastenheft.html")

@app.route("/Agiles_Vorgehen", methods = ["POST","GET"])
def agilesVorgehen():

    return render_template("Agiles Vorgehen.html")

@app.route("/Phasenmodell", methods = ["POST","GET"])
def phasenmodell():

    return render_template("Phasenmodell.html")

@app.route("/Matrix_Projektorganisation", methods = ["POST","GET"])
def matrix():

    return render_template("Matrix Projektorganisation.html")

@app.route("/Staborganisation", methods = ["POST","GET"])
def staborganisation():

    return render_template("Staborganisation.html")

@app.route("/Formale_Spezifikation", methods = ["POST","GET"])
def formale():

    return render_template("Formale Spezifikation.html")

@app.route("/Grafische_Spezifikation_mit_UML", methods = ["POST","GET"])
def uml():

    return render_template("Grafische Spezifikation mit UML.html")

@app.route("/Natürlichsprachige_Spezifikation_mit_Sprachschablonen", methods = ["POST","GET"])
def natuerlichsprachige():

    return render_template("Natürlichsprachige Spezifikation mit Sprachschablonen.html")

@app.route("/Bubble_sort", methods = ["POST","GET"])
def bubble_sort():

    return render_template("Bubble sort.html")

@app.route("/Numeral_assignment", methods = ["POST","GET"])
def numeral_assignment():

    return render_template("Numeral assignment.html")

@app.route("/Analytical_Hierarchy_Process", methods = ["POST","GET"])
def ahp():

    return render_template("Analytical Hierarchy Process.html")

@app.route("/Cumulative_Voting", methods = ["POST","GET"])
def cv():

    return render_template("Cumulative Voting.html")

@app.route("/Minimal_spanning_tree", methods = ["POST","GET"])
def msp():

    return render_template("Minimal spanning tree.html")

@app.route("/Hierarchical_Cumulative_Voting", methods = ["POST","GET"])
def hcv():

    return render_template("Hierarchical Cumulative Voting.html")

@app.route("/Pflichtenheft", methods = ["POST","GET"])
def pflichtenheft():

    return render_template("Pflichtenheft.html")

@app.route("/Product_Backlog", methods = ["POST","GET"])
def product_backlog():

    return render_template("Product Backlog.html")

@app.route("/Projektstrukturplan", methods = ["POST","GET"])
def psp():

    return render_template("Projektstrukturplan.html")

@app.route("/Expertenschätzung", methods = ["POST","GET"])
def experten():

    return render_template("Expertenschätzung.html")

@app.route("/Algorithmische_Schätzung", methods = ["POST","GET"])
def algorithmische_schaetzung():

    return render_template("Algorithmische Schätzung.html")

@app.route("/T-Shirt_Sizing", methods = ["POST","GET"])
def tshirt():

    return render_template("T-Shirt Sizing.html")

@app.route("/Planning_Poker", methods = ["POST","GET"])
def planning_poker():

    return render_template("Planning Poker.html")

@app.route("/Gantt_Diagramm", methods = ["POST","GET"])
def gantt():

    return render_template("Gantt Diagramm.html")

@app.route("/Netzpläne", methods = ["POST","GET"])
def netzplaene():

    return render_template("Netzpläne.html")

@app.route("/Burndown_Chart", methods = ["POST","GET"])
def burndown():

    return render_template("Burndown Chart.html")

@app.route("/Sprint_Review", methods = ["POST","GET"])
def sprint_review():

    return render_template("Sprint Review.html")

@app.route("/Earned_Value_Analyse", methods = ["POST","GET"])
def eva():

    return render_template("Earned Value Analyse.html")

@app.route("/Meilensteintrendanalyse", methods = ["POST","GET"])
def mst():

    return render_template("Meilensteintrendanalyse.html")


if __name__ == "__main__":
    app.run(debug=True)
