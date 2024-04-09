from bs4 import BeautifulSoup
import requests

cookies = {
    'fp': 'ec705e43b61df0749b6c3ffcb98bfb85',
}

proxies = {
    'https': 'http://72.10.160.173:18047',
    'http': 'http://72.10.160.173:18047'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://free-proxy.cz/en/',
    'Connection': 'keep-alive',
    # 'Cookie': 'fp=ec705e43b61df0749b6c3ffcb98bfb85',
    'Upgrade-Insecure-Requests': '1',
}

# s = requests.Session()
# response = s.get('http://free-proxy.cz/en/proxylist/country/US/all/ping/all',
#                  cookies=cookies, headers=headers, proxies=proxies)


def get_location(url):
    response = requests.get(url=url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(response.text, 'lxml')

    ip = soup.find('div', class_='ip').text.strip()
    location = soup.find('div', class_='value-country').text.strip()

    print(f'IP: {ip}\nLocation: {location}')


def main():
    get_location(url='https://2ip.ru')


if __name__ == '__main__':
    main()


    # def parse_proxies(self):
    #     selected_country_index = self.ui.comboBox.currentIndex()
    #     selected_country = self.ui.comboBox.itemText(selected_country_index)
    #
    #     proxy_data = self.parser.parse_free_proxies(selected_country)
    #
    #     # вложенные списки
    #     proxy_list = proxy_data.values.tolist()
    #
    #     proxyList = list(itertools.chain.from_iterable(proxy_list))
    #
    #     print(proxyList)
    #
    #     # Создаем модель данных из списка
    #     proxy_model = ProxyTableModel(proxyList)
    #
    #     # Устанавливаем модель в таблицу
    #     self.ui.tableView.setModel(proxy_model)
    #
    #     # Добавляем данные в модель
    #     for row_index in range(len(proxyList) // 4):  # Учитываем, что у нас есть 4 столбца
    #         for col_index in range(4):
    #             proxy_model.setData(proxy_model.index(row_index, col_index), proxyList[row_index * 4 + col_index])
    #
    #     # Устанавливаем модель в таблицу
    #     self.ui.tableView.setModel(proxy_model)
    #
    #     self.ui.tableView.setStyleSheet("QTableView { background-color: rgba(255, 255, 255, 30);"
    #                                     "            border: 4px rgba(255, 255, 255, 40);"
    #                                     "            border-radius: 7px;"
    #                                     "            color: rgb(255, 255, 255); }")
    #
    #     header = self.ui.tableView.horizontalHeader()
    #     header.setStyleSheet("QTableView { background-color: rgba(255, 255, 255, 30);"
    #                          "            border: 4px rgba(255, 255, 255, 40);"
    #                          "            border-radius: 7px;"
    #                          "            color: rgb(255, 255, 255); }")
