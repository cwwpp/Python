import random
import time
import os
import maskpass

# 18/08/2024


# Initialize variables

cards = [1, 2, 3, 4, 5, 6,7, 8, 9, 10, "J", "Q", "K", "A"]
ace = [1, 10, 11]


experience = ''

balance = 100000


random_color = ['black', 'red']

work_salary = []

roulette_number = []

rob = []

jobs = ['Mechanic', 'Engineer', 'Teacher', 'Scientist']

rob_luck = ['succesfully', 'succesfully', 'failed', 'failed']



# Create a set of random values for the mini games.

for i in range(1, 31):
	roulette_number.append(i)

for i in range(1, 201):
	work_salary.append(i)


for i in range(1, 101):
	rob.append(i)


total_matches = 0
wins = 0
loss = 0
tie = 0
bank = 0
win_rate = 0


# Change cmd color

def colorWhite():
	try:
		os.system('color 7')
	except:
		pass

def colorGreen():
	try:
		os.system('color a')
	except:
		pass
	


# Clear cli screen

def clearScreen():
	try:
		os.system('cls')
	except:
		os.system('clear')

clearScreen()


username = (input("\nName: ")).replace(" ", "")

if username == 'DEV':
	password = maskpass.askpass(mask="*")

	if password != '2024DEV':
		input("\nIncorrect password.")
		clearScreen()
		exit()
	
	else:
		clearScreen()
		input("\nWelcome developer!")


# Set wins command for dev

def setWin():
	if username == 'DEV':
		wins = input('\nHow many wins do you want to set to? ')
		while wins.isdigit() == False:
			wins = input("\nValue entered is not a digit, please enter a different value: ")

		wins = int(wins)
	
	else:
		print("\nYou do not have permission to run this command.")


# Set loss command for dev

def setLoss():
	if username == 'DEV':
		loss = input("\nHow many loses do you want to set to? ")
		while loss.isdigit() == False:
			loss = input("\nValue entered is not a number, please enter a different value: ")
		
		loss = int(loss)

	
	


# Dev help menu

def devHelp():
	print("""
DEV MENU

setwin	    - Set a specific amount of wins
setlose	    - Set a specific amount of loses
settie	    - Set a specific amount of ties
setbal	    - Set a specific amount of cash
setbank	    - Set a specific amount of money in the bank
db          - Double the money you currently have""")


# Player help menu
	
def menu():
	print("""
HELP MENU

roulette	- Play roulette
blackjack	- Play blackjack
baccarat	- Play baccarat
bal     	- Check balance
work		- Work to get money
rob	        - Rob a user
wit	        - Withdraw money from the bank
dep	        - Deposit money to the bank
cls	        - Clear screen
exit		- Exit
help		- Help""")
	


	


# Main func



clearScreen()
colorGreen()
menu()


	
while True:
		
	uInput = (input(f"\n~/Hayden-Casino$ ")).strip()

	# Experience update.

	total_matches = wins + loss + tie

	if (total_matches - tie) == 0:
		win_rate = 0

	else:
		win_rate = wins / total_matches * 100

	if wins >=0:
		experience = 'Newbie'
		
	if wins >= 10:
		experience = 'Veteran'
	
	if wins >= 20:
		experience = 'Professional'



	# Roulette

	if uInput == "roulette":

		try:
			random_color_pick = random.choice(random_color)
			random_number_pick = random.choice(roulette_number)


			bet, betChoice = (input("\nCroupier: Enter your bet (amnt, bet) $")).split(" ")

			if balance < 100:
				print(f"\nCroupier: Insufficient balance to play, you need at least $100.")
			
			else:

				if bet == 'all':
					bet = balance

				else:

					while bet.isdigit() == False:
						bet, betChoice = (input("\nCroupier: Enter your bet (amnt, bet) $")).split(" ")

					bet = int(bet)

					while bet < 100:
						print("\nCroupier: You need at least $100 to bet.")
						bet = input("\nCroupier: Re-enter your bet amount $")

						while bet.isdigit() == False:
							bet, betChoice = (input("\nCroupier: Enter your bet (amnt, bet) $")).split(" ")
						
						bet = int(bet)

					if bet > balance:
						print("\nCroupier: Insufficient balance.")

				betChoice = betChoice.lower()

				while betChoice != 'black' and betChoice != 'odd' and betChoice != 'red' and betChoice != 'even':
					betChoice = input("\nCroupier: Invalid bet, please re-enter your bet (odd, even, black, red) ")

				clearScreen()
					
				print(f"\nCroupier: You've placed a bet on {betChoice} for ${bet}.")

				time.sleep(3)

				if betChoice == 'black' or 'red':

					if random_color_pick == betChoice:
						print(f'\nCroupier: The ball landed on {random_number_pick} {random_color_pick}, you won.')
						
						print(f"\n+ ${bet}")

						balance += bet

						wins += 1

					else:
						print(f'\nCroupier: The ball landed on {random_number_pick} {random_color_pick}, you lost.')

						print(f"\n- ${bet}")

						balance -= bet

						loss += 1

				else:
						
					if betChoice == 'even':
						if random_number_pick % 2 == 0:
							print(f'\nCroupier: The ball landed on {random_number_pick} {random_color_pick}, you won.')
							
							print(f"\n+ ${bet}")

							balance += bet

							wins += 1

						else:
							print(f'\nCroupier: The ball landed on {random_number_pick} {random_color_pick}, you lost.')
							
							print(f"\n- ${bet}")

							balance -= bet

							loss += 1
						
					elif betChoice == 'odd':
						if random_number_pick % 2 == 0:
							print(f'\nThe ball landed on {random_number_pick} {random_color_pick}, you lost.')

							print(f"\n- ${bet}")

							balance -= bet

							loss += 1

						else:
							print(f'\nThe ball landed on {random_number_pick} {random_color_pick}, you won.')

							print(f"\n+ ${bet}")

							balance += bet

							wins += 1

		except:
			print('\nAn error occurred.')


	# Baccarat

	elif uInput == 'baccarat':

		bet=input("\nDealer: How much do you want to bet? (MIN: $100) $")

		user_total = 0
		dealer_total = 0

		if bet.isdigit():
			if int(bet) >= 100:
				bet=int(bet)
				cards_in_hand=[]

				for i in range(3):
					random_card_pick=random.choice(cards)
					cards_in_hand.append(random_card_pick)

				if 'A' in cards_in_hand:
					print(f"\nYou: {cards_in_hand[0]}, {cards_in_hand[1]}, {cards_in_hand[2]}")
				
				for x in range(3):
					if "J" in cards_in_hand:
						cardJPos=cards_in_hand.index("J")
						cards_in_hand[cardJPos]=10
					elif "Q" in cards_in_hand:
						cardQPos=cards_in_hand.index("Q")
						cards_in_hand[cardQPos]=10
					elif "K" in cards_in_hand:
						cardKPos=cards_in_hand.index("K")
						cards_in_hand[cardKPos]=10
					elif "A" in cards_in_hand:
						cardAPos=cards_in_hand.index("A")
						while 1>0:
							ace = input("\nDealer: You got an ace, choose 1, 10 or 11: ")
							
							while ace.isdigit() == False:
								ace = input("\nDealer: Invalid value, please enter again: ")

							if int(ace) == 1 or int(ace) == 10 or int(ace) == 11:
								cards_in_hand[cardAPos] = int(ace)
								break

				clearScreen()


						
				for i in range(3):
					user_total =user_total +int(cards_in_hand[i])
				player_score = str(user_total)[-1]

				print(f"\nYou: {cards_in_hand[0]}, {cards_in_hand[1]}, {cards_in_hand[2]} ({player_score})")


				# Dealer

				cards_in_dealer_hand=[]
				for i in range(3):
					random_card_pick=random.choice(cards)
					cards_in_dealer_hand.append(random_card_pick)
				
				time.sleep(2)


				for x in range(3):

					if "J" in cards_in_dealer_hand:
						cardJPosBot=cards_in_dealer_hand.index("J")
						cards_in_dealer_hand[cardJPosBot]=10

					elif "Q" in cards_in_dealer_hand:
						cardQPosBot=cards_in_dealer_hand.index("Q")
						cards_in_dealer_hand[cardQPosBot]=10

					elif "K" in cards_in_dealer_hand:
						cardKPosBot=cards_in_dealer_hand.index("K")
						cards_in_dealer_hand[cardKPosBot]=10

					elif "A" in cards_in_dealer_hand:
						cardAPosBot=cards_in_dealer_hand.index("A")
						rVal=[1,10,11]
						randomAVal=random.choice(rVal)
						cards_in_dealer_hand[cardAPosBot]=randomAVal

				for x in range(3):
					dealer_total += int(cards_in_dealer_hand[x])
				dealer_score=str(dealer_total)[-1]
				
				print(f"\nDealer: {cards_in_dealer_hand[0]}, {cards_in_dealer_hand[1]}, {cards_in_dealer_hand[2]} ({dealer_score})\n")

				# Score check

				if dealer_score != player_score:
					if dealer_score > player_score:
						print(f"You've lost ${bet}.")
						loss+=1
						balance -= bet
					else:
						print(f"You've won ${bet}!")
						wins+=1
						balance += bet

					
			else:
				print("You need to bet at least $100 to play.")
		else:
			print("Invalid value")



	# Blackjack

	elif uInput == 'blackjack':

		bet = input("\nHow much do you want to bet? $")

		if balance < 100:
			print(f"\nInsufficient balance, you need at least $100 to play.")

		else:

			if bet == 'all':
				bet = balance

			else:

				while bet.isdigit() == False:
					bet = input("\nInvalid bet, please enter a different amount: $")
				
				bet = int(bet)

				while bet > balance:
					bet = input("\nInsufficient balance, please enter a different amount: ")

				bet = int(bet)

				while bet < 100:
					bet = input("\nYou have to bet at least $100, re-enter your bet amount: $")

			DealerCards = []
			PlayerCards = []

			for i in range(2):    
				PlayerCards.append(random.choice(cards))

			count = 0

			while True:
				if len(PlayerCards) == 2:
					print(f"\nYou: {PlayerCards[0]}, {PlayerCards[1]}")
				else:
					print('You: ', end="")
					for i in range(len(PlayerCards)-1):
						print(f"{PlayerCards[i]}", end=", ")
					print(PlayerCards[len(PlayerCards)-1])

				choice = input("\nDealer: Do you want to take another card? (y/n): ")


				if choice == "y":
					if count < 3:
						count += 1
						PlayerCards.append(random.choice(cards))
						
					else:
						print("\nDealer: You cannot take anymore cards.\n")

				elif choice == "n":
					for i in range(2):
						DealerCards.append(random.choice(cards))

					PlayerTotal = 0
					DealerTotal = 0

					for i in range(len(DealerCards)):
						if DealerCards[i] == 'J' or DealerCards[i] == 'Q' or DealerCards[i] == 'K':
							DealerTotal += 10
						elif DealerCards[i] == 'A':
							DealerTotal += random.choice(ace)
						else:
							DealerTotal += int(DealerCards[i])

					while DealerTotal < 16:
						DealerCards.append(random.choice(cards))
						if DealerCards[-1] == 'J' or DealerCards[-1] == 'Q' or DealerCards[-1] == 'K':
							DealerTotal += 10
						elif DealerCards[-1] == "A":
							DealerTotal += int(random.choice(ace))
						else:
							DealerTotal += int(DealerCards[-1])

					CardCount = 0

					while CardCount < len(PlayerCards):
						if PlayerCards[CardCount] == 'J' or PlayerCards[CardCount] == 'Q' or PlayerCards[CardCount] == 'K':
							PlayerTotal += 10
							CardCount += 1

						elif PlayerCards[CardCount] == 'A':
							AceChoice = input("\nYou: You got an Ace, pick 1, 10, 11: ")
							if AceChoice == '1':
								PlayerTotal += 1
							elif AceChoice == "10":
								PlayerTotal += 10
							elif AceChoice == "11":
								PlayerTotal += 11
							else:
								print("\nYou: Invalid choice.\n")
								while True:
									AceChoice = input("You: You got an Ace, pick 1, 10, 11: ")
									if AceChoice == '1':
										PlayerTotal += 1
										break
									elif AceChoice == "10":
										PlayerTotal += 10
										break
									elif AceChoice == "11":
										PlayerTotal += 11
										break
									else:
										print("\nYou: Invalid choice.\n")
							CardCount += 1

						else:
							PlayerTotal += PlayerCards[CardCount]
							CardCount += 1
					break

			time.sleep(3)

			print("\nDealer: ", end="")

			for i in range(len(DealerCards)-1):      
				print(f"{DealerCards[i]}", end=", ")
			print(f"{DealerCards[len(DealerCards)-1]}", end = f" ({DealerTotal})\n")

			print("\nYou: ", end = "")

			for i in range(len(PlayerCards)-1):
				print(f"{PlayerCards[i]}", end=", ")
			print(f"{PlayerCards[len(PlayerCards)-1]}", end = f" ({PlayerTotal})\n")

			if PlayerTotal > 21:
				print("\nDealer: You lost.\n")
				balance -= bet
				print(f"- ${bet}")
				loss += 1

			else:
				if PlayerTotal > DealerTotal:
					print("\nDealer: You won\n")
					balance += bet
					print(f"+ ${bet}")
					wins += 1

				elif PlayerTotal < DealerTotal and DealerTotal <= 21:
					print("\nDealer: You lost.\n")
					balance -= bet
					print(f"- ${bet}")
					loss += 1

				elif PlayerTotal >= 16 and PlayerTotal <= 21 and DealerTotal > 21:
					print("\nDealer: You won\n")
					balance += bet
					print(f"+ ${bet}")
					wins += 1

				elif PlayerTotal >= 21 and DealerTotal >= 21 and PlayerTotal != DealerTotal:
					print("\nDealer: No winners this round.\n")
					tie += 1

				else:
					print("\nDealer: No winners this round.\n")
					tie += 1


				
	elif uInput == "bal":
		print(f"{username}'s Economy")
		print(f"\nCash: ${balance}")
		print(f"Bank: ${bank}")
		print(f"Experience: {experience}")
		print(f"Wins: {wins}")
		print(f"Loss: {loss}")
		print(f"Ties: {tie}")
		print(f"Total Matches: {total_matches}")
		print(f"Win Rate: {round(win_rate, 2)}%")


	# Work

	elif uInput == "work":
		clearScreen()
		for i in range(30):
			print(f"Press Enter 30 times ({i}/30)")
			input("")
			clearScreen()
		time.sleep(2)

		salary = random.choice(work_salary)

		balance += salary

		print(f"You work as a {random.choice(jobs)} and got ${salary}.")

	
	# Criminal code block

	elif uInput == 'rob':
		random_rob_luck = random.choice(rob_luck)

		rob_money = random.choice(rob)

		clearScreen()

		time.sleep(2)

		if random_rob_luck == 'succesfully':
			print(f"You've {random_rob_luck} rob a person and got ${rob_money}.")
			balance += rob_money
		
		else:
			print(f"You've failed to rob a person and got arrested. You lost ${rob_money}.")
			balance -= rob_money




	# DEV UTILITIES

	elif uInput == 'devhelp':
		if username == 'DEV':
			devHelp()
		
		else:
			print('\nYou do not have permission to run this command.')


	elif uInput == 'setbal':
		if username == 'DEV':
			set_bal = input("\nEnter amount of money in balance: $")

			while set_bal.isdigit() == False:
				set_bal = input("\nInvalid input, please enter a new amount: $")

			set_bal = int(set_bal)

			balance = set_bal
		
		else:
			print("\nYou do not have permission to run this command.")

	
	elif uInput == 'setbank':
		if username == 'DEV':
			set_bank = input("\nEnter amount of money in the bank: $")

			while set_bank.isdigit() == False:
				set_bank = input("\nInvalid input, please enter a new amount: $")

			set_bank = int(set_bank)

			bank = set_bank
		
		else:
			print("\nYou do not have permission to run this command.")


	elif uInput == 'setwin':
		if username == 'DEV':
			set_win = input("\nEnter number of wins: ")

			while set_win.isdigit() == False:
				set_win = input("\nInvalid input, please enter a number: ")

			set_win = int(set_win)

			wins = set_win
		
		else:
			print("\nYou do not have permission to run this command.")

	
	elif uInput == 'setloss':
		if username == 'DEV':
			set_loss = input("\nEnter number of loss: ")

			while set_loss.isdigit() == False:
				set_loss = input("\nInvalid input, please enter a number: ")

			set_loss = int(set_loss)

			loss = set_loss
		
		else:
			print("\nYou do not have permission to run this command.")

	elif uInput == 'settie':
		if username == 'DEV':
			set_tie = input("\nEnter number of ties: ")

			while set_tie.isdigit() == False:
				set_tie = input("\nInvalid input, please enter a number: ")
			
			set_tie = int(set_tie)

			tie = set_tie


	elif uInput == 'db':
		if username == "DEV":
			balance *= 2
		
		else:
			print("\nYou do not have permission to run this command.")






	# Deposit money to bank account

	elif uInput == 'dep':
		deposit_amount = input("\nHow much do you want to deposit? $")

		if deposit_amount == 'all':
			deposit_amount = balance
			balance = 0
			bank += deposit_amount

		else:

			while deposit_amount.isdigit() == 'False':
				deposit_amount = input("\nValue entered is not a number, please enter a different value: $")

			deposit_amount = int(deposit_amount)

			while deposit_amount < 0:
				deposit_amount = input("\nYou can not deposit a negative amount of money. Please enter a different amount: $")
			
			deposit_amount = int(deposit_amount)

			while deposit_amount > balance:
				deposit_amount = input("\nInsufficient money to deposit to the bank. Please enter a different amount: $")

			deposit_amount = int(deposit_amount)

			balance -= deposit_amount
			bank += deposit_amount

		print(f"\nYou've succesfully deposit ${deposit_amount} to your bank account.")


	# Withdraw money from bank account

	elif uInput == "wit":
		withdraw_amount = input('\nHow much do you want to withdraw? $')

		if withdraw_amount == 'all':
			withdraw_amount = bank
			bank = 0
			balance += withdraw_amount

		else:
		
			while withdraw_amount.isdigit() == False:
				withdraw_amount = input("\nValue entered is not a number, please enter a different value: $")

			withdraw_amount = int(withdraw_amount)

			while withdraw_amount < 0:
				withdraw_amount = input("\nYou can not withdraw a negative amount of money from the bank. Please enter a different amount: $")

			withdraw_amount = int(withdraw_amount)

			while withdraw_amount > bank:
				withdraw_amount = input("\nInsufficient money to withdraw from the bank. Please enter a different amount: $")

			withdraw_amount = int(withdraw_amount)

			balance += withdraw_amount
			bank -= withdraw_amount

		print(f"\nYou've succesfully withdrawed ${withdraw_amount} from your bank account.")


	# Commands

	elif uInput.strip() == '':
		pass
			
	elif uInput == "clear" or uInput == "cls":
		clearScreen()
			
	elif uInput == "exit":
		colorWhite()
		exit()
		
	elif uInput == "help" or uInput == "h":
		menu()
		
	else:
		print("\nInvalid command.")
