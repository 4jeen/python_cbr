import redis
import exchangeRates as er

r = redis.Redis(host='redisdb', decode_responses = True )
glKey = 'ExchangeRatesJson'
TTL=3600


def putRates2redis(rt):
	cDate=er.getCbrCurrenciesDate()
	with r.pipeline() as pipe:
		for el in rt:
			el['@Date'] = cDate
			pipe.set("CURR_"+el['CharCode'],er.currency2Json(el),3600)			
		pipe.execute()	

def currencyKeysExists():
	c = 0
	for k in r.keys("CURR_*"):
		if r.exists(k) == 0:
			break
		else: 
			c =+ 1	
	if c >= 33:
		return True
	return False		


def getRatesArrayFromRedis():
	if not currencyKeysExists():
		putRates2redis(er.getCbrCurrenciesArray())
	str='['
	for k in r.keys("CURR_*"):
		str += r.get(k) + ","
	str = str [:-1] + ']'
	return str

def getRates():
	if r.exists( glKey ) == 1 :
		return r.get( glKey )
	else:
		r.set(  glKey , er.getCbrExchangeRates2Json()  )
		r.expire( glKey  , TTL)
		return r.get( glKey ) 

# for debug purposese
if __name__ == "__main__":
	print(getRatesFromRedis())
	
