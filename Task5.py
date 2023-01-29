"""
Task 5
Use the BeautifulSoup and requests Python packages to print out a list of all the news titles
on the https://news.ycombinator.com/.
"""
import requests
from bs4 import BeautifulSoup


def get_html(url_link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'}
    response = requests.get(url_link, headers=headers)
    if response.status_code == 200:
        return response.text


def get_titles(url_link):
    """
    checked the source code of webpage and observed required titles are in a <span> with css class name titleline.
    Used findall to get all the spans elements with titleline class name. used gettext to get
    string from those elements.
    """
    html_content = get_html(url_link)
    soup = BeautifulSoup(html_content, 'html.parser')
    titles = soup.find_all(class_="titleline")
    titles = [title.get_text() for title in titles]
    return titles


def main():
    url_link = "https://news.ycombinator.com/"
    titles_list = get_titles(url_link)
    for title in titles_list:
        print(title)


# checking if file run as script as this file is imported in next task Task6. Otherwise it will run main function and
# print output during import process in Task6.
if __name__ == "__main__":
    main()
