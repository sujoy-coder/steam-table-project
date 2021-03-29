from flask import Flask, render_template, request
from src import from_pressure, round_off
from src import from_temperature

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inputbyPressure',methods=['GET','POST'])
def inputbyPressure():
    if request.method=='POST':
        pressure=float(request.form['pressure'])
        ans=from_pressure(pressure)
        ans=round_off(ans, 8)
        return render_template('preasure.html', ans=ans)
    return render_template('preasure.html', ans=False)

@app.route('/inputbyTemperature',methods=['GET','POST'])
def inputbyTemperature():
    if request.method=='POST':
        temperature=float(request.form['temperature'])
        ans=from_temperature(temperature)
        ans=round_off(ans, 8)
        return render_template('temperature.html', ans=ans)
    return render_template('temperature.html', ans=False)


if __name__=="__main__":
    app.run(debug=True)