# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:19:44 2019

@author: Charles
"""

import time, subprocess

filepath = [r" "]

timeLeft = 60 
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['start', filepath], shell=True)

