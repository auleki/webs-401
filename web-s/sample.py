import requests 
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'

res = requests.get(URL)

soup = BeautifulSoup(res.content, 'html.parser')

results = soup.find(id="ResultsContainer")

job_cards = results.find_all('section', class_='card-content')
python_jobs = results.find_all('h2')

for job in job_cards:
  # link = job.find('a')['href']
  job_title = job.find('div', class_="company")
  print(job_title.text)
  # print(f"Apply here {link}")
  


for job_card in job_cards:
  title_elem = job_card.find('h2', class_='title')
  company_elem = job_card.find('div', class_="company")
  location_elem = job_card.find('div', class_='location')
  if None in (title_elem, company_elem, location_elem):
    continue
  print(title_elem.text.strip())
  print(company_elem.text.strip())
  print(location_elem.text.strip())
  print()




