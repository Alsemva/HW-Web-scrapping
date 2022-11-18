import bs4
import requests
from fake_headers import Headers
KEYWORDS = ['интерфейс', 'фронтенд', 'микроэлектроника', 'java']
URL = 'https://habr.com/ru/all'


def get_date_title_url(soup):
    articles = soup.find_all("article")
    for article in articles:
        date = article.find("time").attrs["title"]
        title = article.find(class_="tm-article-snippet__title-link").find("span").text
        href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
        description = article.find(class_="article-formatted-body").text
        full_href = f"{URL[:-7]}{href}"
        for keyword in KEYWORDS:
            if (keyword in title) or (keyword in description):
                print(f"{date[:-7]} - {title} - {full_href}")
                break
    return "Done"


def get_scrapp():
    header = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    )
    response = requests.get(URL, headers=header.generate())
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    return get_date_title_url(soup)


def main():
    print(get_scrapp())


if __name__ == '__main__':
    main()
