from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta


def scrape(time_boundaries):
    r = requests.get('https://www.unian.ua/detail/all_news')
    main_soup = BeautifulSoup(r.content, features='lxml')
    news_ul = main_soup.find('div', {'id': 'block_allnews_list_items'}).ul
    pages = []
    today = datetime.now()
    now = datetime.now()
    for tag in news_ul.children:
        if 'date' in tag['class']:
            today -= timedelta(days=1)
            continue
        elif 'link' not in tag['class']:
            continue
        time = list(map(lambda x: int(x), tag.div.span.string.split(':')))
        new_dt = today.replace(hour=time[0], minute=time[1])
        link = tag.div.a['href']
        pages.append((new_dt, link))

    for dt, link in pages[:]:
        if (now - dt).seconds > time_boundaries:
            pages.remove((dt, link))

    news = []
    for dt, link in pages:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, features='lxml')
        article = soup.find('div', {'class': 'article-text'})
        header = article.h1.string
        contents = article.find('div', {'class': 'clearfix'})
        text = ''.join([x.string for x in contents.children if x.string and x.name == 'p'])
        news.append({
            'header': header,
            'link': link,
            'text': text,
            'img': contents.div.img['src']
        })
    return news


if __name__ == '__main__':
    aa = scrape(30 * 60)
    print(aa)
