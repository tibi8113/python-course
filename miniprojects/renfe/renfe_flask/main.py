# flask
from flask import Flask, session, redirect, url_for
from flask import render_template
# c9 
import os
# renfe
from controller import renfefunctions as rf


app = Flask(__name__)
app.debug = True
# session: set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route("/")
def renfe():
    return render_template('renfe.html')


# select opc: go | return | monthly
@app.route("/setopc/<opc>")
def setopc(opc):
    session["opc"] = opc
    return "Your have selected " + opc
    #return redirect(url_for('stations'))


# select opc: go | return | monthly
@app.route("/getopc")
def getopc():
    return session["opc"]


# get all stations
@app.route("/stations")
@app.route("/stations/<zone>")
def stations(zone=None):
    if zone in rf.zones.keys():
        stations = rf.zones[zone]
    else:
        #stations = rf.zones
        stations = rf.get_stations()
    
    #return str(stations)
    return render_template('stations.html', stations=stations)


# get price of opc(go|return|monthly) from station1 to station2
@app.route("/price/<opc>/<station1>/<station2>")
def price(opc, station1, station2):
    if (station1 in rf.get_stations() and 
        station2 in rf.get_stations() and 
        opc in ['go','return','monthly']):
        
        price = str(rf.get_price(str(opc), str(station1), str(station2)))
    else:
        price = "Error: "

    return price



if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 5000)))

