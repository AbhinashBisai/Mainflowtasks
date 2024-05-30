import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://www.google.com'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the elements containing the data you want to scrape
# For example, if you want to scrape all the links on the page:
links = soup.find_all('a')

# Extract the data from the elements
for link in links:
    print(link['href'])
