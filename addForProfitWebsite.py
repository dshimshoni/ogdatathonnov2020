# import requests
# from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_excel('AmericanCompanies.xlsx')

websites = []

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 


for i in range(len(df)):
    query_row = df.iloc[i]
    org_name = query_row[0]
    for j in search(org_name, tld="co.in", num=1, stop=1, pause=2): 
        websites.append(j)
        print(org_name)
        
df['website'] = websites

df.to_excel('american_companies_with_website.xlsx')