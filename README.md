Christopher Anderson <br>
00218730<br>
CIS – 153 01A<br>
<br>
Description:<br>
This program is used to scrape StockX for Last Sale, Highest Bid and Lowest Ask on specific colorway and size of shoe. It scans an excel file for a unique identifier known as a “Ticker Symbol” and scans the “Size” then uses Selenium to navigate and extract pricing data. <br>
<br>
This program contains at least one of each of the following concepts: Conditional Execution, Functions, Loops, Strings & String Methods, Accessing Files, List Creation, Tuples, Web Services and Networked Programs. - Selenium uses both Web Services, and Networked programs as part of its architecture to browse and scrape websites.  <br>
<br>


Program Operation: <br>
	To use the program, you will need to have the following modules installed for Python: 
1.	pandas
2.	time
3.	openpyxl
4.	selenium webdriver
5.	pathlib<br>
<br>
Additionally, you will need an excel file with a sheet name “Website Inventory” and a column of ticker symbols and column of sizes. These columns should have the headers “Ticker” and “Size” (case sensitive)<br>
When using your own excel file you will need to modify the program under the last block of code. Include the directory path for YOUR .xlsx file. You can also modify the default cells where the data is written in this excel file. <br>
Lastly, you must install chromedriver and I recommend putting it in the same directory as python, otherwise you will need to edit the path in the python file. Browser = webdriver.Chrome(‘YOUR PATH HERE’) <br>
<br>
Depending on the speed of your internet and performance of your computer, you can tweak the sleep time for each task if your pages load slowly. By modifying 1 or all of the time.sleep() functions with the value that suits your internet speed/computer performance. <br>
<br>
Future Work: 
It is my goal to continue this project so that it can loop through an entire columns of Ticker Symbol/Size combinations and extract and write the price data for each symbol/size combination and write them in the adjacent cells to the set of given data.  
