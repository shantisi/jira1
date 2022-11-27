import requests
import json
import io
url='https://shantisingh.atlassian.net/rest/api/3/issue/SINGH-33/transitions'
header={
   "Accept": "application/json",
   "Content-Type": "application/json"
}

payload=json.dumps(
   {
    
    "transition": {
        "id": "21"
    }
}
        
)
response=requests.post(url,headers=header,data=payload,auth=("shantisingh22@navgurukul.org","nRV0AiIkK1XIYCm6yopu272A"))
print(response.text)
