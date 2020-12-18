#Christopher Anderson
#I.D. 00218730
#12/13/2020
#Programming for I.T.
#Final Project - Stockx Web Scraper - Searches Stockx using Ticker Symbol, extracts price data and writes to excel.

#modules/dependencies
import pandas as pd
import time
import openpyxl
from selenium import webdriver
from pathlib import Path


#functions
#checks file path and name are valid/correct
def filechkr():
    global df
    fl = input('Please enter file path and name, include extension: ')
    gfile = Path(fl)
    if gfile.is_file():
        df = pd.read_excel(fl, sheet_name=0)
    else:
        print('File does not exist, check file path and name then re-open program.')
        quit()

#checks column names are valid/exist then creates lists
def columnchkr():
    global tickerclmn
    global sizeclmn
    global tuplist
    global ticker
    global size
    tickerclmn = input('Please enter column header for ticker symbols(Case Sensitive): ')
    sizeclmn = input('Please enter column header for shoe sizes (Case Sensitive): ' )
    if tickerclmn and sizeclmn  in df:
        dfticker = df.dropna(subset=[tickerclmn])
        ticker = list(dfticker[tickerclmn])
        dfsize = df.dropna(subset=[sizeclmn])
        size = list(dfsize[sizeclmn])
        tuplist = zip(ticker, size)
    else:
        print('One or more columns do not exist, please verify column names and try again.')
        quit()

#combine ticker symbol with stockx search prefix URL
def urlmaker ():
    global url_list
    stockx = 'https://stockx.com/search/sneakers?s='
    url_list = list()
    for i in ticker:
        x = stockx + i
        url_list.append(x)
#-------------------------------------------------------------------------------------------
#main
try:
    filechkr()
    columnchkr()
    urlmaker()
except:
    print('Column names are case sensitive please verify input and try again.')
    quit()

#inventory ticker symbol and size list
print('Inventory of Ticker Symbols and Corresponding Sizes')
for i in tuplist:
    print(i)
print()

#inventory URL list
print("List of shoe inventory stockx URL's")
for i in url_list:
    print(i)

#first search URL assigned to variable
stockx = url_list[0]
print('Pulling price data for shoe', ticker[0], 'size', size[0])

#selenium navigate to link and open shoe info page
browser = webdriver.Chrome('chromedriver')
browser.get(stockx)
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/a/div[1]/div/div').click()
time.sleep(5)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/span/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div/div/button').click()
time.sleep(4)
resultSet = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/span/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div/div/div/div/div/div[2]/ul')
options = resultSet.find_elements_by_tag_name("li")

#selects size 10 in standard sizing menu and pulls pricing data last sale, highest bid, lowest ask from webpage
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/span/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div/div/div/div/div/div[2]/ul/li[8]').click()
lastsale = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/span/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[1]').text
lowestask = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/span/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/a/div[1]/div').text
highestbid = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/span/div[2]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/a/div[1]/div').text

#prints values in console that will be inserted in excel
print("Last Sale:", lastsale)
print("Lowest Ask:", lowestask)
print("Highest Bid:", highestbid)

#replace $ with nothing and convert to int before entering in excel
lastsale = lastsale.replace('$','')
lowestask = lowestask.replace('$','')
highestbid = highestbid.replace('$','')
lastsaleint = int(lastsale)
lowestaskint = int(lowestask)
highestbidint = int(highestbid)

#write extracted price data into updated spreadsheet in assigned cells
wb = openpyxl.load_workbook('finalmodified.xlsx')
sheet = wb["Website Inventory"]
sheet['M2'] = lastsaleint
sheet['N2'] = lowestaskint
sheet['O2'] = highestbidint
wb.save('finalmodified.xlsx')

#prevents windows python console from closing before data can be viewed by user
input('Press Enter to Exit')
