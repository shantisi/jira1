import requests
import json
import io
url ='https://shantisingh.atlassian.net/rest/api/3/search'
header={
    "Accept": "application/json",
   "Content-Type": "application/json"
}
query={
    'jql':"project=SINGH"
}
    
response=requests.get(url,headers=header,params=query,auth=("shantisingh22@navgurukul.org","gXml6Z8qRVtil8papCpz1B68"))
print(response.text)
data=response.json()
issues=data["issues"]
for issue in issues:
    print(issue["key"])
