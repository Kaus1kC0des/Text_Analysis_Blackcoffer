"""
This application scrapes data from the given website.
The content in the website have the same locator to locate the content from the website.
Hence we use pandas to iterate through the columns of the given input file, then we parse them with the
help of BeautifulSoup and requests.
"""

# Performing the imports
import requests
from bs4 import BeautifulSoup
import pandas as pd

data = pd.read_excel('input.xlsx')
errors = []

for i in range(len(data.index)):
    current_filename = f"file_{str(int(data.loc[i, 'URL_ID']))}.txt"
    url = data.loc[i, 'URL']

    try:
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        target = soup.select_one("div.td-container > div > div.td-pb-span8.td-main-content")

        if target:
            with open(f"contents/{current_filename}", 'w') as file:
                file.write(target.get_text())
            print(f"Content of {data.loc[i, 'URL_ID']} written into {current_filename}")
        else:
            with open("failures.txt",'a') as fail:
                fail.write(f"{data[i]['URL_ID']}\n")
            errors.append(data[i]['URL_ID'])
            print(f"Unable to parse the content of URL_ID: {data.loc[i, 'URL_ID']}")

    except requests.RequestException as e:
        print(f"Error accessing URL_ID: {data.loc[i, 'URL_ID']}, Error: {e}")
    except Exception as e:
        print(f"An error occurred for URL_ID: {data.loc[i, 'URL_ID']}, Error: {e}")


print(errors)