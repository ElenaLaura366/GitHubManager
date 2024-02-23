import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

def on_button_clicked():
    QMessageBox.about(window, "Message", "Hello, PyQt!")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Simple PyQt App')
window.setGeometry(100, 100, 280, 80)  # x, y, width, height

button = QPushButton('Click Me', window)
button.clicked.connect(on_button_clicked)
button.move(100, 20)  # x, y

window.show()

sys.exit(app.exec_())
