import requests
from bs4 import BeautifulSoup
import pandas as pd
import base64


class Parser:
    def __init__(self):
        self.cookies = {
            'fp': '11fa6ff18da1fc58eb98815ba9da0600',
        }

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            # 'Cookie': 'fp=11fa6ff18da1fc58eb98815ba9da0600',
            'Upgrade-Insecure-Requests': '1',
        }

    def get_country_names(self):
        s = requests.Session()
        # response = s.get('http://free-proxy.cz/en',
        #                  cookies=self.cookies, headers=self.headers)

        response = s.get('https://advanced.name/freeproxy',
                         cookies=self.cookies, headers=self.headers)

        # with open('index.html', 'w') as f:
        #     f.write(response.text)

        soup = BeautifulSoup(response.text, 'lxml')
        select_elements = soup.find_all(
            'select', class_='form-control input-sm')
        countryElement = select_elements[1].find_all('option')

        country_names = []

        for c in countryElement:
            country = c.text
            country_names.append(country)

        country_names.remove('ALL')

        return country_names

    def parse_free_proxies(self, selected_country):
        url = f'https://advanced.name/freeproxy?country={selected_country}'

        s = requests.Session()
        response = s.get(url, cookies=self.cookies, headers=self.headers)
        proxy_list = []
        print(f'Код ответа сайта: {response.status_code}')
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            table_trs = soup.find('table', id='table_proxies').find(
                'tbody').find_all('tr')

            for tr in table_trs:
                try:
                    td_cells = tr.find_all('td')
                    ip_data = td_cells[1].get('data-ip')  # Получаем значение атрибута data-ip
                    port_data = td_cells[2].get('data-port')  # Получаем значение атрибута data-port
                    protocol = td_cells[3].find('a', class_='label').text.strip()
                    country = td_cells[4].find('a').text.strip()

                    # Декодируем значения data-ip и data-port из формата base64
                    ip = base64.b64decode(ip_data).decode('utf-8').strip()
                    port = base64.b64decode(port_data).decode('utf-8').strip()

                    proxy_list.append([ip.strip(), port.strip(), protocol.strip(), country.strip()])
                    proxyDf = pd.DataFrame(proxy_list)
                except Exception as ex:
                    print(f'Exception here: {ex}')
                    continue

            print(proxyDf)
            return proxyDf

        else:
            print(
                f'Что-то пошло не так! Статус код ответа: {response.status_code}')

    def main(self, index):
        try:
            selected_country = self.get_country_names()[index]
            return self.parse_free_proxies(selected_country)
        except Exception as ex:
            print(f'Error in parser: {ex}')
        finally:
            print('Wow')


if __name__ == '__main__':
    parser = Parser()
    proxy_data = parser.main(0)  # Индекс выбранной страны (в данном случае 0)
    try:
        print(f'Proxy: {proxy_data}')
    except Exception as ex:
        print(f'Error in parser like: {ex}')
