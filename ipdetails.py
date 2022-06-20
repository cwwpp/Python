import requests
import os
import re
import pyautogui

getIP = pyautogui.password('Enter IP: ')

response = requests.get('http://ip-api.com/json/' + getIP).json()

#print(response)

def tracertIP():
    tracertLine = 'tracert -h 5 ' + str(getIP)
    tracertCmd = os.system(tracertLine)

def pingIP():
    pingLine = 'ping ' + str(getIP)
    pingCmd = os.system(pingLine)

print('IP: ' + str(getIP))
print("Country: " + response['country'])
print('Country Code: ' + response['countryCode'])
print("City: " + response['city'])
print('Timezone: ' + response['timezone'])
print("Latitude: " + str(response['lat']))
print("Longitude: " + str(response['lon']))
print("ISP: " + str(response['isp']))
print('Organization : ' + response['org'])
print('AS: ' + response['as'])

#tracertIP()

#def netstatIP():
#    netstatLine = 'netstat -n ' + str(getIP)
#    netstatCmd = os.system(netstatLine)

#pingIP()



#netstatIP()













#101.53.52.5
#113.173.78.40 (iceyzx)
#42.118.57.248 (zalo)
#173.244.36.41 (us ytber)
#117.234.15.54 (indian ytber)

# https://tools.keycdn.com/geo
# https://iplogger.org/ | https://iplogger.org/logger/wpsf3fnCute1/