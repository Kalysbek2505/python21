import requests

url = 'https://static.dw.com/image/5692524_4.jpg'
res = requests.get(url)
print(res.content)
name = 'photos/photo1.jpg'
with open(name, 'wb') as file:
    file.write(res.content)