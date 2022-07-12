from colored import fg, bg, attr
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

# Fake hack tool to impress your friends (harmless)

# Install 'colored' module in order to run this script
# To install, type this command in your terminal:
# pip install colored

def black_pearl():
	print(fg(9) + '______________________________________________________________________________')
	print(fg(14) + '__________.__                 __     ', end='')
	print(fg(9) + '__________                     .__   ')
	print(fg(14) + '\______   \  | _____    ____ |  | __ ', end='')
	print(fg(9) + '\______   \ ____  _____ _______|  |  ')
	print(fg(14) + ' |    |  _/  | \__  \ _/ ___\|  |/ /  ', end='')
	print(fg(9) + '|     ___// __ \ \__  \\_  __ \   |  ')
	print(fg(14) + ' |    |   \  |__/ __ \\  \___ |    <   ', end='')
	print(fg(9) + '|    |   \  ___/ / __ \|  | \/   |__')
	print(fg(14) + ' |______  /____(____  /\___  >__|_ \  ', end='')
	print(fg(9) + "|____|    \___  >____  /__|  |____/")
	print(fg(14) + '        \/          \/     \/     \/                ', end='')
	print(fg(9) + '\/     \/')
	print(fg(9) + '                                                [', end='')
	print(fg(15) + 'V 1.0.0', end='')
	print(fg(9) + ']', end=' ')
	print(fg(15) + 'BY', end='')
	print(fg(14) + ':', end='')
	print(fg(15) + 'ICEYZX')

def info():
	print(fg(9) + '______________________________________________________________________________')
	print(fg(9) + '\n[', end='')
	print(fg(14) + '?', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Take down social media accounts with Black Pearl.')
	print(fg(9) + '[!] The script owner DO NOT take any responsibility, use this at your own risk.')
	print(fg(9) + '______________________________________________________________________________\n')

def hack_menu():
	print(fg(9) + '[+] Select an option.')

	print(fg(9) + ' [', end='')
	print(fg(14) + '01', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Facebook', end='   ')

	print(fg(9) + '[', end='')
	print(fg(14) + '09', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Yahoo')

	print(fg(9) + ' [', end='')
	print(fg(14) + '02', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Youtube', end='    ')

	print(fg(9) + '[', end='')
	print(fg(14) + '10', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Microsoft')

	print(fg(9) + ' [', end='')
	print(fg(14) + '03', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Instagram', end='  ')

	print(fg(9) + '[', end='')
	print(fg(14) + '11', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'PlayStation')

	print(fg(9) + ' [', end='')
	print(fg(14) + '04', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Github', end='     ')

	print(fg(9) + '[', end='')
	print(fg(14) + '12', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Netflix')

	print(fg(9) + ' [', end='')
	print(fg(14) + '05', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Gitlab', end='     ')

	print(fg(9) + '[', end='')
	print(fg(14) + '13', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Reddit')

	print(fg(9) + ' [', end='')
	print(fg(14) + '06', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Twitter', end='    ')

	print(fg(9) + '[', end='')
	print(fg(14) + '14', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'VK')

	print(fg(9) + ' [', end='')
	print(fg(14) + '07', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Snapchat', end='   ')

	print(fg(9) + '[', end='')
	print(fg(14) + '15', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Steam')

	print(fg(9) + ' [', end='')
	print(fg(14) + '08', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Xbox', end='       ')

	print(fg(9) + '[', end='')
	print(fg(14) + '16', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'WordPress')

def utility():
	print(fg(9) + '\n[+] Utility.')
	print(fg(9) + ' [', end='')
	print(fg(14) + 'E', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Exit', end='       ')

	print(fg(9) + '[', end='')
	print(fg(14) + 'H', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Help')
	
	print(fg(9) + ' [', end='')
	print(fg(14) + 'C', end='')
	print(fg(9) + ']', end=' ')
	print(fg(14) + 'Clear')
	print(fg(9) + '______________________________________________________________________________\n')

def user_input():
	while True:
		print(fg(14) + 'BlackPearl:', end='')
		print(fg(9) + '~', end='')
		print(fg(14) + '$', end=' ')
		option = input(fg(15) + '')

		if option == '1':
			print(fg(9) + "\n[+] FACEBOOK HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == '2':
			print(fg(9) + "\n[+] YOUTUBE HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == '3':
			print(fg(9) + "\n[+] INSTAGRAM HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == '4':
			print(fg(9) + "\n[+] GTIHUB HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == '5':
			print(fg(9) + "\n[+] GITLAB HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == '6':
			print(fg(9) + "\n[+] TWITTER HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == '7':
			print(fg(9) + "\n[+] SNAPCHAT HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == '8':
			print(fg(9) + "\n[+] XBOX HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == '9':
			print(fg(9) + "\n[+] YAHOO HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == '10':
			print(fg(9) + "\n[+] MICROSOFT HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == '11':
			print(fg(9) + "\n[+] PLAYSTATION HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == '12':
			print(fg(9) + "\n[+] NETFLIX HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == '13':
			print(fg(9) + "\n[+] REDDIT HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == '14':
			print(fg(9) + "\n[+] VK HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == '15':
			print(fg(9) + "\n[+] STEAM HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == '16':
			print(fg(9) + "\n[+] WORDPRESS HACK")

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Username: ', end='')
			username = input(fg(15) + '')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + f'Logging in as {username}...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Grabbing user id...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			print(fg(9) + ' [', end='')
			print(fg(14) + '*', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Deleting account...', end=' ')

			time.sleep(4)

			print(fg(46) + 'Success')

			time.sleep(2)

			print(fg(46) + '\n[+] Account Successfully Deleted.\n')

		elif option == 'E':
			print(fg(46) + '')
			break

		elif option == 'H':
			print(fg(9) + '\n[', end='')
			print(fg(14) + '?', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Take down social media accounts with Black Pearl.')
			print(fg(9) + '[!] The script owner DO NOT take any responsibility, use this at your own risk.\n')

		elif option == 'C':
			os.system('cls')
			print(fg(9) + '______________________________________________________________________________')
			print(fg(14) + '__________.__                 __     ', end='')
			print(fg(9) + '__________                     .__   ')
			print(fg(14) + '\______   \  | _____    ____ |  | __ ', end='')
			print(fg(9) + '\______   \ ____  _____ _______|  |  ')
			print(fg(14) + ' |    |  _/  | \__  \ _/ ___\|  |/ /  ', end='')
			print(fg(9) + '|     ___// __ \ \__  \\_  __ \   |  ')
			print(fg(14) + ' |    |   \  |__/ __ \\  \___ |    <   ', end='')
			print(fg(9) + '|    |   \  ___/ / __ \|  | \/   |__')
			print(fg(14) + ' |______  /____(____  /\___  >__|_ \  ', end='')
			print(fg(9) + "|____|    \___  >____  /__|  |____/")
			print(fg(14) + '        \/          \/     \/     \/                ', end='')
			print(fg(9) + '\/     \/')
			print(fg(9) + '                                                [', end='')
			print(fg(15) + 'V 1.0.0', end='')
			print(fg(9) + ']', end=' ')
			print(fg(15) + 'BY', end='')
			print(fg(14) + ':', end='')
			print(fg(15) + 'ICEYZX')

			print(fg(9) + '______________________________________________________________________________')
			print(fg(9) + '\n[', end='')
			print(fg(14) + '?', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Take down social media accounts with Black Pearl.')
			print(fg(9) + '[!] The script owner DO NOT take any responsibility, use this at your own risk.')
			print(fg(9) + '______________________________________________________________________________\n')

			print(fg(9) + '[+] Select an option.')

			print(fg(9) + ' [', end='')
			print(fg(14) + '01', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Facebook', end='   ')

			print(fg(9) + '[', end='')
			print(fg(14) + '09', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Yahoo')

			print(fg(9) + ' [', end='')
			print(fg(14) + '02', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Youtube', end='    ')

			print(fg(9) + '[', end='')
			print(fg(14) + '10', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Microsoft')

			print(fg(9) + ' [', end='')
			print(fg(14) + '03', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Instagram', end='  ')

			print(fg(9) + '[', end='')
			print(fg(14) + '11', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'PlayStation')

			print(fg(9) + ' [', end='')
			print(fg(14) + '04', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Github', end='     ')

			print(fg(9) + '[', end='')
			print(fg(14) + '12', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Netflix')

			print(fg(9) + ' [', end='')
			print(fg(14) + '05', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Gitlab', end='     ')

			print(fg(9) + '[', end='')
			print(fg(14) + '13', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Reddit')

			print(fg(9) + ' [', end='')
			print(fg(14) + '06', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Twitter', end='    ')

			print(fg(9) + '[', end='')
			print(fg(14) + '14', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'VK')

			print(fg(9) + ' [', end='')
			print(fg(14) + '07', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Snapchat', end='   ')

			print(fg(9) + '[', end='')
			print(fg(14) + '15', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Steam')

			print(fg(9) + ' [', end='')
			print(fg(14) + '08', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Xbox', end='       ')

			print(fg(9) + '[', end='')
			print(fg(14) + '16', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'WordPress')

			print(fg(9) + '\n[+] Utility.')
			print(fg(9) + ' [', end='')
			print(fg(14) + 'E', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Exit', end='       ')

			print(fg(9) + '[', end='')
			print(fg(14) + 'H', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Help')
			
			print(fg(9) + ' [', end='')
			print(fg(14) + 'C', end='')
			print(fg(9) + ']', end=' ')
			print(fg(14) + 'Clear')
			print(fg(9) + '______________________________________________________________________________\n')

black_pearl()
info()
hack_menu()
utility()
user_input()
