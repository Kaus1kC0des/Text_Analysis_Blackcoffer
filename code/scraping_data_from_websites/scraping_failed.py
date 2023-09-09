"""
In this file we try to scrape the links which we were unable to scrape with the parsing_websites.py
Here we change the selector for each file by inspecting the website and then selecting the selector corresponding to the content
in the website.
"""

# Performing imports
import pandas as pd
from bs4 import BeautifulSoup
import requests

# the dataframe reads the excel file and then helps us traverse its contents for the URL_ID and URL
data = pd.read_excel('input.xlsx')
x = 92
# curl = "https://insights.blackcoffer.com/rising-it-cities-and-its-impact-on-the-economy-environment-infrastructure-and-city-life-by-the-year-2040-2/"

contents = requests.get(data.loc[x,'URL']).content
# contents = requests.get(curl).content

soup = BeautifulSoup(contents,'html.parser')

filename = f"file_{str(int(data.loc[x,'URL_ID']))}"

try:
    with open(f"contents/{filename}",'a') as file:
        file.write(soup.select_one("#tdi_117 > div > div.vc_column.tdi_120.wpb_column.vc_column_container.tdc-column.td-pb-span8 > div > div.td_block_wrap.tdb_single_content.tdi_130.td-pb-border-top.td_block_template_1.td-post-content.tagdiv-type > div").text)
except AttributeError:
    print("Locator not found")
    print(data.loc[x,'URL'])
else:
    print(f"File written successfully")
