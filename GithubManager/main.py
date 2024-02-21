from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sys
import requests
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GitHubManager")
        self.setGeometry(100, 100, 1000, 600)
        self.initUI()

    def initUI(self):
        self.loginButton = QPushButton('Login with GitHub', self)
        self.loginButton.move(200, 250)
        self.loginButton.clicked.connect(self.initiateDeviceFlow)

        self.infoLabel = QLabel(self)
        self.infoLabel.move(200, 300)
        self.infoLabel.resize(600, 40)

    def initiateDeviceFlow(self):
        client_id = 'f51b3f373bffc7f74d8f'
        device_code_url = 'https://github.com/login/device/code'
        scope = 'read:user user:email'

        # Solicită codul de dispozitiv
        payload = {
            'client_id': client_id,
            'scope': scope
        }
        response = requests.post(device_code_url, data=payload)

        if response.status_code != requests.codes.ok:
            print(f"Error: {response.status_code}")
            print(response.text)

        if response.status_code == requests.codes.ok:
            try:
                data = response.json()
                device_code = data['device_code']
                user_code = data['user_code']
                verification_uri = data['verification_uri']
                interval = data['interval']

                # Afișează codul pentru utilizator
                self.infoLabel.setText(f"Please go to {verification_uri} and enter the code: {user_code}")

                # Verifică autorizarea
                self.checkAuthorization(client_id, device_code, interval)
            except ValueError:
                # Handle the exception here if response is not in json format
                self.infoLabel.setText(f"Failed to parse JSON response: {response.text}")
        else:
            # Handle the response error (e.g., error response from GitHub)
            self.infoLabel.setText(f"Failed to initiate device flow: {response.status_code} - {response.text}")

    def checkAuthorization(self, client_id, device_code, token_url, interval):
        payload = {
            'client_id': client_id,
            'device_code': device_code,
            'grant_type': 'urn:ietf:params:oauth:grant-type:device_code'
        }
        while True:
            time.sleep(interval)  # Așteaptă intervalul indicat înainte de a reîncerca
            response = requests.post(token_url, data=payload)
            if response.ok:
                access_token = response.json().get('access_token')
                self.infoLabel.setText("Authentication successful.")
                break
            elif response.status_code == 400:
                self.infoLabel.setText("Waiting for user authorization...")
            else:
                self.infoLabel.setText("Authorization failed.")
                break


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
