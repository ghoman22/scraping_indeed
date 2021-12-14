import os
import requests
from bs4 import BeautifulSoup


url = 'https://www.indeed.com/jobs?'
params= {
    'q': 'Python Developer',
    'l': 'New York State'
    }
headers = {
'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}

res=requests.get(url, params=params, headers=headers)
# soup = BeautifulSoup(res.text, 'html.parser')

def get_total_pages():
    params = {
        'q': 'Python Developer',
        'l': 'New York State'
    }

    res = requests.get(url, params=params, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

        total_pages = []

#     scraping step
        soup = BeautifulSoup(res.text, 'html.parser')
        pagination = soup.find('ul', 'pagination-list')
        pages = pagination.find_all('li')
        for page in pages:
            total_pages.append(page.text)
        print(total_pages)

if __name__ == '__main__':
    get_total_pages()
