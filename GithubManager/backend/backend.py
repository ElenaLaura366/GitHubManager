import requests

def fetch_repositories(username, token):
    response = requests.get('https://api.github.com/user/repos', auth=(username, token))
    if response.status_code == 200:
        return response.json()
    else:
        return None
