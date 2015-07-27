from flask import Flask, render_template, request, jsonify

import alert_viewer as sis_alertas

app = Flask(__name__)


def get_sitescope_log(sitescope):
    dir_alertas = 'C:/Users/david.lopes\Documents/HP DAVID/Sitescope/Customizacoes/Alert Log Viewer/'
    print('Getting Sitescope logs from ' + sitescope)
    sis = sis_alertas.obter_alertas_arquivo(dir_alertas + sitescope)

    if sitescope == 'nnm':
        #print (sis)
        sis = sorted(sis, key=lambda k: k['ID'], reverse=True)
    return sis

scripts = [
    "./bower_components/jquery/dist/jquery.min.js",
    "./bower_components/bootstrap/dist/js/bootstrap.min.js",
    "./bower_components/bootstrap-table/dist/bootstrap-table.js",
    "./bower_components/bootstrap-table-filter/extension/bootstrap-table-filter.js",
    "./bower_components/bootstrap-table-filter/bootstrap-table-filter.js",
    "./bower_components/bootstrap-table-filter/bs-table.js",
    "./js/alert_viewer.js"


]

css = [
    "./bower_components/bootstrap/dist/css/bootstrap.min.css",
    "./bower_components/bootstrap-table/dist/bootstrap-table.css",

]
sitescopes = {'sitescope001':{},
              'sitescope002':{},
              'sitescope003':{},
              'sitescope004':{},
              'nnm':{}
              }

for sis, df in sitescopes.items():
    sitescopes[sis] = get_sitescope_log(sis)


def obter_dados_df(offset, limit, order, sitescope):
    resultado = {}
    limit = int(limit)
    offset = int(offset)

    dataframe = sitescopes[sitescope.lower()][::-1]
    resultado['total'] = len(dataframe)


    alertas = dataframe[offset:offset+limit]

    resultado['rows'] = alertas
    #print (resultado)
    return jsonify(resultado)


@app.route('/refresh')
def recarregar_dados():
    for sis, df in sitescopes.items():
        sitescopes[sis] = get_sitescope_log(sis)
    return render_template('alertas.html',
                           base_scripts = scripts,
                           base_css=css,
                           sitescope='sitescope001')


@app.route('/<sitescope>')
def detalhe_sitescope(sitescope):
    if(sitescope.lower() not in ['sitescope001', 'sitescope002', 'sitescope003', 'sitescope004', 'nnm']):
        return 'Arrombado, apenas Sitescopes: 001, 002, 003 e 004 ou NNM'

    if sitescope.lower() == 'nnm':
         return render_template('alertas_nnm.html',
                           base_scripts = scripts,
                           base_css=css,
                           sitescope=sitescope)
    else:
        return render_template('alertas.html',
                           base_scripts = scripts,
                           base_css=css,
                           sitescope=sitescope)


@app.route('/')
def index():
    return render_template('index.html',
                           base_scripts = scripts,
                           base_css=css,
                           sitescopes=['Sitescope001', 'Sitescope002', 'Sitescope003', 'Sitescope004'])

@app.route('/<sitescope>/get_data')
def get_data(sitescope):
    if(sitescope.lower() not in ['sitescope001', 'sitescope002', 'sitescope003', 'sitescope004', 'nnm']):
        return 'Arrombado, apenas Sitescopes: 001, 002, 003 e 004 ou NNM'
    offset = request.args.get('offset')
    limit = request.args.get('limit')
    order = request.args.get('order')

    return obter_dados_df(offset, limit, order, sitescope)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='10.116.90.112')

