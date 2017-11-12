from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/graph/<list_id>')
def show_graphs(list_id):
    if list_id == "1":
        watchlist = ["TLS.AX", "WFD.AX"]
    else:
        watchlist = []
    print(watchlist)
    return render_template("watchlist.html", watchlist=watchlist)
