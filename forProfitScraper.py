#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:22:50 2020

@author: danielrichardson
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
import time
import pandas as pd

df = pd.read_excel('american_companies_with_website.xlsx')
websites = df['Website']
tickers = df['Ticker Symbol']
descriptions = []

# print(tickers)


driver = webdriver.Chrome("/Users/danielrichardson/Downloads/chromedriver")

for ticker in tickers:
    URL = 'https://www.bloomberg.com/profile/company/' + ticker +':US'
    driver.get(URL)
    
    description = driver.find_element_by_class_name("description__ce057c5c")
    print(description.text)
    descriptions.append(description.text)

df['descriptions'] = descriptions

df.to_excel('american_companies_with_descriptions.xlsx')
