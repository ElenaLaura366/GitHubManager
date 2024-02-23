import sys

from PyQt5.QtWidgets import QApplication

from interface.gui import AppWindow  # Adjust this import according to your project structure


def main():
    app = QApplication(sys.argv)
    mainwindow = AppWindow()
    mainwindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    