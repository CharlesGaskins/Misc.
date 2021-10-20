# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:18:47 2019

@author: Charles
"""

import pyautogui
import pyperclip

#print(pyautogui.size())

width, height = pyautogui.size()

#for i in range(10):
#    pyautogui.moveRel(100, 0, duration = .25)
#    pyautogui.moveRel(0, 100, duration = .25)
#    pyautogui.moveRel(-100, 0, duration = .25)
#    pyautogui.moveRel(0, -100, duration = .25)
#    

#pyautogui.click(1023, 225, button='left')

numbers = ''
for i in range(200):
    numbers = numbers + str(i) + '\n'
    
pyperclip.copy(numbers)
print(numbers)

