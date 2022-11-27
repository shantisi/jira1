import requests
import json
url='https://shantisingh.atlassian.net/rest/api/3/users/search'
header={
   "Accept": "application/json",
   "Content-Type": "application/json"
}

response=requests.get(url,headers=header,auth=("shantisingh22@navgurukul.org","4bR479R36cGhrzjoDel90FC5"))
data=response.json()
print(len(data))
for users in data:
    print(users["displayName"])
