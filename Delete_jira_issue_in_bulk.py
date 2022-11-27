import requests
import json
import io
header={
   "Accept": "application/json",
   "Content-Type": "application/json"
}
with io.open("issue_delete.csv","r",encoding="utf-8")as f1:
    data=f1.read()
data=data.split("\n")
for id in data:
    url='https://shantisingh.atlassian.net/rest/api/3/issue/'+id
    response=requests.delete(url,headers=header,auth=("shantisingh22@navgurukul.org","CMuKNofdfGFvrg6Rimr599E0"))
# print(response.text)


