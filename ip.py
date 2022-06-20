import re, subprocess

class classIP():
    def ipGrab():
        ipConfig = subprocess.run(['ipconfig'], capture_output = True).stdout.decode()
        ipSearch = re.findall("IPv4 Address. . . . . . . . . . . : (.*)\r", ipConfig)
        ipSearch2 = re.findall("Default Gateway . . . . . . . . . : (.*)\r", ipConfig)
        personalIP = dict()
        personalIP["Device IP Address"] = ipSearch
        routerIP = dict()
        routerIP["Router IP Address"] = ipSearch2
        print(personalIP)
        print(routerIP)
classIP.ipGrab()
