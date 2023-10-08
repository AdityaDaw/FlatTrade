
#set token and user id
#paste the token generated using the login flow described 
# in LOGIN FLOW of https://pi.flattrade.in/docs
token='d3c4848282de216e8c630ddc740d9a6924726f38f10be30a990417f3e5ea753b'
password = 'Mita99*daw'
userid =  'FT032354'

from NorenRestApiPy.NorenApi import  NorenApi

class FlatTradeApiPy(NorenApi):
    def __init__(self):
         NorenApi.__init__(self, host='https://piconnect.flattrade.in/PiConnectTP/', websocket='wss://piconnect.flattrade.in/PiConnectWSTp/', eodhost='https://web.flattrade.in/chartApi/getdata/')

api = FlatTradeApiPy()




ret = api.set_session(userid= userid, password = password, usertoken= token)

print(api.get_limits())

exch  = 'NFO'
query = 'NIFTY 26OCT CE'
ret = api.searchscrip(exchange=exch, searchtext=query)
import pandas as pd
df = pd.DataFrame.from_dict(ret['values'])
print(df["optt"])