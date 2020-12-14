#Christopher Anderson
#I.D. 00218730
#12/13/2020
#Programming for I.T.
#Final Project - Stockx Web Scraper - Searches Stockx using Ticker Symbol, extracts price data and writes to excel.

import pandas as pd
import urllib
import time

from selenium import webdriver
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#open excel sheet 1
df = pd.read_excel("final.xlsx", sheet_name=0)
#
dfticker = df.dropna(subset=['Ticker'])
dfsize = df.dropna(subset=['Size'])
ticker = list(dfticker['Ticker'])
size = list(dfsize['Size'])
tuplist = zip(ticker, size)

#test to see tuple list values
for i in tuplist:
    print(i)


#combine ticker symbol with stockx search prefix URL

stockx = 'https://stockx.com/search/sneakers?s='
url_list = list()
for i in ticker:
    x = stockx + i
    url_list.append(x)

#test values print URL list
for i in url_list:
    print(i)

#concatenate search url with ticker symbol to create a search url for specific colorway
stockx = 'https://stockx.com/search/sneakers?s=AJ1MS-WBRSGS'
url = stockx

#selenium navigate to link and open shoe info page
browser = webdriver.Chrome()
browser.get(stockx)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/a/div[1]/div/div').click()
time.sleep(3)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/span/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div/div/button').click()


#save for later
#print(url_list[0])

input('Press Enter to Exit')
