#-------------------------------------------------------------------------
# AUTHOR: Ryan Hoang
# FILENAME: scraper.py
# SPECIFICATION: This program crawls the Circular Links section of
#                TestingURL.dev using the frontier and seen lists from the
#                pseudocode in Question 1. It prints the <h1> text of each
#                page it visits, follows only links that start with the
#                seed URL, and prints all URLs it has seen.
# FOR: CS 4250 - Assignment #2
# TIME SPENT: 2 hours
#-------------------------------------------------------------------------

# Importing Python libraries
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"
baseURL = "https://testingurl.dev"

# Creating the frontier and seen collections
# --> add your Python code here
frontier = [seed]
seen = [seed]

# Crawling until the frontier is empty
while frontier:

    # Removing the first URL from the frontier
    # --> add your Python code here
    url = frontier.pop(0)

    # Retrieving and parsing the Web page
    # --> add your Python code here
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Could not retrieve {url}: {e}")
        continue
    soup = BeautifulSoup(response.text, "html.parser")

    # Printing the text contained in the <h1> element
    # --> add your Python code here
    h1 = soup.find("h1")
    if h1 is not None:
        print(h1.get_text(strip = True))
    else:
        print(f"[Cannot find <h1> on {url}]")

    # Extracting and processing hyperlinks
    # --> add your Python code here
    for a in soup.find_all("a", href = True):
        link = urljoin(url, a["href"].strip())
        link, _ = urldefrag(link)
        if not link.startswith(seed):
            continue
        if link not in seen:
            seen.append(link)
            frontier.append(link)

# Printing all URLs in seen
# --> add your Python code here
print("All URLs in seen:")
for u in seen:
    print(u)