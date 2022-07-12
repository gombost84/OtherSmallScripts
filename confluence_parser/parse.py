import requests
import json
from bs4 import BeautifulSoup as bs
import re

# Authentication details for OAuth
email = ''
auth_token = ''

# For assembling the needed links
baseLink = ''
spaceLink = baseLink + ''
pageLink = baseLink + ''
linkAttributes = ''

pattern = r''
header = {'Content-type': 'application/json'}

# Get the list of pages in the space
r = requests.get(spaceLink, auth = (email, auth_token))

# Make into readable format
jsonContent = r.json()

# We only need to extract the pade ids and titles
pageIDs = dict(zip(list(x['id'] for x in jsonContent['page']['results']), list(x['title'] for x in jsonContent['page']['results'])))


# There are some weird titles in the list.
# Remove those so only the ones with "new" in the title remain
tempList = []
for key, value in pageIDs.items():
    if not re.search(r'.new.|.New.|.NEW.', value):
        tempList.append(key)

for x in tempList:
    del pageIDs[x]

# Function for downloading a page
# Extracting and
# updating the links and
# uploading it to confluence
# As input, it needs a pageid

def linkupdates(pageid):
    # Download the page by ID
    page = requests.get(pageLink + pageid + linkAttributes, auth = (email, auth_token))
    page = page.json()
    # Put it through BeautifulSoup
    soup = bs(page['body']['storage']['value'], features = "html.parser")
    for x in soup.find_all('a'):
        if re.search(pattern, x['href']):
            x['href'] = re.sub(pattern, '', x['href'])
            for key, value in pageIDs.items():
                if re.sub(r"\s(new)", "", value) == x.string:
                    x['href'] = re.sub(x['href'].split("/")[-1], key, x['href'])
                    print(x['href'])

    page['body']['storage']['value'] = str(soup)
    page['version']['number'] += 1
    page = json.dumps(page)

    r2 = requests.put(pageLink + pageid, data = page, headers = header, auth = (email, auth_token))

    return r2

print(linkupdates(''))
