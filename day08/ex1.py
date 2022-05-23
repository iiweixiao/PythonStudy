from requests import Request, Session
url = 'http://httpbin.org/post'
data = {
    'name': 'Bruce'
}
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"}
req = Request('POST', url, data=data, headers=headers )

ss = Session()

red = ss.prepare_request(req)
r = ss.send(red)
print(r.text)