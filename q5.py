import requests
import json
import io
url ='https://shantisingh.atlassian.net/rest/api/3/issue/SINGH-1/comment'
header={
    "Accept": "application/json",
   "Content-Type": "application/json"
}

response=requests.get(url,headers=header,auth=("shantisingh22@navgurukul.org","gXml6Z8qRVtil8papCpz1B68"))
data=response.json()
print(data["total"])
with io.open("comments.csv","w",encoding="utf-8")as f1:
  for comments in data["comments"]:
    f1.write(comments["id"]+","+comments["body"]["content"][0]["content"][0]["text"])
  f1.close()    