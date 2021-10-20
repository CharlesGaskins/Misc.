# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:11:33 2019

@author: Charles
"""
#this program will draw using the pain app on your machine
import pyautogui, time

#sleep gives the user time to move from running your program over to the paint
#app
time.sleep(5)

#using these particular coordinated the program will draw a spiraling square
#relative to the starting point of where the cursor is on the screen
pyautogui.click()
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration = .2)
    distance = distance -5
    pyautogui.dragRel(0, distance, duration = .2)
    pyautogui.dragRel(-distance, 0, duration = .2)
    distance = distance -5
    pyautogui.dragRel(0,-distance, duration = .2)
    0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.6+++++++++++++++++++++++++++++++++++++++++++++++++++++