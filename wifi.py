import subprocess
import re

commandLine = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

profileNames = (re.findall("    All User Profile     : (.*)\r", commandLine))
               
wifiList = list()

if len(profileNames) != 0:
    for name in profileNames:
        wifiProfile = dict()

        profileInfo = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

        if re.search("    Security key           : Absent", profileInfo):
                           Continue

        else:
            wifiProfile["ssid"] = name

            profileInfoPass = subprocess.run(["netsh", "wlan", "show", "profiles", name, "key=clear"], capture_output = True).stdout.decode()

            password = re.search("    Key Content            : (.*)\r", profileInfoPass)

            if password == None:
                wifiProfile["password"] = None

            else:
                wifiProfile["password"] = password[1]

                wifiList.append(wifiProfile)
for x in range(len(wifiList)):
    print(wifiList[x])