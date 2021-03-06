from bs4 import BeautifulSoup
from requests import get
from csv import writer

with open('sow_titles.csv', 'w', encoding='utf-8', newline='') as f:
    thewriter = writer(f)
    header = ['title']
    thewriter.writerow(header)

    URL = 'https://schoolofwok.co.uk/tips-and-recipes?sort=latest&filter=recipe'
    page = get(URL)
    url = 'https://schoolofwok.co.uk'
    bs = BeautifulSoup(page.content, 'html.parser')
    links_list = []

    for recipe in bs.find_all('div', class_='col-xs-6 col-md-3'):
        titles = recipe.find('span', class_='title').get_text().strip()
        links = recipe.find('a')['href']
        new_links = url + links
        links_list.append(new_links)
        info = [titles]
        thewriter.writerow(info)
