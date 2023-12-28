from bs4 import BeautifulSoup4
import requests

website = 'https://thsconline.github.io/s/'
result = requests.get(website)


result.text