import requests
import json
import io
url ='https://shantisingh.atlassian.net/rest/api/3/issue/SINGH-2/attachments'
header={
    "X-Atlassian-Token": "no-check"
}
files={"file":("userlist.csv",open("userlist.csv","rb"))}
response=requests.post(url,headers=header,files=files,auth=("shantisingh22@navgurukul.org","gXml6Z8qRVtil8papCpz1B68"))
print(response.text)

