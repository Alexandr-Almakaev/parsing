from bs4 import BeautifulSoup
import requests as req


all_films = []
link = 'https://megogo.ru'
stop = '<link rel="canonical" href="http://megogo.ru/ru/films" />'
fout = open('base_megogo.txt', 'w', encoding='UTF-8')


def get_html(k):
    url = 'https://megogo.ru/ru/films/page_{}'.format(j)
    return req.get(url)


def pars(resp1):
    soup = BeautifulSoup(resp.text, "html.parser")
    films = soup.find_all('h3', class_='video-title')
    for i in films:
        all_films.append((i.text.strip(), link + i.parent.get('href')))
        fout.write(i.text.strip() + '#DELIMETER#' + link + i.parent.get('href') + '\n')


j = 1
resp = get_html(j)
while stop in resp.text and resp.status_code == 200:
    pars(resp)
    j += 1
    resp = get_html(j)
fout.close()
