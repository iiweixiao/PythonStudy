import requests

url = 'http://httpbin.org/post'

data = {'file': open('/Users/abc/PycharmProjects/pythonStudy/day07/haha.mp3', 'rb')}

r = requests.post(url, data)
print(r.text)