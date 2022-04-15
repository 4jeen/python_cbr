import requests
import json
import xmltodict
from collections import OrderedDict


def getCbrExchangeRates2Json( sUrl = 'http://www.cbr.ru/scripts/XML_daily.asp' ):
	''' Gets currency courses from sUrl in XML and converts them to json No conversion , slicing & so on convert to json as is'''
	if sUrl is None or len(sUrl) < 10:
		sUrl = 'http://www.cbr.ru/scripts/XML_daily.asp'
	r = requests.get(sUrl) 
	if r.status_code == requests.codes.ok:
		d_dict=xmltodict.parse( r.text )
		json_txt = json.dumps( d_dict )
	else:
		json_txt = json.dumps( { "Error code" : r.status_code } )
	return json_txt

def getCbr2Dictionary( sUrl = 'http://www.cbr.ru/scripts/XML_daily.asp' ):
	''' As above but return dictionary'''
	if sUrl is None or len(sUrl) < 10:
		sUrl = 'http://www.cbr.ru/scripts/XML_daily.asp'
	r = requests.get(sUrl) 
	if r.status_code == requests.codes.ok:
		d_dict=xmltodict.parse( r.text )
	return d_dict	

def getCbrCurrenciesArray():
	''' Extracts array of currences '''
	s_dict = getCbr2Dictionary()
	if s_dict is None:
		return None
	return  s_dict.get('ValCurs', {}).get('Valute')



def getCbrCurrenciesDate():
	''' Return date of exchange rates '''
	s_dict = getCbr2Dictionary()
	if s_dict is None:
		return None
	return  s_dict.get('ValCurs', {}).get('@Date')

def getCbrCurrenciesArray2Json():
	''' Add @Date attr to each currency and  Converts array  to json '''
	v_arr = getCbrCurrenciesArray()
	cDate=getCbrCurrenciesDate()
	for el in v_arr:
		el['@Date'] = cDate
	return json.dumps( v_arr )

def currency2Json(e):
	return json.dumps( e )

def getCurrency2Json( v_key ):
	''' Gets currency in json via code  '''
	v_arr = getCbrCurrenciesArray()
	json_txt =''
	if v_arr is None or v_key is None:
		return None  
	for v in v_arr:
		if v['NumCode'] == v_key:
			json_txt = json.dumps( v )
			break
	return json_txt


# for debug purposese
if __name__ == "__main__":

	print( getCbrCurrenciesArray() )	


