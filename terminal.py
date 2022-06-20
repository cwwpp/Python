import subprocess, platform, socket, time, os

class Terminal():
	def terminalStart():
		os.system('cls')
		print("\033[1;32;40m********************************************")
		print("\033[1;32;40mWelcome To Iceyzx's Terminal [Version 1.0.0]")
		print("\033[1;32;40m********************************************")
	
	def terminalSetup():
		path = 'C:/'
		host_name = socket.gethostname()
		host_ip = socket.gethostbyname(host_name)
		while True:
			code = input('\033[1;32;40m~/Iceyzx-Terminal\u001b[37m$ ')

			if code == 'cmd':
				print("\033[1;32;40m********************************************")
				print("\033[1;32;40mWelcome To Iceyzx's Terminal [Version 1.0.0]")
				print("\033[1;32;40m********************************************")
			
			elif code == 'help':
				print("\033[1;32;40mHELP      ALL COMMANDS")
				print('CMD       TERMINAL VERSION')
				print('PING      PING A WEBSITE')
				print('LOCAL     LOCAL IP ADDRESS AND DESKTOP NAME')
				print('LS        DISPLAYS ALL THE FILES AND DIRECTORY')
				print('DATE      DISPLAYS THE DATE')
				print('CLS       CLEAR THE SCREEN')
				print('ECHO      DISPLAYS THE TEXT ENTERED')
				print('SUM       PRINTS THE SUM OF 2 INT')
				print('START     START A PROGRAM')
				print('COUNT     COUNT FROM 1 TILL THE NUMBER YOU ENTERED')
				print('CREATOR   SHOW WHO MADE THIS TERMINAL')
				print('EXIT      EXIT THE TERMINAL')

			elif code == 'ping':
				host = input('\033[1;32;40mEnter Website To Ping: ')
				number = input("Enter How Many Times To Ping: ")

				def ping(host):
					param = '-n' if platform.system().lower() == 'windows' else "-c"
					command = ['ping', param, number, host]
					return subprocess.call(command)
				print(ping(host))

			elif code == 'local':
				print('\033[1;32;40mYour Local IP Is: ' + host_ip)
				print('Your Desktop Name Is: ' + host_name)

			elif code == 'date':
				print('\033[1;32;40mThe Local Date Is: ' + time.strftime("%d/%m/20%y"))

			elif code == 'ls':
				dir_list = os.listdir(path)
				print('\033[1;32;40mFiles and Directory in', path, ': ')
				print(dir_list)

			elif code == 'echo':
				echo = input("\033[1;32;40mContext: ")
				print(echo)

			elif code == 'count':
				timecount = 0
				print('Choose a number')
				num = int(input(''))

				while 3>2:
					timecount+=1
					print(timecount)
					if timecount == num:
						print('Finished counting')
						break

			elif code == 'creator':
				print('\033[1;32;40mMade By Iceyzx')

			elif code == 'sum':
				first_num = input('Enter the first number: ')
				second_num = input('Enter the second number: ')

				try:
					checkint1 = int(first_num)
					checkint2 = int(second_num)
					result = checkint1 + checkint2
					print(result)
					
				except:
					print('Please enter an integer')

			elif code == 'start':
				prg = input('Program: ')
				os.system(prg + '.exe')

			elif code == 'cls':
				os.system('cls')
				print("\033[1;32;40m********************************************")
				print("\033[1;32;40mWelcome To Iceyzx's Terminal [Version 1.0.0]")
				print("\033[1;32;40m********************************************")

			elif code == 'exit':
				os.system('cls')
				quit()

			elif code == "" or code == " " or code == "  " or code == "   " or code == "     ":
				pass

			else:
				print('Iceyzx-Terminal: ' + code, 'is not a valid command')
Terminal.terminalStart()
Terminal.terminalSetup()