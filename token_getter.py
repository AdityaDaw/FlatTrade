import json
import requests
import time
import pyotp
import os
import requests
from urllib.parse import parse_qs,urlparse
import hashlib



APIKEY =    '8cac21d8da3c4430a357e16423d14d73'
secretKey = '2023.80807a86c1ee467ea36a3dbb25119e8fa082af04eb4b9e62'
totp_key= '3U3SU2TPECDQKRGFA364DIGSE47477FM'
password = 'Mita99*daw'
userid =  'FT032354'

passwordEncrpted =  hashlib.sha256(password.encode()).hexdigest()
ses = requests.Session()

sid = "02d1004f8e1033b2f0a9b6ee007dd7506206da7fab3f9b7c789a62e95ab43de3"


url2 = 'https://authapi.flattrade.in/ftauth'
payload = {"UserName":userid,"Password":passwordEncrpted,"PAN_DOB":pyotp.TOTP(totp_key).now(),"App":"","ClientID":"","Key":"","APIKey":APIKEY,"Sid":sid}
res2 = ses.post(url2, json=payload)
reqcodeRes = res2.json()
print(reqcodeRes)
parsed = urlparse(reqcodeRes['RedirectURL'])
reqCode = parse_qs(parsed.query)['code'][0]
api_secret =APIKEY+ reqCode + secretKey
api_secret =  hashlib.sha256(api_secret.encode()).hexdigest()
payload = {"api_key":APIKEY, "request_code":reqCode, "api_secret":api_secret}
url3 = 'https://authapi.flattrade.in/trade/apitoken'
res3 = ses.post(url3, json=payload)
print(res3.json())
token = res3.json()['token']
print(token)