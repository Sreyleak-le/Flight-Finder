from urllib import response
from bs4 import BeautifulSoup
import requests

url = 'https://www.aircanada.com/us/en/aco/home/app.html#/faredriven'
cookies = {'session_id': 'asdfasdfasdfasdfasdf'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.example.com/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}
proxy_addresses = {
    # 'http': 'http://129.146.16.244:8888',
    'http': '136.243.89.93:8888'
}

session = requests.session()

def scrape_title(url):
    response = session.get(url, proxies=proxy_addresses, headers=headers)
    if response.status_code == 200:
        # Parse the html on that url
        soup = BeautifulSoup(response.text,'html.parser')
        title = soup.title.text
        # h1 = soup.find('h1').text
        print(title)
        # print(h1)
    else:
        print(response.status_code)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scrape_title(url)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
