import sqlite3

import requests
from bs4 import BeautifulSoup
from config import DATABASE_NAME


def get_sours(url):
    import requests

    cookies = {
        'rdt': '5933ed29b6bd0b3ee80048210c55dd65',
        'edgebucket': 'T1DwZUNlnsWfDjYEcc',
        'loid': '000000000ml5zwuom9.2.1698339277734.Z0FBQUFBQmxPcG5ONU5jRF84bWZhTTZic1gwZGQ0TENzNkRRN0M5NlctWDdwTWdfdHZJME9YdnhZR21vZjhDVWRGTHVXQnQ3TUJ3TGlFeFZuUTd1aHhLaTA5WVI3aVdmUExJaUFYRjBvYWVyUTUzSldzMjJJdEpIQ3gyci1OUTBLWDgtLXZSY0JqX3A',
        'session_tracker': 'adofkcljmocfaadhaq.0.1698341243744.Z0FBQUFBQmxPcUY3eHFoNTV3R21Ea0pJMXk0dldnWjlxVmtkemtwdGx1N1E4UjktenF0eHBkUzBFdU9ZRFY2SDY3YW84X3lKbjdpU0FaaURQN1luLWhMZUpTYU5oaGpFbm4wZTFFSHhWN0NIQVo4SmI4QlBnWEF3bEdNbS1rR1VxamdZUU9GUU5WSjY',
        'csrf_token': 'c8e7361056b4597233a0d6fd16dfa8ea',
        'token_v2': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJsb2lkIiwiZXhwIjoxNjk4NDI1Njc3LjczNDk2NCwiaWF0IjoxNjk4MzM5Mjc3LjczNDk2NCwianRpIjoiQVkxQWdOejdUQ09NWE1tMGhxV3ZhN09DVFpPOW53IiwiY2lkIjoiMFItV0FNaHVvby1NeVEiLCJsaWQiOiJ0Ml9tbDV6d3VvbTkiLCJsY2EiOjE2OTgzMzkyNzc3MzQsInNjcCI6ImVKeGtrZEdPdERBSWhkLWwxejdCX3lwX05odHNjWWFzTFFhb2szbjdEVm9jazcwN2NENHBIUDhuS0lxRkxFMnVCS0c0eXBsNzgxNFdMSVZNMDVRR3RheEFrcWIwSkRXV2Q1b1NGV3hHNW5LbEhTczBlR0NhVXVXU3VTMzB1TFFKemQxWTlPekVxTXBsNVVGVm9QVlVqVzFNWVh0aWZMT3gycENLNjNJcUUxZ1d5bWZ4b2g5eTlkWS1mN2JmaEhZd3JLZ0tEX1RPdUZWd1lfSERGSFpfVDAxNnRpNVkxTjdyUVdxZjYzRzc5bG16ME96Y2ZxN25yNDFrWEk2aC1RbjI3NjVmUWdjZWVWNW0xQUdNV01PUE11eklPdnlyRHFCeVFRRmpDZUxUQ09USzVkdF9DYlpyMDdfRzdSTV9mRFBpcGpmODFnelVjd25pMEtmeDlSc0FBUF9fSV9yYXVRIiwiZmxvIjoxfQ.cQvjkTGsZcpPRhvgByrdQO2Fr-hwEe6aJssH9JKC1nvo3HJW5q2hnsnnk5oQa1ZSgDzTy5qEBlzf_AZa3i8QGCL59x3NRRt7fiXaK2OCOddmkVzMLyy26Oc_GgrZlk1Z65taVGYmY2fJOz-UXDpeS0QDSK0xIlpiLXPiBurFdNultI93ZPipRoM_8YQahuD7Sfd4wDJT5ByZ8lrFQyNYRyHTRrJjv3BJdxHlEry8KJWq7gz_lxEiq9BaIee3vdDLirPfk4lACD61vkrFgMPI4RZFp9qupiwBw2hyePlgPYRB7kJHqUO2ANqTAp2gqTaQ9sx7M49lihdw-yvshPIvxA',
        'csv': '2',
        'pc': 'vn',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-EN,en;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        # 'Cookie': 'rdt=5933ed29b6bd0b3ee80048210c55dd65; edgebucket=T1DwZUNlnsWfDjYEcc; loid=000000000ml5zwuom9.2.1698339277734.Z0FBQUFBQmxPcG5ONU5jRF84bWZhTTZic1gwZGQ0TENzNkRRN0M5NlctWDdwTWdfdHZJME9YdnhZR21vZjhDVWRGTHVXQnQ3TUJ3TGlFeFZuUTd1aHhLaTA5WVI3aVdmUExJaUFYRjBvYWVyUTUzSldzMjJJdEpIQ3gyci1OUTBLWDgtLXZSY0JqX3A; session_tracker=adofkcljmocfaadhaq.0.1698341243744.Z0FBQUFBQmxPcUY3eHFoNTV3R21Ea0pJMXk0dldnWjlxVmtkemtwdGx1N1E4UjktenF0eHBkUzBFdU9ZRFY2SDY3YW84X3lKbjdpU0FaaURQN1luLWhMZUpTYU5oaGpFbm4wZTFFSHhWN0NIQVo4SmI4QlBnWEF3bEdNbS1rR1VxamdZUU9GUU5WSjY; csrf_token=c8e7361056b4597233a0d6fd16dfa8ea; token_v2=eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJsb2lkIiwiZXhwIjoxNjk4NDI1Njc3LjczNDk2NCwiaWF0IjoxNjk4MzM5Mjc3LjczNDk2NCwianRpIjoiQVkxQWdOejdUQ09NWE1tMGhxV3ZhN09DVFpPOW53IiwiY2lkIjoiMFItV0FNaHVvby1NeVEiLCJsaWQiOiJ0Ml9tbDV6d3VvbTkiLCJsY2EiOjE2OTgzMzkyNzc3MzQsInNjcCI6ImVKeGtrZEdPdERBSWhkLWwxejdCX3lwX05odHNjWWFzTFFhb2szbjdEVm9jazcwN2NENHBIUDhuS0lxRkxFMnVCS0c0eXBsNzgxNFdMSVZNMDVRR3RheEFrcWIwSkRXV2Q1b1NGV3hHNW5LbEhTczBlR0NhVXVXU3VTMzB1TFFKemQxWTlPekVxTXBsNVVGVm9QVlVqVzFNWVh0aWZMT3gycENLNjNJcUUxZ1d5bWZ4b2g5eTlkWS1mN2JmaEhZd3JLZ0tEX1RPdUZWd1lfSERGSFpfVDAxNnRpNVkxTjdyUVdxZjYzRzc5bG16ME96Y2ZxN25yNDFrWEk2aC1RbjI3NjVmUWdjZWVWNW0xQUdNV01PUE11eklPdnlyRHFCeVFRRmpDZUxUQ09USzVkdF9DYlpyMDdfRzdSTV9mRFBpcGpmODFnelVjd25pMEtmeDlSc0FBUF9fSV9yYXVRIiwiZmxvIjoxfQ.cQvjkTGsZcpPRhvgByrdQO2Fr-hwEe6aJssH9JKC1nvo3HJW5q2hnsnnk5oQa1ZSgDzTy5qEBlzf_AZa3i8QGCL59x3NRRt7fiXaK2OCOddmkVzMLyy26Oc_GgrZlk1Z65taVGYmY2fJOz-UXDpeS0QDSK0xIlpiLXPiBurFdNultI93ZPipRoM_8YQahuD7Sfd4wDJT5ByZ8lrFQyNYRyHTRrJjv3BJdxHlEry8KJWq7gz_lxEiq9BaIee3vdDLirPfk4lACD61vkrFgMPI4RZFp9qupiwBw2hyePlgPYRB7kJHqUO2ANqTAp2gqTaQ9sx7M49lihdw-yvshPIvxA; csv=2; pc=vn',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-GPC': '1',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get('https://old.reddit.com/r/Tacticus_Codes/', cookies=cookies, headers=headers)

    # with open("redit.html", "w") as file:
    #     file.write(response.text)

    response = response.text

    # with open("redit.html", "r") as file:
    #     response = file.read()

    soup = BeautifulSoup(response, "lxml")
    return soup


def get_list(soup, search_word):
    add_url = 'https://www.reddit.com'
    urls_list = soup.find_all("a", class_="title may-blank", href=lambda href: href and search_word in href)

    result = []
    for url in urls_list:
        url = url['href']
        result.append(add_url + url)
    return result


def duplicate_checking(data):
    result_list = []
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    for url in data:
        # Проверка наличия записи в базе данных
        cursor.execute("SELECT * FROM tacticus WHERE url = ?", (url,))
        result = cursor.fetchone()

        if result is None:
            # Если записи нет, добавляем ее в базу данных
            cursor.execute("INSERT INTO tacticus (url, date) VALUES (?, date('now'))", (url,))
            result_list.append(url)
    conn.commit()
    conn.close()
    if not result_list:
        return None
    else:
        return result_list


def scrap():
    url = 'https://old.reddit.com/r/Tacticus_Codes/ '
    search_word = "new_code"
    soup = get_sours(url)
    data = get_list(soup, search_word)
    result = duplicate_checking(data)
    return result


if __name__ == '__main__':
    scrap()

