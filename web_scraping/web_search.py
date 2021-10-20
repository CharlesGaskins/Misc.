 # -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:15:43 2019

@author: Charles
"""

# from selenium import webdriver
from pprint import pprint
import requests


# def webFunction(search_str):
#     print('Googling...')
url = 'http://www.eslcafe.com/jobs/china/'
page = requests.get(url)
#     print(f'url: {url}')
#     browser = webdriver.Chrome()
#     browser.get(url)
#     links = []
#     linkElems = browser.find_elements_by_class_name('ellip')
#     for i in linkElems:
#         link = i.get_attribute('href')
# #        print(link)
#         links.append(link)
#     pprint(links[5:])
        
    


        
    #open a browser tab for each result
#    linkElem = browser.find_element_by_class_name('ellip')
#    numOpen = (5, len(linkElem))
#    for i in range(numOpen):
#        linkElem.click()
#    print(linkElem)
# 
    
# def test_it(args):
#     print(args)
#     webFunction(args)
   
# if __name__ == '__main__':
#     client = input("What do you want to search?: ")
#     test_it(client)  
    
    

 
