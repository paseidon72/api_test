import requests

url = "https://api.chucknorris.io/jokes/random"
print(url)
result = requests.get(url)
print(str(result.status_code) + " : status code")
assert 200 == result.status_code
if result.status_code == 200:
    print("Very good!!!")
else:
    print("Bag?????????")
result.encoding = "utf-8"
print(result.text)
