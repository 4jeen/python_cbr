from flask import Flask
from flask import Response
import exchangeRates
import exchangeRates2Redis as er


def getCbr(*sUrl):
	return exchangeRates.getCbrExchangeRates2Json(sUrl)

def getExRJson():
	return er.getRates()

def getRatesArrayJson():
	return er.getRatesArrayFromRedis()

def getCurrenciesArray():
	return exchangeRates.getCbrCurrenciesArray2Json()


mimeJson='application/json'
mimeText='text/html'
app = Flask(__name__)
first_page = '<html><head></head><body><p>Directory listing prohibited</p>\
	<p>USAGE:</p><ul><li><a href="/cbr">http://localhost/cbr -> CBR to Json direct</a></li>\
	<li><a href="/cbr2text">http://localhost/cbr2text -> plain text</a></li>\
	<li><a href="/rd_cache">http://localhost/rd_cache -> redis cache</a></li>\
	<li><a href="/erts">http://localhost/erts ->  Currencies Json Array</a></li>\
	<li><a href="/erts_rd_cache">http://localhost/erts_rd_cache ->  Currencies Json  redis cache</a></li>\
	</ul></body></html>'

@app.route('/')
def default():
    return Response(first_page, mimetype=mimeText)

@app.route('/cbr', methods=['GET'])
def cbr():
	return Response( getCbr(), mimetype=mimeJson)

@app.route('/rd_cache', methods=['GET'])
def rd_c():
	return Response( getExRJson(), mimetype=mimeJson)	

@app.route('/erts', methods=['GET'])
def erj():
	return Response(  getCurrenciesArray() , mimetype=mimeJson)
@app.route('/erts_rd_cache', methods=['GET'])
def erj_rd_c():
	return Response(  getRatesArrayJson() , mimetype=mimeJson)


@app.route('/cbr2text', methods=['GET'])
def cbr2text():
	''' return json as plain text '''
	return Response( getCbr(), mimetype=mimeText)	

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')

