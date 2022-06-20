import requests

IP = input('IP: ')

class classIP():
    def getIP(self, x):
        response = requests.get('http://ip-api.com/json/' + x).json()
        #print(response)
        print("Country: " + response['country'])
        print('Country Code: ' + response['countryCode'])
        print("City: " + response['city'])
        print('Timezone: ' + response['timezone'])
        print("Latitude: " + str(response['lat']))
        print("Longitude: " + str(response['lon']))
        print("ISP: " + str(response['isp']))
        print('Organization : ' + response['org'])
        print('AS: ' + response['as'])

cIP = classIP()
cIP.getIP(IP)
