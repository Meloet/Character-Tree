from flask import Flask, render_template
app=Flask(__name__,template_folder='templates')
@app.route('/Dulse')
def showDulse():
    return render_template('Dulse.html')
@app.route('/Escovo')
def showEscovo():
    return render_template('Escovo.html')
@app.route('/Reiko')
def showReiko():
    return render_template('Reiko.html')
@app.route('/Sheik')
def showSheik():
    return render_template('Sheik.html')
@app.route('/Vex')
def showVex():
    return render_template('Vex.html')

app.run(debug=True)