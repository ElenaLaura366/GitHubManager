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

    def setup_ui(self):
        self.setWindowTitle('GitHub Repository Manager')
        self.setGeometry(100, 100, 480, 320)
        layout = QVBoxLayout()

        # Add widgets for repository management
        self.repo_name_input = QLineEdit(self)
        self.repo_name_input.setPlaceholderText("Enter repository name")
        layout.addWidget(self.repo_name_input)

        add_button = QPushButton('Add Repository', self)
        add_button.clicked.connect(self.on_add_button_clicked)
        layout.addWidget(add_button)

        delete_button = QPushButton('Delete Repository', self)
        delete_button.clicked.connect(self.on_delete_button_clicked)
        layout.addWidget(delete_button)

        fetch_button = QPushButton('Fetch Repositories', self)
        fetch_button.clicked.connect(self.on_fetch_button_clicked)
        layout.addWidget(fetch_button)

        self.repos_label = QLabel(self)
        layout.addWidget(self.repos_label)

        self.setLayout(layout)

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
