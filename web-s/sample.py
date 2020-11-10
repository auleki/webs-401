import requests 
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'

res = requests.get(URL)

soup = BeautifulSoup(res.content, 'html.parser')

search_results = soup.find(id="ResultsContainer")

job_card = search_results.find_all('section', class_('card-content'))


