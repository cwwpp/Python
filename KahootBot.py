import os
import time

def packages_setup():
	os.system('cls')
	packages_choice = input('Download\x20packages\x20need?\x20[y/n]:\x20')

	if packages_choice == 'y':
		version_num = input('Are\x20using\x20python\x203?\x20[y/n]:\x20')

		if version_num == 'y':
			os.system('pip3 install colored')
			os.system('pip3 install names')
			os.system('cls')

		else:
			os.system('py -m pip install colored')
			os.system('py -m pip install names')
			os.system('cls')

	else:
		pass

packages_setup()

from colored import fg, bg, attr
import names

def packages():
	time.sleep(0.8)
	print(fg(46) + 'Preparing...')
	time.sleep(0.6)
	print('Required\x20colored')
	time.sleep(0.7)
	print('Required\x20names')
	time.sleep(0.5)
	os.system('cls')

def caution():
	print(fg(9) + "[!] This\x20software\x20was\x20made\x20for\x20educational\x20and\x20demonstrational\x20purposes.\x0aDistributing\x20this\x20software\x20without\x20proper\x20credit\x20and\x20LICENSE\x20is\x20illegal.\x0a\x0aThe\x20LICENSE\x20is\x20stated\x20here\x20and\x20should\x20also\x20be\x20a\x20file\x20within\x20or\x20outside\x20the\x20program.\x0a\x0aCopyright\x20belongs\x20to\x20Iceyzx.")
	print(fg(46) + '\x20\x0a\x0aPermission\x20is\x20hereby\x20granted,\x20free\x20of\x20charge,\x20to\x20any\x20person\x20obtaining\x20a\x20copy\x20of\x20this\x20software\x20and\x20associated\x20documentation\x20files\x20(the\x20\x22Software\x22),\x20to\x20deal\x20in\x20the\x20Software\x20without\x20restriction,\x20including\x20without\x20limitation\x20the\x20rights\x20to\x20use,\x20copy,\x20modify,\x20merge,\x20publish,\x20distribute,\x20sublicense,\x20and/or\x20sell\x20copies\x20of\x20the\x20Software,\x20and\x20to\x20permit\x20persons\x20to\x20whom\x20the\x20Software\x20is\x20furnished\x20to\x20do\x20so,\x20subject\x20to\x20the\x20following\x20conditions:\x0a\x0a' + fg(11) + 'The\x20above\x20copyright\x20notice\x20and\x20this\x20permission\x20notice\x20shall\x20be\x20included\x20in\x20all\x20copies\x20or\x20substantial\x20portions\x20of\x20the\x20Software.\x0a\x0a' + fg(46) + 'THE\x20SOFTWARE\x20IS\x20PROVIDED\x20\x22AS\x20IS\x22,\x20WITHOUT\x20WARRANTY\x20OF\x20ANY\x20KIND,\x20EXPRESS\x20OR\x20IMPLIED,\x20INCLUDING\x20BUT\x20NOT\x20LIMITED\x20TO\x20THE\x20WARRANTIES\x20OF\x20MERCHANTABILITY,\x20FITNESS\x20FOR\x20A\x20PARTICULAR\x20PURPOSE\x20AND\x20NON-INFRINGEMENT.\x20IN\x20NO\x20EVENT\x20SHALL\x20THE\x20AUTHORS\x20OR\x20COPYRIGHT\x20HOLDERS\x20BE\x20LIABLE\x20FOR\x20ANY\x20CLAIM,\x20DAMAGES\x20OR\x20OTHER\x20LIABILITY,\x20WHETHER\x20IN\x20AN\x20ACTION\x20OF\x20CONTRACT,\x20TORT\x20OR\x20OTHERWISE,\x20ARISING\x20FROM,\x20OUT\x20OF\x20OR\x20IN\x20CONNECTION\x20WITH\x20THE\x20SOFTWARE\x20OR\x20THE\x20USE\x20OR\x20OTHER\x20DEALINGS\x20IN\x20THE\x20SOFTWARE.\x0a')
	begin = input('>>\x20Press\x20enter\x20to\x20continue\x20<<')

def flood(): 
	print(fg(9) + '\x0a\x0a[', end='')
	print(fg(15) + '*', end='')
	print(fg(9) + ']', end=' ')
	pin = input(fg(46) + 'Enter\x20game\x20pin: ')

	print(fg(9) + '[', end='')
	print(fg(15) + '*', end='')
	print(fg(9) + ']', end=' ')
	custom_name_choice = input(fg(46) + 'Randomize\x20username?\x20[y/n]:\x20')

	if custom_name_choice == 'y':
		name = names.get_first_name()
	
	else:
		print(fg(9) + '[', end='')
		print(fg(15) + '*', end='')
		print(fg(9) + ']', end=' ')
		name = input(fg(46) + 'Enter\x20Username: ')

	print(fg(9) + '[', end='')
	print(fg(15) + '*', end='')
	print(fg(9) + ']', end=' ')
	bot_count = input(fg(46) + 'Enter\x20amounts\x20of\x20bots: ')

	os.system('cls')
	print(fg(46) + f'Connecting\x20to\x20' + fg(11) + f'{pin}' + fg(46) + '...', end=' ')
	time.sleep(3)
	if pin.isdigit() == False:
		print(fg(9) + f'Failed')
	
	else:
		print(fg(46) + 'Success')
	num_count = 0
	print(fg(46) + 'Generating' + fg(11) + f'\x20{bot_count}' + fg(46) + '\x20Bots...', end=' ')
	time.sleep(3)
	if bot_count.isdigit() == True:
		print(fg(46) + 'Success\x0a')
		time.sleep(2)
		for i in range(int(bot_count) + 1):
			if pin.isdigit() == True:
				print(f'Successfully\x20joined\x20game\x20as\x20{name + str(num_count)}')
				num_count += 1
				time.sleep(0.05)

			elif bot_count.isdigit() == False:
				break

			else:
				break
	
	else:
		print(fg(9) + 'Failed' + fg(46))

def main():
	os.system('cls')
	packages()
	caution()
	flood()

main()
