import requests
import json
import io
url ='https://shantisingh.atlassian.net/rest/api/3/issue/SINGH-2/comment'
header={
    "Accept": "application/json",
   "Content-Type": "application/json"
}
data=json.dumps({"body": {
    "type": "doc",
    "version": 1,
    "content": [
      {
        "type": "paragraph",
        "content": [
          {
            "text": "comment-1 added by python",
            "type": "text"
          }
        ]
      }
    ]
  }
})
response=requests.post(url,headers=header,data=data,auth=("shantisingh22@navgurukul.org","gXml6Z8qRVtil8papCpz1B68"))
print(response.text)
