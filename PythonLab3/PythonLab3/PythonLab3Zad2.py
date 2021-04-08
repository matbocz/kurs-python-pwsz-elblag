import urllib.request
from bs4 import BeautifulSoup
import csv

def get_html(url):
    req = urllib.request.Request(url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla'
    })
    resp = urllib.request.urlopen(req)
    data = resp.read() # page in bytes
    html = data.decode("UTF-8") # page in string

    return html

def get_table_header(table):
    header = []
    for th_id, th in enumerate(table.thead.find_all("th")):
        if (th_id == 0):
            continue
        header.append(th.text.replace('\n', ' ').strip())

    return header

def save_table_header(fileName, header):
    with open(fileName, mode='w') as csv_file:
        fieldnames = header
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

url = "https://www.worldometers.info/coronavirus/"

soup = BeautifulSoup(get_html(url), "html.parser")
table = soup.find("table", attrs={"id": "main_table_countries_today"})

fileName = 'corona.csv'
header = get_table_header(table)
save_table_header(fileName, header)

print(get_table_header(table))