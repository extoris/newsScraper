import sqlite3

import requests
from bs4 import BeautifulSoup
from config import DATABASE_NAME


def get_sours(url):
    response = requests.get(url=url, verify=False)

    # with open("news.html", "w") as file:
    #     file.write(response.text)

    soup = BeautifulSoup(response.text, "lxml")
    return soup


def get_title(soup, search_word):
    add_url = 'https://www.paritetbank.by'
    news_list = soup.find_all("a", href=lambda href: href and search_word in href)
    result = {}
    for news in news_list:
        title = news.find('p').text
        url = add_url + news['href']
        result[title] = url
    return result


def duplicate_checking(data):
    result_list = dict()
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    for i in data:

        title = i
        url = data[i]

        # Проверка наличия записи в базе данных
        cursor.execute("SELECT * FROM news WHERE url = ?", (url,))
        result = cursor.fetchone()

        if result is None:
            # Если записи нет, добавляем ее в базу данных
            cursor.execute("INSERT INTO news (title, url, date) VALUES (?, ?, date('now'))", (title, url))
            result_list[title] = url
    conn.commit()
    conn.close()
    if result_list == {}:
        return None
    else:
        return result_list


def scrap():
    url = 'https://www.paritetbank.by/about/news/'
    search_word = 'kombo'
    soup = get_sours(url)
    news = get_title(soup, search_word)
    return duplicate_checking(news)


if __name__ == '__main__':
    scrap()
