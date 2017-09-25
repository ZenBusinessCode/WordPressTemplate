import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
 
res = requests.get("https://finance.yahoo.com/quote/TSLA?p=TSLA")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[1] 
df = pd.read_html(str(table))
print( tabulate(df[0], headers='keys', tablefmt='psql') )
