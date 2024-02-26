from PyQt5.QtWidgets import QWidget, QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from backend.backend import fetch_repositories
from backend.backend import create_repository
from backend.backend import delete_repository


class AppWindow(QWidget):
    def __init__(self, username, token):
        super().__init__()
        self.username = username
        self.token = token
        self.setup_ui()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login to GitHub')
        self.setGeometry(100, 100, 1000, 500)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)  # Reducem spațiul dintre widgeturi

        # Username layout
        username_layout = QHBoxLayout()
        username_layout.addStretch(1)
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your GitHub username")
        self.username_input.setFixedSize(400, 40)
        username_layout.addWidget(self.username_input)
        username_layout.addStretch(1)
        main_layout.addLayout(username_layout)

        # Token layout
        token_layout = QHBoxLayout()
        token_layout.addStretch(1)
        self.token_input = QLineEdit()
        self.token_input.setPlaceholderText("Enter your GitHub token")
        self.token_input.setEchoMode(QLineEdit.Password)
        self.token_input.setFixedSize(400, 40)
        token_layout.addWidget(self.token_input)
        token_layout.addStretch(1)
        main_layout.addLayout(token_layout)

        # Login button layout
        login_button_layout = QHBoxLayout()
        login_button_layout.addStretch(1)
        login_button = QPushButton('Login')
        login_button.clicked.connect(self.handle_login)
        login_button_layout.addWidget(login_button)
        login_button_layout.addStretch(1)
        main_layout.addLayout(login_button_layout)

        main_layout.setContentsMargins(10, 10, 10, 10)  # Setăm marginile exterioare ale layout-ului principal
        self.setLayout(main_layout)

    def on_add_button_clicked(self):
        repo_name = self.repo_name_input.text()
        result = create_repository(self.username, self.token, repo_name)
        if result:
            QMessageBox.information(self, "Success", f"Repository '{repo_name}' created successfully.")
        else:
            QMessageBox.critical(self, "Failure", "Failed to create repository.")

    def on_delete_button_clicked(self):
        repo_name = self.repo_name_input.text()
        if delete_repository(self.username, self.token, repo_name):
            QMessageBox.information(self, "Success", f"Repository '{repo_name}' deleted successfully.")
        else:
            QMessageBox.critical(self, "Failure", "Failed to delete repository.")

    def on_fetch_button_clicked(self):
        repos = fetch_repositories(self.username, self.token)
        if repos is not None:
            message = "Your Repositories:\n"
            message += '\n'.join([f"{repo['name']}" for repo in repos])
            self.repos_label.setText(message)
        else:
            QMessageBox.critical(self, "Failure", "Failed to fetch repositories.")
