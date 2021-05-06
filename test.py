import operator

""" -------------------------------- BAUSTEINE -------------------------------- """


#Projekt starten
#Grobziele definieren

#Kundenanforderungen erheben
beobachtungstechnik_score = 0
befragungstechnik_score = 0
kreativitaetstechnik_score = 0
kundenanforderungen_erheben = {"Beobachtungstechnik" : beobachtungstechnik_score,
                               "Befragungstechnik" : befragungstechnik_score,
                               "Kreativitätstechnik" : befragungstechnik_score}

def kundenanforderungen_erheben_funktion(beobachtungstechnik_score, kreativitaetstechnik_score, befragungstechnik_score):
    k = komplexitaet_messen(befragungstechnik_score, kreativitaetstechnik_score, matrix_score,
                            stab_score, reine_po_score, pflichtenheft_dokumentieren_score,
                            projektstrukturplan_score, netzplan_score, formale_score,
                            uml_score, natürlichsprachig_score)
    z = zeitkritikalitaet_messen(ahp_score, bubble_sort_score, cv_score, numeral_assignment_score, hcv_score, msp_score, beobachtungstechnik_score, befragungstechnik_score, initialer_product_backlog_score, stab_score, reine_po_score, matrix_score, burndown_score)
    q = qualifikation_messen(beobachtungstechnik_score, matrix_score, stab_score,
                             reine_po_score, experten_score, algorithmisch_score,
                             formale_score, uml_score, natürlichsprachig_score)
    pd = projektdauer_messen(befragungstechnik_score, beobachtungstechnik_score, stab_score,
                        matrix_score, reine_po_score, planning_poker_score)
    ka = klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score,
                                       projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score,
                                       initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score,
                                       burndown_score, eva_score, meilensteintrend_score)
    e = einsatz_messen(beobachtungstechnik_score, stab_score, reine_po_score, matrix_score)
    er = erfahrung_messen(beobachtungstechnik_score, reine_po_score, matrix_score,
                          stab_score, experten_score, formale_score,
                          uml_score, natürlichsprachig_score)
    b = bedeutung_messen(stab_score, matrix_score, pflichtenheft_dokumentieren_score,
                     projektstrukturplan_score, tshirt_score, kreativitaetstechnik_score,
                     reine_po_score, formale_score, uml_score, natürlichsprachig_score)
    v = verteilung_messen(beobachtungstechnik_score, natürlichsprachig_score)
    beobachtungstechnik_score = z[8] + q[0] + pd[1] + e[0] + er[0] + v[0]
    befragungstechnik_score = z[7] + k[0] + pd[0] + ka[0]
    kreativitaetstechnik_score = k[1] + ka[5] + b[5]

    kundenanforderungen_erheben = {"Beobachtungstechnik": beobachtungstechnik_score,
                                   "Befragungstechnik": befragungstechnik_score,
                                   "Kreativitätstechnik": kreativitaetstechnik_score}

    print(kundenanforderungen_erheben)
    print(max(kundenanforderungen_erheben, key=kundenanforderungen_erheben.get))



#Kundenanforderungen festhalten
initialer_product_backlog_score = 0 #z[8]
lastenheft_score = 0

def kundenanforderungen_festhalten_funktion(initialer_product_backlog_score, lastenheft_score):
    z = zeitkritikalitaet_messen(ahp_score, bubble_sort_score, cv_score, numeral_assignment_score, hcv_score, msp_score, beobachtungstechnik_score, befragungstechnik_score, initialer_product_backlog_score, stab_score, reine_po_score, matrix_score, burndown_score)
    ka = klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score,
                                       projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score,
                                       initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score,
                                       burndown_score, eva_score, meilensteintrend_score)
    initialer_product_backlog_score = z[8] + ka[6]
    lastenheft_score = ka[1]

    kundenanforderungen_festhalten = {"Initialer Product Backlog": initialer_product_backlog_score,
                                   "Lastenheft": lastenheft_score}

    print(kundenanforderungen_festhalten)
    print(max(kundenanforderungen_festhalten, key=kundenanforderungen_festhalten.get))


#PM-Prozess festlegen

#Organisation festlegen
matrix_score = 0
stab_score = 0
reine_po_score = 0
organisation_festlegen = {"Matrix Projektorganisation" : matrix_score,
                          "Staborganisation" : befragungstechnik_score,
                          "Reine Projektorganisation" : reine_po_score}

def organisation_festlegen_methode(matrix_score, reine_po_score, stab_score):
    p = projektgroeße(ahp_score, bubble_sort_score, stab_score, product_backlog_planen_score, cv_score,
                      numeral_assignment_score, matrix_score, projektstrukturplan_score, hcv_score, msp_score,
                      reine_po_score)
    z = zeitkritikalitaet_messen(ahp_score, bubble_sort_score, cv_score,
                                 numeral_assignment_score, hcv_score, msp_score,
                                 beobachtungstechnik_score, befragungstechnik_score, initialer_product_backlog_score,
                                 stab_score, reine_po_score, matrix_score, burndown_score)
    k = komplexitaet_messen(befragungstechnik_score, kreativitaetstechnik_score, matrix_score,
                            stab_score, reine_po_score, pflichtenheft_dokumentieren_score,
                            projektstrukturplan_score, netzplan_score, formale_score,
                            uml_score, natürlichsprachig_score)
    q = qualifikation_messen(beobachtungstechnik_score, matrix_score, stab_score,
                             reine_po_score, experten_score, algorithmisch_score,
                             formale_score, uml_score, natürlichsprachig_score)
    pd = projektdauer_messen(befragungstechnik_score, beobachtungstechnik_score, stab_score,
                             matrix_score, reine_po_score, planning_poker_score)
    e = einsatz_messen(beobachtungstechnik_score, stab_score, reine_po_score, matrix_score)
    er = erfahrung_messen(beobachtungstechnik_score, reine_po_score, matrix_score,
                          stab_score, experten_score, formale_score,
                          uml_score, natürlichsprachig_score)
    b = bedeutung_messen(stab_score, matrix_score, pflichtenheft_dokumentieren_score,
                     projektstrukturplan_score, tshirt_score, kreativitaetstechnik_score,
                     reine_po_score, formale_score, uml_score, natürlichsprachig_score)
    matrix_score = p[6] + z[11] + k[2] + q[1] + pd[3] + e[3] + er[2] + b[1]
    reine_po_score = p[10] + z[10] + k[4] + q[3] + pd[4] + e[2] + er[1] + b[6]
    stab_score = p[2] + z[9] + k[3] + q[2] + pd[2] + e[1] + er[3] + b[0]

    organisation_festlegen = {"Matrix Projektorganisation": matrix_score,
                              "Staborganisation": stab_score,
                              "Reine Projektorganisation": reine_po_score}

    print(organisation_festlegen)
    print(max(organisation_festlegen, key=organisation_festlegen.get))


#Rollen definieren

#Anforderungsspezifikation
formale_score = 0
uml_score = 0
natürlichsprachig_score = 0

def anforderungsspezifikation_methode(formale_score, uml_score, natürlichsprachig_score):
    k = komplexitaet_messen(befragungstechnik_score, kreativitaetstechnik_score, matrix_score,
                            stab_score, reine_po_score, pflichtenheft_dokumentieren_score,
                            projektstrukturplan_score, netzplan_score, formale_score,
                            uml_score, natürlichsprachig_score)
    q = qualifikation_messen(beobachtungstechnik_score, matrix_score, stab_score,
                             reine_po_score, experten_score, algorithmisch_score,
                             formale_score, uml_score, natürlichsprachig_score)
    er = erfahrung_messen(beobachtungstechnik_score, reine_po_score, matrix_score,
                          stab_score, experten_score, formale_score,
                          uml_score, natürlichsprachig_score)
    b = bedeutung_messen(stab_score, matrix_score, pflichtenheft_dokumentieren_score,
                     projektstrukturplan_score, tshirt_score, kreativitaetstechnik_score,
                     reine_po_score, formale_score, uml_score, natürlichsprachig_score)
    v = verteilung_messen(beobachtungstechnik_score, natürlichsprachig_score)
    formale_score = k[8] + q[6] + er[5] + b[7]
    uml_score = k[9] + q[7] + er[6] + b[8]
    natürlichsprachig_score = k[10] + q[8] + er[7] + b[9] + v[1]

    anforderungsspezifikation = {"Formale Spezifikation": formale_score,
                              "Grafische Spezifikation mit UML": uml_score,
                              "Natürlichsprachige Spezifikation mit Sprachschablonen": natürlichsprachig_score}

    print(anforderungsspezifikation)
    print(max(anforderungsspezifikation, key=anforderungsspezifikation.get))



#Anforderungen Priorisieren
bubble_sort_score = 0
numeral_assignment_score = 0
ahp_score = 0
cv_score = 0
msp_score = 0
hcv_score = 0

def anforderungen_priorisieren(ahp_score, cv_score, bubble_sort_score, numeral_assignment_score,hcv_score, msp_score):
    p = projektgroeße(ahp_score, bubble_sort_score, stab_score, product_backlog_planen_score, cv_score,
                      numeral_assignment_score, matrix_score, projektstrukturplan_score, hcv_score, msp_score,
                      reine_po_score)
    z = zeitkritikalitaet_messen(ahp_score, bubble_sort_score, cv_score, numeral_assignment_score, hcv_score, msp_score, beobachtungstechnik_score, befragungstechnik_score, initialer_product_backlog_score, stab_score, reine_po_score, matrix_score, burndown_score)
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
    print(max(anforderungen_priorisieren, key=anforderungen_priorisieren.get))


#Anforderungen dokumentieren
pflichtenheft_dokumentieren_score = 0
product_backlog_dokumentieren_score = 0

def anforderungen_dokumentieren_methode(pflichtenheft_dokumentieren_score, product_backlog_dokumentieren_score):
    k = komplexitaet_messen(befragungstechnik_score, kreativitaetstechnik_score, matrix_score,
                            stab_score, reine_po_score, pflichtenheft_dokumentieren_score,
                            projektstrukturplan_score, netzplan_score, formale_score,
                            uml_score, natürlichsprachig_score)
    ka = klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score,
                                       projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score,
                                       initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score,
                                       burndown_score, eva_score, meilensteintrend_score)
    b = bedeutung_messen(stab_score, matrix_score, pflichtenheft_dokumentieren_score,
                     projektstrukturplan_score, tshirt_score, kreativitaetstechnik_score,
                     reine_po_score, formale_score, uml_score, natürlichsprachig_score)
    s = stabilitaet_messen(projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score,
                           product_backlog_planen_score, burndown_score, meilensteintrend_score,
                           product_backlog_termine_score)
    pflichtenheft_dokumentieren_score = k[5] + ka[2] + b[2]
    product_backlog_dokumentieren_score = ka[7] + s[1]

    anforderungen_dokumentieren = {"Pflichtenheft": pflichtenheft_dokumentieren_score,
                                   "Product Backlog dokumentieren": product_backlog_dokumentieren_score}

    print(anforderungen_dokumentieren)
    print(max(anforderungen_dokumentieren, key=anforderungen_dokumentieren.get))

#Phasen und Meilensteine festlegen

#Inhalte planen
product_backlog_planen_score = 0 #p[3]
projektstrukturplan_score = 0

def inhalte_planen_methode(product_backlog_planen_score, projektstrukturplan_score):
    k = komplexitaet_messen(befragungstechnik_score, kreativitaetstechnik_score, matrix_score,
                            stab_score, reine_po_score, pflichtenheft_dokumentieren_score,
                            projektstrukturplan_score, netzplan_score, formale_score,
                            uml_score, natürlichsprachig_score)
    p = projektgroeße(ahp_score, bubble_sort_score, stab_score, product_backlog_planen_score, cv_score,
                      numeral_assignment_score, matrix_score, projektstrukturplan_score, hcv_score, msp_score,
                      reine_po_score)
    ka = klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score,
                                       projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score,
                                       initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score,
                                       burndown_score, eva_score, meilensteintrend_score)
    b = bedeutung_messen(stab_score, matrix_score, pflichtenheft_dokumentieren_score,
                     projektstrukturplan_score, tshirt_score, kreativitaetstechnik_score,
                     reine_po_score, formale_score, uml_score, natürlichsprachig_score)
    s = stabilitaet_messen(projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score,
                           product_backlog_planen_score, burndown_score, meilensteintrend_score,
                           product_backlog_termine_score)
    product_backlog_planen_score = p[3] + s[3]
    projektstrukturplan_score = k[6] + ka[3] + b[3] + s[0]

    inhalte_planen = {"Projektstrukturplan": projektstrukturplan_score,
                      "Product Backlog planen": product_backlog_planen_score}

    print(inhalte_planen)
    print(max(inhalte_planen, key=inhalte_planen.get))


#Aufwände schätzen
experten_score = 0
algorithmisch_score = 0
tshirt_score = 0
planning_poker_score = 0

def aufwaende_schaetzen_methode(experten_score, algorithmisch_score, tshirt_score, planning_poker_score):
    q = qualifikation_messen(beobachtungstechnik_score, matrix_score, stab_score,
                             reine_po_score, experten_score, algorithmisch_score,
                             formale_score, uml_score, natürlichsprachig_score)
    pd = projektdauer_messen(befragungstechnik_score, beobachtungstechnik_score, stab_score,
                             matrix_score, reine_po_score, planning_poker_score)
    ka = klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score,
                                       projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score,
                                       initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score,
                                       burndown_score, eva_score, meilensteintrend_score)
    er = erfahrung_messen(beobachtungstechnik_score, reine_po_score, matrix_score,
                          stab_score, experten_score, formale_score,
                          uml_score, natürlichsprachig_score)
    b = bedeutung_messen(stab_score, matrix_score, pflichtenheft_dokumentieren_score,
                     projektstrukturplan_score, tshirt_score, kreativitaetstechnik_score,
                     reine_po_score, formale_score, uml_score, natürlichsprachig_score)
    s = stabilitaet_messen(projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score,
                           product_backlog_planen_score, burndown_score, meilensteintrend_score,
                           product_backlog_termine_score)
    experten_score = q[4] + er[4]
    algorithmisch_score = q[5]
    tshirt_score = ka[8] + b[4] + s[2]
    planning_poker_score = pd[5]

    aufwaende_schaetzen = {"Expertenschätzung": experten_score,
                           "Algorithmische Schätzung" : algorithmisch_score,
                           "T-Shirt Sizing" : tshirt_score,
                           "Planning Poker" : planning_poker_score}

    print(aufwaende_schaetzen)
    print(max(aufwaende_schaetzen, key=aufwaende_schaetzen.get))

#Termine planen
gantt_termine_score = 0
netzplan_score = 0
product_backlog_termine_score = 0

def termine_planen_methode(gantt_termine_score, netzplan_score, product_backlog_termine_score):
    k = komplexitaet_messen(befragungstechnik_score, kreativitaetstechnik_score, matrix_score,
                            stab_score, reine_po_score, pflichtenheft_dokumentieren_score,
                            projektstrukturplan_score, netzplan_score, formale_score,
                            uml_score, natürlichsprachig_score)
    s = stabilitaet_messen(projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score,
                           product_backlog_planen_score, burndown_score, meilensteintrend_score,
                           product_backlog_termine_score)
    netzplan_score = k[7]
    product_backlog_termine_score = s[6]
    gantt_termine_score = 0

    termine_planen = {"Netzplan": netzplan_score,
                      "Product Backlog Termine": product_backlog_termine_score,
                      "Gantt Diagramm" : gantt_termine_score}

    print(termine_planen)
    print(max(termine_planen, key=termine_planen.get))

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
                                       burndown_score, eva_score, meilensteintrend_score)
    s = stabilitaet_messen(projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score,
                           product_backlog_planen_score, burndown_score, meilensteintrend_score,
                           product_backlog_termine_score)
    burndown_score = ka[9] + s[4]
    gantt_fortschritt_score = ka[4]

    fortschritt_bestimmen = {"Burndown Chart": burndown_score,
                             "Gantt Diagramm Fortschritt" : gantt_fortschritt_score}

    print(fortschritt_bestimmen)
    print(max(fortschritt_bestimmen, key=fortschritt_bestimmen.get))

#Fortschritt analysieren
sprint_review_score = 0
eva_score = 0
meilensteintrend_score = 0

def fortschritt_analysieren_methode(sprint_review_score, eva_score, meilensteintrend_score):
    ka = klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score,
                                       projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score,
                                       initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score,
                                       burndown_score, eva_score, meilensteintrend_score)
    s = stabilitaet_messen(projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score,
                           product_backlog_planen_score, burndown_score, meilensteintrend_score,
                           product_backlog_termine_score)
    sprint_review_score = 0
    eva_score = ka[10]
    meilensteintrend_score = ka[11] + s[5]

    fortschritt_analysieren = {"Sprint Review": sprint_review_score,
                             "Earned Value Analyse" : eva_score,
                             "Meilensteintrendanalyse" : meilensteintrend_score}

    print(fortschritt_analysieren)
    print(max(fortschritt_analysieren, key=fortschritt_analysieren.get))

#Fortschritt steuern
sprint_retrospektive_score = 0
ressourcen_veraendern_score = 0

#Ergebnisse übergeben
finales_produkt_score = 0
inkrement_score = 0

""" -------------------------------- KRITERIEN -------------------------------- """
zeitkritikalitaet = "Hoch"
projektgroeße = "Groß"
klarheit_anforderungen = "Unklar"
verteilung = "Zentral"
komplexitaet = "Hoch"
qualifikation = "Professionell"
projektdauer = "Kurz"
einsatz = "Nebenamtlich", "Hauptamtlich", "Teilzeit"
erfahrung = "4+ Jahre"
bedeutung = "Groß"
stabilitaet = "Stabil", "Volatil"

def stabilitaet_messen(projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score, product_backlog_planen_score, burndown_score, meilensteintrend_score, product_backlog_termine_score):
    if stabilitaet == "Stabil":
        projektstrukturplan_score += 1
    if stabilitaet == "Volatil":
        product_backlog_dokumentieren_score += 1
        tshirt_score += 1
        product_backlog_planen_score += 1
        burndown_score += 1
        meilensteintrend_score += 1
        product_backlog_termine_score += 1
    return [projektstrukturplan_score, product_backlog_dokumentieren_score, tshirt_score, product_backlog_planen_score, burndown_score, meilensteintrend_score, product_backlog_termine_score]

def verteilung_messen(beobachtungstechnik_score, natürlichsprachig_score):
    #if verteilung == "Zentral":

    if verteilung == "Dezentral":
        beobachtungstechnik_score -= 1
        natürlichsprachig_score += 1
    return [beobachtungstechnik_score, natürlichsprachig_score]

def bedeutung_messen(stab_score, matrix_score, pflichtenheft_dokumentieren_score, projektstrukturplan_score, tshirt_score, kreativitaetstechnik_score, reine_po_score, formale_score, uml_score, natürlichsprachig_score):
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

def erfahrung_messen(beobachtungstechnik_score, reine_po_score, matrix_score, stab_score, experten_score, formale_score, uml_score, natürlichsprachig_score):
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

def einsatz_messen(beobachtungstechnik_score,stab_score, reine_po_score, matrix_score):
    if einsatz == "Nebenamtlich":
        beobachtungstechnik_score -= 1
        stab_score += 1
    if einsatz == "Hauptamtlich":
        reine_po_score += 1
    if einsatz == "Teilzeit":
        beobachtungstechnik_score -= 1
        matrix_score += 1
    return [beobachtungstechnik_score,stab_score, reine_po_score, matrix_score]

def klarheit_anforderungen_messen(befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score, projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score, initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score, burndown_score, eva_score, meilensteintrend_score):
    if klarheit_anforderungen == "Klar":
        befragungstechnik_score +=1
        lastenheft_score +=1
        pflichtenheft_dokumentieren_score +=1
        projektstrukturplan_score +=1
        gantt_fortschritt_score +=1
    if klarheit_anforderungen == "Unklar":
        kreativitaetstechnik_score +=1
        initialer_product_backlog_score +=1
        product_backlog_dokumentieren_score +=1
        tshirt_score +=1
        burndown_score +=1
        eva_score -=1
        meilensteintrend_score -=1
    return [befragungstechnik_score, lastenheft_score, pflichtenheft_dokumentieren_score, projektstrukturplan_score, gantt_fortschritt_score, kreativitaetstechnik_score, initialer_product_backlog_score, product_backlog_dokumentieren_score, tshirt_score, burndown_score, eva_score, meilensteintrend_score]

def projektdauer_messen(befragungstechnik_score, beobachtungstechnik_score, stab_score, matrix_score, reine_po_score, planning_poker_score):
    if projektdauer == "Kurz":
        befragungstechnik_score -= 1
        beobachtungstechnik_score -= 1
        stab_score += 1
    if projektdauer == "Mittel":
        matrix_score += 1
    if projektdauer == "Lang":
        matrix_score += 1
        reine_po_score += 1
        planning_poker_score += 1
    return [befragungstechnik_score, beobachtungstechnik_score, stab_score, matrix_score, reine_po_score, planning_poker_score]
#Kriterium Qualifikation der Mitarbeiter
def qualifikation_messen(beobachtungstechnik_score, matrix_score, stab_score, reine_po_score, experten_score, algorithmisch_score, formale_score, uml_score, natürlichsprachig_score):
    if qualifikation == "Professionell":
        beobachtungstechnik_score += 1
        reine_po_score += 1
        experten_score += 1
        formale_score += 1
    if qualifikation == "Qualifiziert":
        beobachtungstechnik_score += 1
        matrix_score += 1
        uml_score += 1
        formale_score -= 1
    if qualifikation == "Wenig qualifiziert":
        stab_score += 1
        algorithmisch_score += 1
        natürlichsprachig_score += 1
        formale_score -= 1
    return [beobachtungstechnik_score, matrix_score, stab_score,
            reine_po_score, experten_score, algorithmisch_score,
            formale_score, uml_score, natürlichsprachig_score]


#Kriterium Komplexität
def komplexitaet_messen(befragungstechnik_score, kreativitaetstechnik_score, matrix_score,stab_score, reine_po_score, pflichtenheft_dokumentieren_score,projektstrukturplan_score, netzplan_score, formale_score, uml_score ,natürlichsprachig_score):
    if komplexitaet == "Gering":
        stab_score += 1
        natürlichsprachig_score += 1
        formale_score -= 1
    if komplexitaet == "Mittel":
        matrix_score += 1
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
    return [befragungstechnik_score, kreativitaetstechnik_score, matrix_score,
            stab_score, reine_po_score, pflichtenheft_dokumentieren_score,
            projektstrukturplan_score, netzplan_score, formale_score,
            uml_score ,natürlichsprachig_score]

#Kriterium Projektgröße
def projektgroeße(ahp_score, bubble_sort_score, stab_score, product_backlog_planen_score, cv_score, numeral_assignment_score, matrix_score, projektstrukturplan_score, hcv_score, msp_score, reine_po_score):
    if projektgroeße == "Klein":
        ahp_score += 1
        cv_score += 1
        bubble_sort_score += 1
        stab_score += 1
        product_backlog_planen_score += 1
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
    return [ahp_score, bubble_sort_score, stab_score, product_backlog_planen_score, cv_score, numeral_assignment_score, matrix_score, projektstrukturplan_score, hcv_score, msp_score, reine_po_score]

def zeitkritikalitaet_messen(ahp_score, bubble_sort_score, cv_score, numeral_assignment_score, hcv_score, msp_score, beobachtungstechnik_score, befragungstechnik_score, initialer_product_backlog_score, stab_score, reine_po_score, matrix_score, burndown_score):
    if zeitkritikalitaet == "Gering":
        ahp_score += 1
        befragungstechnik_score += 1
        beobachtungstechnik_score += 1
        stab_score += 1
    if zeitkritikalitaet == "Mittel":
        numeral_assignment_score +=1
        bubble_sort_score +=1
        matrix_score += 1
    if zeitkritikalitaet == "Hoch":
        msp_score += 1
        cv_score += 1
        hcv_score += 1
        befragungstechnik_score -= 1
        beobachtungstechnik_score -= 1
        initialer_product_backlog_score += 1
        reine_po_score += 1
        burndown_score += 1
    return [ahp_score, bubble_sort_score, cv_score, numeral_assignment_score, hcv_score, msp_score, befragungstechnik_score, beobachtungstechnik_score, initialer_product_backlog_score, stab_score, reine_po_score, matrix_score, burndown_score]

def inhalte_planen(product_backlog_planen_score, projektstrukturplan_score):
    if projektstrukturplan_score > initialer_product_backlog_score:
        print("Projektstrukturplan")
    elif product_backlog_planen_score > projektstrukturplan_score:
        print("Product Backlog")



kundenanforderungen_erheben_funktion(beobachtungstechnik_score, kreativitaetstechnik_score, befragungstechnik_score)
organisation_festlegen_methode(matrix_score, reine_po_score, stab_score)
anforderungen_priorisieren(ahp_score, cv_score, bubble_sort_score, numeral_assignment_score,hcv_score, msp_score)
termine_planen_methode(gantt_termine_score, netzplan_score, product_backlog_termine_score)
kundenanforderungen_festhalten_funktion(initialer_product_backlog_score, lastenheft_score)
anforderungen_dokumentieren_methode(pflichtenheft_dokumentieren_score, product_backlog_dokumentieren_score)
inhalte_planen_methode(product_backlog_planen_score, projektstrukturplan_score)
termine_planen_methode(gantt_termine_score, netzplan_score, product_backlog_termine_score)
aufwaende_schaetzen_methode(experten_score, algorithmisch_score, tshirt_score, planning_poker_score)
fortschritt_bestimmen_methode(burndown_score, gantt_fortschritt_score)
fortschritt_analysieren_methode(sprint_review_score, eva_score, meilensteintrend_score)
anforderungsspezifikation_methode(formale_score, uml_score, natürlichsprachig_score)