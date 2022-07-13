import os
import time

# _________                             .__       .__     __   
# \_   ___ \  ____ ______ ___.__._______|__| ____ |  |___/  |_ 
# /    \  \/ /  _ \\____ <   |  |\_  __ \  |/ ___\|  |  \   __\
# \     \___(  <_> )  |_> >___  | |  | \/  / /_/  >   Y  \  |  
#  \______  /\____/|   __// ____| |__|  |__\___  /|___|  /__|  
#         \/       |__|   \/              /_____/      \/      
# .___                                    
# |   | ____  ____ ___.__.___________  ___
# |   |/ ___\/ __ <   |  |\___   /\  \/  /
# |   \  \__\  ___/\___  | /    /  >    < 
# |___|\___  >___  > ____|/_____ \/__/\_ \
#          \/    \/\/           \/      \/

# _______________   ________ ________  
# \_____  \   _  \  \_____  \\_____  \ 
#  /  ____/  /_\  \  /  ____/ /  ____/ 
# /       \  \_/   \/       \/       \ 
# \_______ \_____  /\_______ \_______ \
#         \/     \/         \/       \/

def packages():
	packages_choice = input('Download\x20packages\x20need?\x20[y/n]:\x20')

	if packages_choice == 'y':
		version_num = input('Are\x20using\x20python\x203?\x20[y/n]:\x20')

		if version_num == 'y':
			os.system('pip3 install colored')
			os.system('cls')

		else:
			os.system('pip install colored')
			os.system('cls')

	else:
		pass

packages()

from colored import fg, bg, attr

def hydrax():
	os.system('cls')
	print(fg(9) + '______________________________________________________________________________')
	print(fg(15) + '  ___ ___            .___             ', end='')
	print(fg(9) + '____  ___')
	print(fg(15) + ' /   |   \ ___.__. __| _/___________  ', end='')
	print(fg(9) + '\   \/  /')
	print(fg(15) + '/    ~    <   |  |/ __ |\_  __ \__  \  ', end='')
	print(fg(9) + '\     / ')
	print(fg(15) + '\    Y    /\___  / /_/ | |  | \// __ \_', end='')
	print(fg(9) + '/     \ ')
	print(fg(15) + ' \___|_  / / ____\____ | |__|  (____  /', end='')
	print(fg(9) + '___/\  \ ')
	print(fg(15) + '       \/  \/         \/            \/      ', end='')
	print(fg(9) + '\_/')
	print(fg(9) + '                 [', end='')
	print(fg(15) + 'V 1.0.0', end='')
	print(fg(9) + ']', end=' ')
	print(fg(15) + 'BY', end='')
	print(fg(15) + ':', end='')
	print(fg(15) + 'ICEYZX')

def info():
	print(fg(9) + '______________________________________________________________________________')
	print(fg(9) + '\n[', end='')
	print(fg(15) + '?', end='')
	print(fg(9) + ']', end=' ')
	print(fg(15) + 'Unlimited UC, diamonds, coins, etc... With HydraX.')
	print(fg(9) + '[!] The script owner DO NOT take any responsibility, use this at your own risk.')
	print(fg(9) + '______________________________________________________________________________\n')

def hack_menu():
	print(fg(9) + '[+] Select an option.')

	print(fg(9) + ' [', end='')
	print(fg(15) + '01', end='')
	print(fg(9) + ']', end=' ')
	print(fg(15) + 'PUBG MOBILE', end='     ')

	print(fg(9) + ' [', end='')
	print(fg(15) + '05', end='')
	print(fg(9) + ']', end=' ')
	print(fg(15) + 'ROBLOX')

	print(fg(9) + ' [', end='')
	print(fg(15) + '02', end='')
	print(fg(9) + ']', end=' ')
	print(fg(15) + 'FREE FIRE', end='       ')

	print(fg(9) + ' [', end='')
	print(fg(15) + '06', end='')
	print(fg(9) + ']', end=' ')
	print(fg(15) + 'POKEMON GO')

	print(fg(9) + ' [', end='')
	print(fg(15) + '03', end='')
	print(fg(9) + ']', end=' ')
	print(fg(15) + 'STANDOFF 2', end='      ')

	print(fg(9) + ' [', end='')
	print(fg(15) + '07', end='')
	print(fg(9) + ']', end=' ')
	print(fg(15) + '8 BALL POOL')

	print(fg(9) + ' [', end='')
	print(fg(15) + '04', end='')
	print(fg(9) + ']', end=' ')
	print(fg(15) + 'SUBWAY SURFER', end='   ')

	print(fg(9) + ' [', end='')
	print(fg(15) + '08', end='')
	print(fg(9) + ']', end=' ')
	print(fg(15) + 'STUMBLE GUYS')

def utility():
	print(fg(9) + '\n[+] Utility.')
	print(fg(9) + ' [', end='')
	print(fg(15) + 'E', end='')
	print(fg(9) + ']', end=' ')
	print(fg(15) + 'Exit', end='       ')

	print(fg(9) + '[', end='')
	print(fg(15) + 'H', end='')
	print(fg(9) + ']', end=' ')
	print(fg(15) + 'Help')
	
	print(fg(9) + ' [', end='')
	print(fg(15) + 'C', end='')
	print(fg(9) + ']', end=' ')
	print(fg(15) + 'Clear')
	print(fg(9) + '______________________________________________________________________________\n')

def user_input():
	while True:
		print(fg(15) + ' HydraX:', end='')
		print(fg(9) + '~', end='')
		print(fg(15) + '$', end=' ')
		option = input(fg(15) + '')

		if option == '1':
			print(fg(9) + '\n[+] PUBGM UC HACK')

			print(fg(9) + ' [', end='')
			print(fg(15) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'Account ID: ', end='')
			account_id = input(fg(15) + '')

			while True:
				print(fg(9) + ' [', end='')
				print(fg(15) + '*', end='')
				print(fg(9) + ']', end=' ')
				print(fg(15) + 'Enter number of UC (1 - 99999): ', end='')
				uc = input(fg(15) + '')

				if uc.isdigit() == True:
					if 1 <= int(uc) <= 99999:
						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Grabbing user id...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Generating UC...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + f'Sending {uc} UC to {account_id}...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						time.sleep(2)

						print(fg(46) + f'\n[+] Succesfully sent {uc} UC to {account_id}.\n')

						break

					else:
						print(fg(9) + "\n[x] Invalid Input.\n")

				else:
					print(fg(9) + '\n[x] Invalid Input.\n')

		elif option == '2':
			print(fg(9) + '\n[+] FREE FIRE DIAMONDS HACK')

			print(fg(9) + ' [', end='')
			print(fg(15) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'Account ID: ', end='')
			account_id = input(fg(15) + '')

			while True:
				print(fg(9) + ' [', end='')
				print(fg(15) + '*', end='')
				print(fg(9) + ']', end=' ')
				print(fg(15) + 'Enter number of Diamonds (1 - 99999): ', end='')
				diamonds = input(fg(15) + '')

				if diamonds.isdigit() == True:
					if 1 <= int(diamonds) <= 99999:
						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Grabbing user id...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Generating Diamonds...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + f'Sending {diamonds} Diamonds to {account_id}...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						time.sleep(2)

						print(fg(46) + f'\n[+] Succesfully sent {diamonds} Diamonds to {account_id}.\n')

						break

					else:
						print(fg(9) + "\n[x] Invalid Input.\n")

				else:
					print(fg(9) + '\n[x] Invalid Input.\n')

		elif option == '3':
			print(fg(9) + '\n[+] STANDOFF 2 GOLD HACK')

			print(fg(9) + ' [', end='')
			print(fg(15) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'Account ID: ', end='')
			account_id = input(fg(15) + '')

			while True:
				print(fg(9) + ' [', end='')
				print(fg(15) + '*', end='')
				print(fg(9) + ']', end=' ')
				print(fg(15) + 'Enter number of Gold (1 - 99999): ', end='')
				gold = input(fg(15) + '')

				if gold.isdigit() == True:
					if 1 <= int(gold) <= 99999:
						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Grabbing user id...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Generating Gold...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + f'Sending {gold} Gold to {account_id}...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						time.sleep(2)

						print(fg(46) + f'\n[+] Succesfully sent {gold} Gold to {account_id}.\n')

						break

					else:
						print(fg(9) + "\n[x] Invalid Input.\n")

				else:
					print(fg(9) + '\n[x] Invalid Input.\n')

		elif option == '4':
			print(fg(9) + '\n[+] SUBWAY SURFER COIN HACK')

			print(fg(9) + ' [', end='')
			print(fg(15) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'Account Username: ', end='')
			account_username = input(fg(15) + '')

			while True:
				print(fg(9) + ' [', end='')
				print(fg(15) + '*', end='')
				print(fg(9) + ']', end=' ')
				print(fg(15) + 'Enter number of Coins (1 - 999999): ', end='')
				coin = input(fg(15) + '')

				if coin.isdigit() == True:
					if 1 <= int(coin) <= 999999:
						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Grabbing user id...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Generating Coins...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + f'Sending {coin} Coins to {account_username}...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						time.sleep(2)

						print(fg(46) + f'\n[+] Succesfully sent {coin} Coins to {account_username}.\n')

						break

					else:
						print(fg(9) + "\n[x] Invalid Input.\n")

				else:
					print(fg(9) + '\n[x] Invalid Input.\n')

		elif option == '5':
			print(fg(9) + '\n[+] ROBUX HACK')

			print(fg(9) + ' [', end='')
			print(fg(15) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'Account Username: ', end='')
			account_username = input(fg(15) + '')

			while True:
				print(fg(9) + ' [', end='')
				print(fg(15) + '*', end='')
				print(fg(9) + ']', end=' ')
				print(fg(15) + 'Enter number of Robux (1 - 99999): ', end='')
				Robux = input(fg(15) + '')

				if Robux.isdigit() == True:
					if 1 <= int(Robux) <= 99999:
						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Grabbing user id...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Generating Robux...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + f'Sending {Robux} Robux to {account_username}...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						time.sleep(2)

						print(fg(46) + f'\n[+] Succesfully sent {Robux} Robux to {account_username}.\n')

						break

					else:
						print(fg(9) + "\n[x] Invalid Input.\n")

				else:
					print(fg(9) + '\n[x] Invalid Input.\n')

		elif option == '6':
			print(fg(9) + '\n[+] POKECOIN HACK')

			print(fg(9) + ' [', end='')
			print(fg(15) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'Account Username: ', end='')
			account_username = input(fg(15) + '')

			while True:
				print(fg(9) + ' [', end='')
				print(fg(15) + '*', end='')
				print(fg(9) + ']', end=' ')
				print(fg(15) + 'Enter number of Pokecoins (1 - 9999): ', end='')
				coin = input(fg(15) + '')

				if coin.isdigit() == True:
					if 1 <= int(coin) <= 9999:
						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Grabbing user id...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Generating Pokecoins...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + f'Sending {coin} Pokecoins to {account_username}...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						time.sleep(2)

						print(fg(46) + f'\n[+] Succesfully sent {coin} Pokecoins to {account_username}.\n')

						break

					else:
						print(fg(9) + "\n[x] Invalid Input.\n")

				else:
					print(fg(9) + '\n[x] Invalid Input.\n')

		elif option == '7':
			print(fg(9) + '\n[+] 8 BALL POOL COIN HACK')

			print(fg(9) + ' [', end='')
			print(fg(15) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'Account ID: ', end='')
			account_username = input(fg(15) + '')

			while True:
				print(fg(9) + ' [', end='')
				print(fg(15) + '*', end='')
				print(fg(9) + ']', end=' ')
				print(fg(15) + 'Enter number of Coins (1 - 999999): ', end='')
				coin = input(fg(15) + '')

				if coin.isdigit() == True:
					if 1 <= int(coin) <= 999999:
						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Grabbing user id...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Generating Coins...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + f'Sending {coin} Coins to {account_username}...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						time.sleep(2)

						print(fg(46) + f'\n[+] Succesfully sent {coin} Coins to {account_username}.\n')

						break

					else:
						print(fg(9) + "\n[x] Invalid Input.\n")

				else:
					print(fg(9) + '\n[x] Invalid Input.\n')

		elif option == '8':
			print(fg(9) + '\n[+] STUMBLE GUYS GEMS HACK')

			print(fg(9) + ' [', end='')
			print(fg(15) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'Account Username: ', end='')
			account_username = input(fg(15) + '')

			while True:
				print(fg(9) + ' [', end='')
				print(fg(15) + '*', end='')
				print(fg(9) + ']', end=' ')
				print(fg(15) + 'Enter number of Gems (1 - 99999): ', end='')
				gem = input(fg(15) + '')

				if gem.isdigit() == True:
					if 1 <= int(gem) <= 99999:
						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Grabbing user id...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + 'Generating Gems...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						print(fg(9) + ' [', end='')
						print(fg(15) + '*', end='')
						print(fg(9) + ']', end=' ')
						print(fg(15) + f'Sending {gem} Gems to {account_username}...', end=' ')

						time.sleep(4)

						print(fg(46) + 'Success')

						time.sleep(2)

						print(fg(46) + f'\n[+] Succesfully sent {gem} Gems to {account_username}.\n')

						break

					else:
						print(fg(9) + "\n[x] Invalid Input.\n")

				else:
					print(fg(9) + '\n[x] Invalid Input.\n')

		elif option == 'E':
			print(fg(46) + '')
			break

		elif option == 'H':
			print(fg(9) + '\n[', end='')
			print(fg(15) + '?', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'Unlimited UC, diamonds, etc... With HydraX.')
			print(fg(9) + '[!] The script owner DO NOT take any responsibility, use this at your own risk.\n')

		elif option == 'C':
			os.system('cls')
			print(fg(9) + '______________________________________________________________________________')
			print('  ___ ___            .___             ____  ___')
			print(' /   |   \ ___.__. __| _/___________  \   \/  /')
			print('/    ~    <   |  |/ __ |\_  __ \__  \  \     / ')
			print('\    Y    /\___  / /_/ | |  | \// __ \_/     \ ')
			print(' \___|_  / / ____\____ | |__|  (____  /___/\  \ ')
			print('       \/  \/         \/            \/      \_/')
			print(fg(9) + '                 [', end='')
			print(fg(15) + 'V 1.0.0', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'BY', end='')
			print(fg(15) + ':', end='')
			print(fg(15) + 'ICEYZX')

			print(fg(9) + '______________________________________________________________________________')
			print(fg(9) + '\n[', end='')
			print(fg(15) + '?', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'Unlimited UC, diamonds, coins, etc... With HydraX.')
			print(fg(9) + '[!] The script owner DO NOT take any responsibility, use this at your own risk.')
			print(fg(9) + '______________________________________________________________________________\n')

			print(fg(9) + '[+] Select an option.')

			print(fg(9) + ' [', end='')
			print(fg(15) + '01', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'PUBG UC')

			print(fg(9) + ' [', end='')
			print(fg(15) + '02', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'FREE FIRE DIAMONDS')

			print(fg(9) + ' [', end='')
			print(fg(15) + '03', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'STANDOFF 2 GOLD')

			print(fg(9) + '\n[+] Utility.')
			print(fg(9) + ' [', end='')
			print(fg(15) + 'E', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'Exit', end='       ')

			print(fg(9) + '[', end='')
			print(fg(15) + 'H', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'Help')
			
			print(fg(9) + ' [', end='')
			print(fg(15) + 'C', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'Clear')
			print(fg(9) + '______________________________________________________________________________\n')

		elif option == '':
			pass

		else:
			print(fg(9) + '\n[x] Invalid Input.\n')

hydrax()
info()
hack_menu()
utility()
user_input()
