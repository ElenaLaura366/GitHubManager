import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GitHubManager")
        self.setGeometry(100, 100, 1000, 600)
        label = QLabel("Bine ai venit în GitHubManager!", self)
        label.move(200, 200)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
