import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QVBoxLayout
from backend.backend import fetch_repositories


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple PyQt App')
        self.setGeometry(100, 100, 360, 180)  # x, y, width, height

        layout = QVBoxLayout(self)

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter your username")
        layout.addWidget(self.username_input)

        self.token_input = QLineEdit(self)
        self.token_input.setPlaceholderText("Enter your token")
        self.token_input.setEchoMode(QLineEdit.Password)  # ascunde tokenul
        layout.addWidget(self.token_input)

        button = QPushButton('Fetch Repositories', self)
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button)

    def on_button_clicked(self):
        username = self.username_input.text()
        token = self.token_input.text()
        repos = fetch_repositories(username, token)
        if repos is not None:
            message = ""
            for repo in repos:
                message += f"Project Name: {repo['name']}\nProject URL: {repo['html_url']}\n"
            QMessageBox.about(self, "Your Projects", message)
        else:
            QMessageBox.warning(self, "Error", "Could not fetch repositories")