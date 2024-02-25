from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QVBoxLayout
from interface.gui import AppWindow


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login to GitHub')
        self.setGeometry(100, 100, 360, 180)

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your GitHub username")
        layout.addWidget(self.username_input)

        self.token_input = QLineEdit()
        self.token_input.setPlaceholderText("Enter your GitHub token")
        self.token_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.token_input)

        login_button = QPushButton('Login')
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        token = self.token_input.text()
        # You should validate the token here, for simplicity we just check if they are not empty
        if username and token:
            self.main_window = AppWindow(username, token)
            self.main_window.show()
            self.close()  # Close the login window
        else:
            QMessageBox.warning(self, "Error", "Please enter a username and token")
