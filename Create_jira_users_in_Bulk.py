import requests
import json
import io
url='https://shantisingh.atlassian.net//rest/api/2/user'
header={
   "Accept": "application/json",
   "Content-Type": "application/json"
}
with io.open("userlist.csv","r",encoding='utf-8')as f1:
    user_data=f1.read()
    f1.close()
user_data=user_data.split("\n")[1:]
print(user_data)
i=0
while i<len(user_data)-1:
    displayName=user_data[i].split(",")[0] 
    email=user_data[i].split(",")[1]
    i=i+1
    payload=json.dumps(
        {
        "emailAddress":email,
        "displayName":displayName
        }
        )
    response=requests.post(url,headers=header,data=payload,auth=("shantisingh22@navgurukul.org","gXml6Z8qRVtil8papCpz1B68"))
    print(response.text)
