import sys
import os
import json
import time
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView, QFileDialog, QVBoxLayout, QDialog, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from UI.ui import Ui_MainWindow
from parser.parser import Parser
import folium
import requests
import psycopg2
from psycopg2 import sql


class ProxyTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.headers = ["IP", "Port", "Protocol", "Country"]
        self.data_frame = None

    def setItems(self, items):
        if isinstance(items, pd.DataFrame):
            self.data_frame = items
            self.beginResetModel()
            self.endResetModel()
        else:
            self.data_frame = None
            self.beginResetModel()
            self.endResetModel()

    def rowCount(self, parent=QModelIndex()):
        if self.data_frame is not None:
            return self.data_frame.shape[0]
        return 0

    def columnCount(self, parent=QModelIndex()):
        return len(self.headers)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[section]
        return super().headerData(section, orientation, role)

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            if 0 <= row < self.rowCount() and 0 <= col < self.columnCount():
                return str(self.data_frame.iloc[row, col])
        return None


class MapWindow(QDialog):
    def __init__(self, map_file, parent=None):
        super(MapWindow, self).__init__(parent)
        self.setWindowTitle("Proxy Map")
        self.resize(800, 600)

        layout = QVBoxLayout()
        self.web_view = QWebEngineView()

        try:
            with open(map_file, 'r', encoding='utf-8') as file:
                html_content = file.read()
                self.web_view.setHtml(html_content)
        except Exception as e:
            print(f"Ошибка при чтении файла карты: {e}")

        layout.addWidget(self.web_view)
        self.setLayout(layout)


class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()

        self.parser = Parser()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.parse_proxies)
        self.ui.pushButton_3.clicked.connect(self.save_proxies_to_json)
        self.ui.pushButton_4.clicked.connect(self.create_map)
        self.ui.pushButton_5.clicked.connect(self.show_map)

        self.populate_combo_box()

        self.db_connection = psycopg2.connect(
            host="localhost",
            database="Proxies",
            user="m3rcy",
            password="1337"
        )
        self.db_cursor = self.db_connection.cursor()
        self.create_table()

    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS proxies (
            ip VARCHAR(255) PRIMARY KEY,
            port VARCHAR(255),
            protocol VARCHAR(255),
            country VARCHAR(255)
        )
        """
        self.db_cursor.execute(create_table_query)
        self.db_connection.commit()

    def closeEvent(self, event):
        # Закрытие соединения с базой данных при закрытии приложения
        self.db_cursor.close()
        self.db_connection.close()
        super().closeEvent(event)

    def save_proxies_to_db(self, proxies):
        try:
            insert_query = sql.SQL("""
                INSERT INTO proxies (ip, port, protocol, country)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (ip) DO NOTHING
            """)
            for row in proxies.itertuples(index=False):
                self.db_cursor.execute(insert_query, (row._0, row._1, row._2, row._3))
            self.db_connection.commit()
        except Exception as e:
            self.db_connection.rollback()
            print(f"Ошибка при сохранении данных в базу: {e}")

    def populate_combo_box(self):
        try:
            country_names = self.parser.get_country_names()
            self.ui.comboBox.addItems(country_names)
        except Exception as ex:
            print(f'Error parser first: {ex}')

    def parse_proxies(self):
        selected_country_index = self.ui.comboBox.currentIndex()
        selected_country = self.ui.comboBox.itemText(selected_country_index)

        proxy_data = self.parser.parse_free_proxies(selected_country)

        print(f"Proxy: {proxy_data}")

        # Создаем модель данных из списка
        proxy_model = ProxyTableModel()
        proxy_model.setItems(proxy_data)

        self.save_proxies_to_db(proxy_data)

        # Устанавливаем модель в таблицу
        self.ui.tableView.setModel(proxy_model)

        self.ui.tableView.setStyleSheet(
            "QTableView::item {"
            "            background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));"
            "            border-radius: 5px;"
            "            padding: 2px;"
            "            color: white;"
            "            color: rgb(255, 255, 255); }"
        )

        header = self.ui.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setStyleSheet(
            "QHeaderView::section {"
            "    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));"
            "    color: white;"
            "    border-radius: 5px;"
            "    padding: 2px;"
            "}"
        )

        column = self.ui.tableView.verticalHeader()
        column.setStyleSheet(
            "QHeaderView::section {"
            "    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));"
            "    color: white;"
            "    border: 1px solid rgba(255, 255, 255, 40);"
            "}"
        )

    def save_proxies_to_json(self):
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setDirectory(os.path.join(os.path.dirname(__file__), 'results'))
        selected_country_index = self.ui.comboBox.currentIndex()
        selected_country = self.ui.comboBox.itemText(selected_country_index)

        file_name = selected_country
        file_path = file_dialog.getSaveFileName(self, "Save result", f"results/{file_name}",
                                                "JSON Files (*.json);;All Files (*)")

        if file_path:
            data = {}

            table_model = self.ui.tableView.model()

            for row in range(table_model.rowCount()):
                ip = table_model.index(row, 0).data(Qt.DisplayRole)
                port = table_model.index(row, 1).data(Qt.DisplayRole)
                protocol = table_model.index(row, 2).data(Qt.DisplayRole)
                country = table_model.index(row, 3).data(Qt.DisplayRole)

                if country not in data:
                    data[country] = {protocol: [f"{ip}:{port}"]}
                elif protocol not in data[country]:
                    data[country][protocol] = [f"{ip}:{port}"]
                else:
                    data[country][protocol].append(f"{ip}:{port}")

            with open(f"results/{file_name}", 'w') as file:
                json.dump(data, file, indent=4)

            file_name_old = os.path.splitext(f'results/{file_name}')[0]
            new_file_name = f"{file_name_old}.json"
            os.rename(f"{file_name_old}", f"{new_file_name}")

    def location_IP(self, ip: str):
        try:
            ip = str(ip).strip()
            response = requests.get(f"http://ipwho.is/{ip}")
            #response = requests.get(f"http://ip-api.com/json/{ip}?lang=en")
            #response = requests.get(f"https://api.ip2location.io/?key=E88DCAEA1AC17AC1A8E86F623C007070&ip={ip}&format=json")
            if response.status_code != 200:
                print(f"Failed to retrieve data for IP: {ip}, Status code: {response.status_code}")
                return None

            result = response.json()
            if result["success"] == "false":
                print(f"Failed to retrieve data for IP: {ip}, Reason: {result['message']}")
                return None

            return result
        except json.decoder.JSONDecodeError:
            print(f"Error decoding JSON for IP: {ip}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def create_map(self):
        query = "SELECT ip FROM proxies"
        self.db_cursor.execute(query)
        proxies = self.db_cursor.fetchall()

        if not proxies:
            print("Нет прокси для отображения на карте.")
            return

        map_center = [0, 0]
        my_map = folium.Map(location=map_center, zoom_start=2)

        added_ips = set()
        city_ips = {}

        for proxy in proxies:
            ip_address = proxy

            if ip_address in added_ips:
                continue

            ip_address = ip_address[0] if isinstance(ip_address, tuple) else ip_address

            location_data = self.location_IP(str(ip_address))
            if location_data:
                city = location_data.get("city")

                latitude = location_data.get("latitude")
                longitude = location_data.get("longitude")
                if city and latitude and longitude:
                    if city not in city_ips:
                        city_ips[city] = {
                            "lat": latitude,
                            "lon": longitude,
                            "ips": []
                        }
                    city_ips[city]["ips"].append(ip_address)

        for city, data in city_ips.items():
            ip_list = "<br>".join(data["ips"])
            folium.Marker(
                location=[data["lat"], data["lon"]],
                popup=f"City: {city}<br>IPs:<br>{ip_list}",
                tooltip="Click for more info"
            ).add_to(my_map)

        map_file = "map/proxy_map.html"
        my_map.save(map_file)
        print(f"Карта сохранена в {map_file}")

    def show_map(self):
        map_file = "map/proxy_map.html"
        if not os.path.exists(map_file):
            print(f"Map not found {map_file}")
            return

        self.map_window = MapWindow(map_file)
        self.map_window.show()


def main():
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
