import requests

BASE = "http://127.0.0.1:5000/"


data = [{"likes":10, "name":"Tim", "views":10000},
        {"likes":78, "name":"How to Make REst API", "views":34555},
        {"likes":10, "name":"John Dick", "views":2000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/"+ str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/2")
print(response.json())
