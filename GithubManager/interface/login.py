from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from interface.gui import AppWindow
from backend.backend import check_github_user_exists
from backend.backend import check_github_token_validity


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login to GitHub')
        self.setGeometry(100, 100, 1000, 500)

        layout = QVBoxLayout()
        layout.setSpacing(10)  # Ajustează spațierea între elemente

        username_layout = QHBoxLayout()
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your GitHub username")
        self.username_input.setFixedSize(400, 40)
        username_layout.addWidget(self.username_input, alignment=Qt.AlignCenter)
        layout.addLayout(username_layout)

        token_layout = QHBoxLayout()
        self.token_input = QLineEdit()
        self.token_input.setPlaceholderText("Enter your GitHub token")
        self.token_input.setEchoMode(QLineEdit.Password)
        self.token_input.setFixedSize(400, 40)
        token_layout.addWidget(self.token_input, alignment=Qt.AlignCenter)
        layout.addLayout(token_layout)

        login_button_layout = QHBoxLayout()
        login_button = QPushButton('Login')
        login_button.setFixedSize(400, 40)
        login_button.clicked.connect(self.handle_login)
        login_button_layout.addWidget(login_button, alignment=Qt.AlignCenter)
        layout.addLayout(login_button_layout)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        token = self.token_input.text()
        if not username or not token:
            QMessageBox.warning(self, "Error", "Please enter a username and token")
            return
        if check_github_user_exists(username) and check_github_token_validity(token):
            self.main_window = AppWindow(username, token)
            self.main_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or token. Please try again.")