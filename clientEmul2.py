import json
import requests
# with open("scale_1200.jpg","rb") as file:
#     file={"file":file.read()}
data = {"id":"0","name":"testDe","password":"pass","commands":["123","456"],"cmDescription":["abc","def"],
        "dvDescription":"Test"}
# print(json.loads(json.dumps(data)))
res=requests.post("http://192.168.1.22:5000/api/user/getDevices/",json=json.dumps(data))
# with open("xxx.jpg","wb") as file:
#     file.write(res.con)
print(res.text)