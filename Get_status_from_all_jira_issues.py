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
data=response.json()
issues=data["issues"]
for issue in issues:
    issue_key=issue["key"]
    url1="https://shantisingh.atlassian.net/rest/api/3/issue/"+issue_key
    response=requests.get(url1,headers=header,auth=("shantisingh22@navgurukul.org","gXml6Z8qRVtil8papCpz1B68"))
    data=response.json()
    print(f'issue id is {issue_key} and status is {data["fields"]["status"]["name"]}')
