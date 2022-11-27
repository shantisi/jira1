import requests
import json
import io
url='https://shantisingh.atlassian.net/rest/api/3/issue/SINGH-38/assignee'
header={
   "Accept": "application/json",
   "Content-Type": "application/json"
}
payload=json.dumps({
    "accountId": "6380f327213a315af3477338"
}
)
response=requests.put(url,headers=header,data=payload,auth=("shantisingh22@navgurukul.org","CMuKNofdfGFvrg6Rimr599E0"))
print(response.text)


