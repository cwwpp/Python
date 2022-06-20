import requests
import pyautogui

getIP = pyautogui.password('Enter IP: ')

response = requests.get('http://ip-api.com/json/' + getIP).json()

#print(response)

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
