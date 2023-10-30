
#set token and user id
#paste the token generated using the login flow described 
# in LOGIN FLOW of https://pi.flattrade.in/docs
import pandas as pd
def get_time(time_string):
    import time
    data = time.strptime(time_string,'%d-%m-%Y %H:%M:%S')
    return time.mktime(data)


token='25ae661bd03cdd6b84f942f3aa847f2ac6ab9a7196e6fc0b0670f81859ba8143'
password = 'Mita99*daw'
userid =  'FT032354'

from NorenRestApiPy.NorenApi import  NorenApi
from api_helper import get_time

class FlatTradeApiPy(NorenApi):
    def __init__(self):
         NorenApi.__init__(self, host='https://piconnect.flattrade.in/PiConnectTP/', websocket='wss://piconnect.flattrade.in/PiConnectWSTp/', eodhost='https://web.flattrade.in/chartApi/getdata/')

api = FlatTradeApiPy()




ret = api.set_session(userid= userid, password = password, usertoken= token)

if ret != None:
     print("Not none")
     print(ret)
     start_time = "30-10-2023 09:10:00"
    #end_time = time.time()
    
     start_secs = get_time(start_time)

     end_time = get_time("30-10-2023 09:20:00")
     ret = api.get_time_price_series(exchange='NSE', token='26000', starttime=start_secs, endtime=end_time)
    
     df = pd.DataFrame.from_dict(ret)
     print(df)            
     print(f'{start_secs} to {end_time}')
else:
     print("value is None")
