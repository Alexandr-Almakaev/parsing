from bs4 import BeautifulSoup
import requests as req


all_films = []
fout = open('base_ivi.txt', 'w', encoding='UTF-8')
link = 'https://www.ivi.ru/'


def get_html(k):
    url = 'https://www.ivi.ru/movies/page{}'.format(k)
    return req.get(url)


def pars(resp1):
    soup = BeautifulSoup(resp1.text, "html.parser")
    films = soup.find_all('span', class_='name')
    for i in films:
        all_films.append((i.text, link + i.parent.parent.get('href')))
        fout.write(i.text + '#DELIMETER#' + link + i.parent.parent.get('href') + '\n')


j = 1
resp = get_html(j)
while resp.status_code == 200:
    pars(resp)
    j += 1000
    resp = get_html(j)
fout.close()
