import pyautogui, time

text = input('Enter Text: ')

class spam():
	def spamLoop(self, x):
		time.sleep(5)
		while True:
			pyautogui.typewrite(x)
			pyautogui.press('enter')
startSpam = spam()
startSpam.spamLoop(text)
