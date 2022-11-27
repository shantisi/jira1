import requests
import json
import io
url ='https://shantisingh.atlassian.net/rest/api/3/issue/SINGH-1/comment/10006'
header={
    "Accept": "application/json",
   "Content-Type": "application/json"
}   
response=requests.delete(url,headers=header,auth=("shantisingh22@navgurukul.org","gXml6Z8qRVtil8papCpz1B68"))
print(response.text)
