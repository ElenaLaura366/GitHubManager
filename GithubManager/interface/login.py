from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QDesktopWidget, QSpacerItem, QSizePolicy, QLabel
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

        # Main layout that centers everything
        center_layout = QVBoxLayout()

        # Use a widget as a container for the center layout
        center_widget = QWidget()
        center_widget.setLayout(center_layout)

        # "Please Login" label with larger font
        login_label = QLabel("Please Login")
        login_label.setAlignment(Qt.AlignCenter)  # Ensure the label is centered
        # Customize the label's appearance with a larger font size
        login_label.setStyleSheet("font-size: 20pt; font-weight: bold;")
        center_layout.addWidget(login_label)

        # Container for username and token inputs
        input_container = QWidget()
        input_layout = QVBoxLayout(input_container)

        # Username input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your GitHub username")
        self.username_input.setFixedSize(400, 40)
        input_layout.addWidget(self.username_input)

        # Fixed spacing between username and token inputs
        input_layout.addSpacing(10)

        # Token input
        self.token_input = QLineEdit()
        self.token_input.setPlaceholderText("Enter your GitHub token")
        self.token_input.setEchoMode(QLineEdit.Password)
        self.token_input.setFixedSize(400, 40)
        input_layout.addWidget(self.token_input)

        # Add the input container to the center layout
        center_layout.addWidget(input_container, 0, Qt.AlignCenter)

        # Login button directly under the inputs, with reduced spacing
        login_button = QPushButton('Login')
        login_button.setFixedSize(400, 40)
        login_button.clicked.connect(self.handle_login)
        center_layout.addWidget(login_button, 0, Qt.AlignCenter)

        # Main layout of the window
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Add the center widget to the main layout to ensure everything is centered
        main_layout.addWidget(center_widget, 0, Qt.AlignCenter)

        self.centerWindow()

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

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

