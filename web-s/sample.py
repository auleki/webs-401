import requests 
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'

res = requests.get(URL)

soup = BeautifulSoup(res.content, 'html.parser')

results = soup.find(id="ResultsContainer")

job_cards = results.find_all('section', class_='card-content')

for job_card in job_cards:
  title_elem = job_card.find('h2', class_='title'))
  company_elem = job_card.find('div', class_="company"))
  location_elem = job_card.find('div', class_='location'))
  print(title_elem)
  print(company_elem)
  print(location_elem)
  print()




