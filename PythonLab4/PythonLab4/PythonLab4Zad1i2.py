import urllib.request
from bs4 import BeautifulSoup
import re

# Get page html
def get_html(url):
    req = urllib.request.Request(url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla'
    })
    resp = urllib.request.urlopen(req)
    data = resp.read() # page in bytes
    html = data.decode('latin-1') # page in string

    return html

# Get links
hrefsName = ['https://www.pwsz.suwalki.pl']
hrefsDuplicate = [0]
hrefsNumber = 0

for href in hrefsName:
    soup = BeautifulSoup(get_html(href), "html.parser")

    print("Searching: " + href + "\n")
    
    for a in soup.findAll('a', attrs={'href': re.compile("^https://")}):
        link = a.get('href')
    
        if (link.find("pwsz.suwalki.pl") == -1):
            continue

        if link in hrefsName:
            print("Duplicate: " + link)
            hrefsDuplicate[hrefsName.index(link)] = hrefsDuplicate[hrefsName.index(link)] + 1
            continue

        hrefsDuplicate.append(1)
        hrefsName.append(link)

        print("New: " + link)

    hrefsNumber = hrefsNumber + 1
    print("Links checked: " + str(hrefsNumber))

    print(100 * "-")

# Concatenate and sort lists
hrefs = list(zip(hrefsName, hrefsDuplicate))
sortedHrefs = sorted(hrefs, key=lambda tup: tup[1], reverse=True)

# Display all links
print("All links:")
for href in hrefs:
    print(href)

print(100 * "-")

# Display top n links
n = 5
print("Top " + str(n) + " links:")
for i in range(0, n):
    print(sortedHrefs[i])

print(100 * "-")