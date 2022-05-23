import requests

url = 'http://f3.htqyy.com/play9/33/mp3/6'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

r = requests.get(url, headers=headers).content

with open('./haha.mp3', 'wb') as f:
    f.write(r)
