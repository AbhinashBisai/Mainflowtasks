import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to extract information from a webpage
def extract_info(url):
    # Send a GET request to fetch the HTML content
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract text
    text = soup.get_text()

    # Extract links
    base_url = url  # Base URL for resolving relative URLs
    links = [urljoin(base_url, link.get('href')) for link in soup.find_all('a')]

    # Extract images
    images = [urljoin(base_url, img.get('src')) for img in soup.find_all('img')]

    return {
        "text": text,
        "links": links,
        "images": images
    }

# Example usage
url = 'https://www.amazon.in'
info = extract_info(url)
print("Extracted Text:")
print(info["text"])

print("\nExtracted Links:")
for link in info["links"]:
    print(link)

print("\nExtracted Images:")
for img in info["images"]:
    print(img)
