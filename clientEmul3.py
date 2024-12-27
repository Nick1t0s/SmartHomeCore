import json
import requests
# with open("scale_1200.jpg","rb") as file:
#     file={"file":file.read()}
data = {"password":"pass", "ipDev":"192.168.1.22", "command": ["du hast1,adsf"]}
print(json.loads(json.dumps(data)))
res=requests.post("http://192.168.1.22:5000/api/user/writeCMD/",json=json.dumps(data))
# with open("xxx.jpg","wb") as file:
#     file.write(res.con)
print(res.text)