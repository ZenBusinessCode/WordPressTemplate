#Define the first table 

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
 
#grab stock data from yahoo finance website and not the API 
res = requests.get("https://finance.yahoo.com/quote/TSLA?p=TSLA")
soup = BeautifulSoup(res.content,'lxml')

#change the table from 0 - infinity based upon how many tables are present 
table = soup.find_all('table')[0] 
df = pd.read_html(str(table))

#change the table format from psql, csv, json or other format 
print( tabulate(df[0], headers='keys', tablefmt='psql') )

------------------------------------------------------------------------------------
#Define the second table 

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
 
res = requests.get("https://finance.yahoo.com/quote/TSLA?p=TSLA")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[1] 
df = pd.read_html(str(table))
print( tabulate(df[0], headers='keys', tablefmt='psql') )
------------------------------------------------------------------------------------
#Define the third table 

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
 
res = requests.get("https://finance.yahoo.com/quote/TSLA?p=TSLA")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[2] 
df = pd.read_html(str(table))
print( tabulate(df[0], headers='keys', tablefmt='psql') )
------------------------------------------------------------------------------------

#Definet master parse file 
import pandas as pd

print(1)
import TeslaYahooFinance1 as df1
print(2)
import TeslaYahooFinance2 as df2 
print(3)
import TeslaYahooFinance3 as df3

