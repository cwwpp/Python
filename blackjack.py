import random
import os

cards = [1, 2, 3, 4, 5, 6,7, 8, 9, 10, "J", "Q", "K", "A"]
ace = [1, 10, 11]



def game():
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
                elif DealerCards == "A":
                    DealerTotal += random.choice(ace)
                else:
                    DealerTotal += int(DealerCards[i])

            while DealerTotal < 16:
                DealerCards.append(random.choice(cards))
                if DealerCards[-1] == 'J' or DealerCards[-1] == 'Q' or DealerCards[-1] == 'K':
                    DealerTotal += 10
                elif DealerCards[-1] == "A":
                    DealerTotal += random.choice(ace)
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
    else:
        if PlayerTotal > DealerTotal:
            print("\nDealer: You won\n")
        elif PlayerTotal < DealerTotal and DealerTotal <= 21:
            print("\nDealer: You lost.\n")
        elif PlayerTotal >= 16 and PlayerTotal <= 21 and DealerTotal > 21:
            print("\nDealer: You won\n")
        elif PlayerTotal >= 21 and DealerTotal >= 21 and PlayerTotal != DealerTotal:
            print("\nDealer: No winners this round.\n")
        else:
            print("\nDealer: No winners this round.\n")



def main():
    try:
        os.system('cls')
    except:
        os.system("clear")
    game()


main()
