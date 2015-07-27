from flask import Flask
from flask import request, jsonify, render_template, make_response
import pandas as pd
import json
import sys
import glob
import numpy as np
import argparse

from pyxley import UILayout
from pyxley.filters import SelectButton
from pyxley.charts.mg import LineChart, Figure, ScatterPlot, Histogram
from pyxley.charts.datatables import DataTable
from collections import OrderedDict

import alert_viewer as sis_alertas

parser = argparse.ArgumentParser(description="Flask Template")
parser.add_argument("--env", help="production or local", default="local")
args = parser.parse_args()

TITLE = "Pyxley"

scripts = [
    "./bower_components/jquery/dist/jquery.min.js",
    "./bower_components/datatables/media/js/jquery.dataTables.js",
    "./bower_components/d3/d3.min.js",
    "./bower_components/metrics-graphics/dist/metricsgraphics.js",
    "./bower_components/require/build/require.min.js",
    "./bower_components/react/react.js",
    "./bower_components/react-bootstrap/react-bootstrap.min.js",
    "./bower_components/pyxley/build/pyxley.js",
]

css = [
    "./bower_components/bootstrap/dist/css/bootstrap.min.css",
    "./bower_components/metrics-graphics/dist/metricsgraphics.css",
    "./bower_components/datatables/media/css/jquery.dataTables.min.css",
    "./css/main.css"
]

# Make a UI
ui = UILayout(
    "FilterChart",
    "./static/bower_components/pyxley/build/pyxley.js",
    "component_id",
    filter_style="''")

# Read in the data and stack it, so that we can filter on columns

dir_alertas = 'C:/Users/david.lopes\Documents/HP DAVID/Sitescope/Customizacoes/Alert Log Viewer/'

try:
    df = pd.read_csv(dir_alertas + 'sitescope003/' +
                 'arquivo_alertas_web.txt')
except UnicodeDecodeError:
    df = pd.read_csv(dir_alertas + 'sitescope003/' +
                 'arquivo_alertas_web.txt', encoding='latin-1')

df = df.loc[df['alert-name'] != 'Eventos'].reset_index()
df = df.iloc[::-1]

#df = df.sort(['hora'], ascending=[1])
#print (df.columns.tolist())

#print (df)
#sf = sf.rename(columns={"level_1": "Data", 0: "value"})
sf = df.set_index("alert-id").stack().reset_index()
sf = sf.rename(columns={"level_1": "Data", 0: "value"})

print(sf)

# Make a Button
sitescopes = [c for c in ['Sitescope001', 'Sitescope002', 'Sitescope003', 'Sitescope004']]
btn = SelectButton("Servidor", sitescopes, "Data", "Sitescope")

# Make a FilterFrame and add the button to the UI
ui.add_filter(btn)


# Now make a FilterFrame for the histogram
hFig = Figure("/mghist/", "myhist")
hFig.layout.set_size(width=450, height=200)
hFig.layout.set_margin(left=40, right=40)
hFig.graphics.animate_on_load()
# Make a histogram with 20 bins
hc = Histogram(sf, hFig, "value", 20, init_params={"Data": "Sitescope"})
ui.add_chart(hc)

# Let's play with our input

#print(df)

cols = OrderedDict([
    ("hora", {"label": "Hora"}),
    ("alert-monitor", {"label": "Monitor"}),
    ("alert-name", {"label": "Nome"}),
    ("alert-message", {"label": "Mensagem"}),
    ("alert-type", {"label": "Tipo"}),
    ("alert-id", {"label": "ID"}),
    ("alert-monitor-id", {"label": "Monitor ID"}),
    ("alert-group", {"label": "Grupo"}),
])


tb = DataTable("mytable", "/mytable/", df,
               columns=cols,
               paging=True,
               pageLength=50,
               init_params={"Data": "Sitescope"})

ui.add_chart(tb)


app = Flask(__name__)
sb = ui.render_layout(app, "./static/layout.js")


@app.route('/', methods=["GET"])
@app.route('/index', methods=["GET"])
def index():
    _scripts = ["./layout.js"]
    return render_template('index.html',
        title=TITLE,
        base_scripts=scripts,
        page_scripts=_scripts,
        css=css)

if __name__ == "__main__":
    app.run(host='10.116.90.112', port=80, debug=True)