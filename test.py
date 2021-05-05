

'''Bausteine Vorgehensmodell'''

#Projekt starten
#Grobziele definieren

#Kundenanforderungen erheben
beobachtungstechnik_score = 0
befragungstechnik_score = 0
kreativitaetstechnik_score = 0
kundenanforderungen_erheben = {"Beobachtungstechnik" : beobachtungstechnik_score,
                               "Befragungstechnik" : befragungstechnik_score,
                               "Kreativitätstechnik" : befragungstechnik_score}

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
def ahp_score_berechnen():
    ahp_score = 0
    if projektgroeße == "Klein" and zeitkritikalitaet == "Niedrig":
        ahp_score += 2
    elif projektgroeße == "Klein" or zeitkritikalitaet == "Niedrig":
        ahp_score += 1
    return ahp_score

def bubble_sort_score_berechnen():
    bubble_sort_score = 0
    if projektgroeße == "Klein" and zeitkritikalitaet == "Mittel":
        bubble_sort_score += 2
    elif projektgroeße == "Klein" or zeitkritikalitaet == "Mittel":
        bubble_sort_score += 1
    return bubble_sort_score
def cv_score_berechnen():
    cv_score = 0
    if projektgroeße == "Klein" or projektgroeße == "Mittel" and zeitkritikalitaet == "Hoch":
        cv_score += 2
    elif projektgroeße == "Klein" or projektgroeße == "Mittel" or zeitkritikalitaet == "Hoch":
        cv_score += 1
    return cv_score
def numeral_assignment_score_berechnen():
    numeral_assignment_score = 0
    if projektgroeße == "Mittel" or projektgroeße == "Groß" and zeitkritikalitaet == "Mittel":
        numeral_assignment_score += 2
    elif projektgroeße == "Mittel" or projektgroeße == "Groß" or zeitkritikalitaet == "Mittel":
        numeral_assignment_score += 1
    return numeral_assignment_score
def hcv_score_berechnen():
    hcv_score = 0
    if projektgroeße == "Groß" and zeitkritikalitaet == "Hoch":
        hcv_score += 2
    elif projektgroeße == "Groß" or zeitkritikalitaet == "Hoch":
        hcv_score += 1
    return hcv_score
def msp_score_berechnen():
    msp_score = 0
    if projektgroeße == "Klein" or projektgroeße == "Mittel" and zeitkritikalitaet == "Hoch":
        msp_score += 2
    elif projektgroeße == "Klein" or projektgroeße == "Mittel" or zeitkritikalitaet == "Hoch":
        msp_score += 1
    return msp_score

ahp_score = ahp_score_berechnen()
numeral_assignment_score = numeral_assignment_score_berechnen()
msp_score = msp_score_berechnen()
cv_score = cv_score_berechnen()
hcv_score = hcv_score_berechnen()
bubble_sort_score = bubble_sort_score_berechnen()
anforderungen_priorisieren = anforderungen_priorisieren(ahp_score, cv_score, bubble_sort_score, numeral_assignment_score,hcv_score, msp_score)


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




def projektgroeße(ahp_score, bubble_sort_score, stab_score, product_backlog_planen_score, cv_score, numeral_assignment_score, matrix_score, projektstrukturplan_score, hcv_score, msp_score, reine_po_score):
    projektgroeße = input
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
    return ahp_score, bubble_sort_score, stab_score, product_backlog_planen_score, cv_score, numeral_assignment_score, matrix_score, projektstrukturplan_score, hcv_score, msp_score, reine_po_score

def inhalte_planen(product_backlog_planen_score, projektstrukturplan_score):
    if projektstrukturplan_score > initialer_product_backlog_score:
        print("Projektstrukturplan")
    elif product_backlog_planen_score > projektstrukturplan_score:
        print("Product Backlog")

def anforderungen_priorisieren(ahp_score, cv_score, bubble_sort_score, numeral_assignment_score,hcv_score, msp_score):
    anforderungen_priorisieren = {
        "Analytical Hierarchy Process" : ahp_score,
        "Cumulative Voting" : cv_score,
        "Bubble sort" : bubble_sort_score,
        "Minimal spanning tree" : msp_score,
        "Numeral assignment" : numeral_assignment_score,
        "Hierarchical cumulative voting" : hcv_score}
    print(max(anforderungen_priorisieren, key=anforderungen_priorisieren.get))

zeitkritikalitaet = "Mittel"
projektgroeße = "Medium"

