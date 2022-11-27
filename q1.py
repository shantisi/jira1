import requests
import json
url='https://shantisingh.atlassian.net//rest/api/2/issue'
header={
   "Accept": "application/json",
   "Content-Type": "application/json"
}
payload=json.dumps({
    "fields": {
       "project":
       {
          "key": "SINGH"
       },
       "summary": "REST ye merry gentlemen.",
       "description": "Creating of an issue using project keys and issue type names using the REST API",
       "issuetype": {
          "name": "Task"
       }
   }
}
)
response=requests.post(url,headers=header,data=payload,auth=("shantisingh22@navgurukul.org","CMuKNofdfGFvrg6Rimr599E0"))
print(response.text)


