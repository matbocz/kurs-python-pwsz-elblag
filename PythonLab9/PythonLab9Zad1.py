import urllib.request
import csv

from bs4 import BeautifulSoup


def get_html(url):
    req = urllib.request.Request(url,
                                 data=None,
                                 headers={
                                     'User-Agent': 'Mozilla'
                                 })
    resp = urllib.request.urlopen(req)
    data = resp.read()  # page in bytes
    html = data.decode("UTF-8")  # page in string

    return html


def get_table_header(table):
    header = []
    for th in table.thead.find_all("th"):
        text = th.text.replace('\t', '').strip()
        if "[MW]" in text:
            continue
        header.append(text)

    return header


def get_table_content(table):
    content = []
    rows = table.tbody.findChildren("tr")
    for row in rows:
        text_list = []
        cells = row.findChildren('td')
        for cell in cells:
            text = cell.text.strip()
            text_list.append(text)
        content.append(text_list)

    return content


def save_table_to_csv(table):
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(table)


date = input("Enter date (dd.mm.yyyy): ")

try:
    url = f"https://transparency.entsoe.eu/transmission-domain/physicalFlow/show?name=&defaultValue=false&viewType=TABLE&areaType=BORDER_BZN&atch=false&dateTime.dateTime={date}+00:00|UTC|DAY&border.values=CTY|10YPL-AREA-----S!BZN_BZN|10YPL-AREA-----S_BZN_BZN|10YCZ-CEPS-----N&dateTime.timezone=UTC&dateTime.timezone_input=UTC"
    soup = BeautifulSoup(get_html(url), "html.parser")
    table = soup.find("table")

    csv_table = []
    csv_table.append(get_table_header(table))
    csv_table.extend(get_table_content(table))
    save_table_to_csv(csv_table)

    print(csv_table)
except AttributeError:
    print("You entered an incorrect date! Try again.")
