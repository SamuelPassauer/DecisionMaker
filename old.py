
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