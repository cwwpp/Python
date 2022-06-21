import time, pyautogui

numCLick = input('ENTER THE NUMBER OF CLICKS: ')

class autoclicker():
    def autoclick(self, x):
        time.sleep(5)
        for i in range(int(x)):
            pyautogui.leftClick()
auto = autoclicker()
auto.autoclick(numCLick)
