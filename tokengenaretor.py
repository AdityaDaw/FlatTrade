import json
import requests
import time
import pyotp
import os
import requests
from urllib.parse import parse_qs,urlparse
import hashlib

APIKEY =    '8cac21d8da3c4430a357e16423d14d733'
secretKey = '2023.80807a86c1ee467ea36a3dbb25119e8fa082af04eb4b9e622'
totp_key= '3U3SU2TPECDQKRGFA364DIGSE47477FMK'
password = 'Nothing'
userid =  'FT032355'
passwordEncrpted =  hashlib.sha256(password.encode()).hexdigest()

url = f"https://auth.flattrade.in/?app_key={APIKEY}"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

ses = requests.Session()
res_pin = ses.get(url)
rt2 = ses.get_redirect_target(res_pin)

sid = "32bb2106a32f1a0b97839b6467bf29a0c7ea412bde6b73792ea8baf296712327"

url2 = 'https://authapi.flattrade.in/ftauth'
payload = {"UserName":userid,"Password":passwordEncrpted,"PAN_DOB":pyotp.TOTP(totp_key).now(),"App":"","ClientID":"","Key":"","APIKey":APIKEY,"Sid":sid}
res2 = ses.post(url2, json=payload)
reqcodeRes = res2.json()
# print(reqcodeRes)
parsed = urlparse(reqcodeRes['RedirectURL'])
reqCode = parse_qs(parsed.query)['code'][0]

api_secret =APIKEY+ reqCode + secretKey
api_secret =  hashlib.sha256(api_secret.encode()).hexdigest()
payload = {"api_key":APIKEY, "request_code":reqCode, "api_secret":api_secret}
url3 = 'https://authapi.flattrade.in/trade/apitoken'
res3 = ses.post(url3, json=payload)
# print(res3.json())
token = res3.json()['token']
print(token)

