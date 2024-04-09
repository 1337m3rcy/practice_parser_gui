import sys

import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QHeaderView
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from UI.ui import Ui_MainWindow
from parser.parser import Parser


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


class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()

        self.parser = Parser()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.parse_proxies)

        self.populate_combo_box()

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

        # Создаем модель данных из списка
        proxy_model = ProxyTableModel()

        proxy_model.setItems(proxy_data)

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


def main():
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
