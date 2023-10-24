import pyautogui
import time
import os

def openChrome():
    time.sleep(2)
    os.system('start "" /b chrome --incognito --kiosk')
    pyautogui.click(x=1042, y=699)
    pyautogui.click()

def votar():
    pyautogui.click(x=367, y=54)
    pyautogui.write('https://evc.camara.leg.br/votacao-pjb-paraiba-pb/')
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.hotkey('pagedown')
    pyautogui.moveTo(x=985, y=850)
    pyautogui.click()
    pyautogui.scroll(-300)
    pyautogui.click(x=632, y=831)
    pyautogui.click()
    pyautogui.click(x=636, y=891)
    pyautogui.click()

x=1
while(x>0):
    openChrome()
    time.sleep(2)
    votar()
    time.sleep(3)
    pyautogui.hotkey('alt','f4')
    x-=1



