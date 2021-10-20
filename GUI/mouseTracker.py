# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:21:05 2019

@author: Charles
"""

#displays the current position of the mouse

#import pyautogui
#
#print('Press Crtl-C to quit')
#try:
#    while True:
#        x, y = pyautogui.position()
#        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#        print(positionStr, end='')
#        print('\b' * len(positionStr), end='', flush=True)
#except KeyboardInterrupt:
#    print('\nDone.')


import pyautogui
print('Press Ctrl-C to quit.')
try:
    while True:
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='\r', flush=True)
except KeyboardInterrupt:
    print('\nDone.')
    
#    try:
#    while True:
#        x, y = pyautogui.position()
#        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#        print(positionStr, end='\r', flush=True)
#except KeyboardInterrupt:
#    print('\nDone.')