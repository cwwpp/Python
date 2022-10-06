import pyautogui
import random

count = 0

keyboard = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
keyboard_list = list(keyboard)

password = pyautogui.password('Enter Password: ')
guess_password = ''

while (guess_password != password):
    count += 1
    guess_password = random.choices(keyboard_list, k = len(password))
    print(str(guess_password))

    if (guess_password == list(password)):
        print('Your password is: ' + "".join(guess_password))
        print('Took ' + str(count) + ' Tries To Find.')
        break
