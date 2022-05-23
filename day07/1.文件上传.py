import requests

url = "http://httpbin.org/post"

files = {'file': open('haha.mp3', "rb")}

r = requests.post(url, files)
print(r.text)
