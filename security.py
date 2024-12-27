import json
def checkPassword(request, dic,credentials):
    if dic.get("password","1") == credentials.get(request.remote_addr,"2"): return True
    return False
