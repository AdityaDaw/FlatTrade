import requests

sesurl = "https://authapi.flattrade.in/auth/session"
sesurl = "https://auth.flattrade.in/?app_key=8cac21d8da3c4430a357e16423d14d73&sid=8a64eb731815ad67e0649b64a843946d398a30c29f82fe714fad17711f74b46c"

ses = requests.Session()
respin = ses.post(sesurl)

sid = respin.headers

print(sid)