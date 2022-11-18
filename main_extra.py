import bs4
import requests
from fake_headers import Headers
KEYWORDS = ['интерфейс', 'фронтенд', 'микроэлектроника', 'прокси']


def get_date_title_url(soup, url):
    articles = soup.find_all("article")
    for article in articles:
        date = article.find("time").attrs["title"]
        title = article.find(class_="tm-article-snippet__title-link").find("span").text
        href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
        description = article.find(class_="article-formatted-body").text
        full_href = f"{url[:-7]}{href}"
        full_article_soup = get_scrapp(full_href)
        full_article = full_article_soup.find(class_="article-formatted-body").find("div").text
        # print(full_href)
        for keyword in KEYWORDS:
            if (keyword in title) or (keyword in description) or (keyword in full_article):
                print(f"{date[:-7]} - {title} - {full_href}")
                break
    return "Done"


def get_scrapp(url):
    header = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    )
    response = requests.get(url, headers=header.generate())
    text = response.text
    return bs4.BeautifulSoup(text, features='html.parser')


def main():
    url = 'https://habr.com/ru/all'
    soup = get_scrapp(url)
    print(get_date_title_url(soup, url))


if __name__ == '__main__':
    main()
