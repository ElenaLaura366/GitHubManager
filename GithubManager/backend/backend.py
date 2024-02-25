import requests


def fetch_repositories(username, token):
    response = requests.get('https://api.github.com/user/repos', auth=(username, token))
    if response.status_code == 200:
        return response.json()
    else:
        return None


def create_repository(username, token, repo_name):
    url = 'https://api.github.com/user/repos'
    headers = {'Authorization': f'token {token}'}
    data = {'name': repo_name}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:  # 201 Created
        return response.json()  # Returns the created repository data
    else:
        return None


def delete_repository(username, token, repo_name):
    url = f'https://api.github.com/repos/{username}/{repo_name}'
    headers = {'Authorization': f'token {token}'}
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:  # 204 No Content
        return True  # Repository successfully deleted
    else:
        return False


