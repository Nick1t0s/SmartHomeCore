import pandas as pd
import dt
import json
def getDF():
    devicesDF=pd.DataFrame({"ip": [],
                              "name": [],
                              "commands": [],
                              "cmDescription": [],
                              "dvDescription": [],
                              "lastConnection": [],
                              "commandsToRun": []})
    return devicesDF

def writeDevice(request,devicesDF,dic):
    devicesDFSorted = devicesDF[devicesDF["ip"]==request.remote_addr]
    print(devicesDFSorted["commandsToRun"].tolist())
    commandsToExecute = devicesDFSorted["commandsToRun"].tolist()
    if commandsToExecute == []:
        commandsToExecute = ""
    else:
        commandsToExecute = ",".join(commandsToExecute)
    # print(commandsToExecute)
    listForWrite=[request.remote_addr, dic["name"],  # ID, IP, NAME
                  ",".join(dic["commands"]) if type(dic["commands"]) == list else dic["commands"],  # Commands
                  ",".join(dic["cmDescription"]) if type(dic["cmDescription"]) == list else dic["cmDescription"],
                  dic["dvDescription"], dt.getStrTimeNow(True),
                  commandsToExecute]
    if len(devicesDFSorted) == 0:
        # print(listForWrite)
        devicesDF.loc[devicesDF.shape[0]] = listForWrite
    else:
        devicesDF.loc[devicesDF["ip"] == request.remote_addr] = listForWrite
    return devicesDF

def writeCommand(request,devicesDF,dic):
    ips = devicesDF['ip'].tolist()
    ipDev = dic.get("ipDev", "nip")
    if ipDev in ips:
        new_val = devicesDF.loc[devicesDF['ip'] == ipDev].iloc[0].to_list()
        commands = list(map(lambda x: x+":"+request.remote_addr, dic["command"][0].split(",")))
        print(commands)
        new_val[6] = ",".join(new_val[6].split(",")+commands).strip(",")
        devicesDF.loc[devicesDF["ip"] == ipDev] = new_val
        return {"hello": "ok"}
    else:
        return {"hello":"noIP"}
