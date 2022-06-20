import socket
import subprocess
import os 

class repeater():
    def repeaterCount():
        idecount = 0
        os.system('cls')
        cmdlist = ['help', 'cls', 'exit']

        while True:
            code = input('\033[1;32;40mIn [' + str(idecount) + "]: ")
            idecount +=1

            if code == cmdlist[0]:
                print('HELP   ALL COMMANDS')
                print('CLS    CLEAR THE SCREEN')
                print('EXIT   EXIT THE PROGRAM') 

            elif code == cmdlist[1]:
                idecount = 0
                os.system('cls')

            elif code == cmdlist[2]:
                break

            else:
                print(code)
repeater.repeaterCount()