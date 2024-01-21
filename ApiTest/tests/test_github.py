import requests
import json
import os

token = "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"
headers = {'Authorization': f'token {token}'}


def test_github_user():
    end_point = 'https://api.github.com/user'
    user = requests.get(url=end_point, headers=headers)
    user_data = json.loads(user.content)
    # assert user_data.get('login') == 'JanaKuchugurna'
    pass


def test_delete_repository():
    end_point = 'https://api.github.com/repos/JanaKuchugurna/api_test_repository_1'
    response = requests.delete(url=end_point, headers=headers)
    pass


def test_update_repo():
    end_point = 'https://api.github.com/repos/JanaKuchugurna/api_test_repository_3'
    repo_data = {'name': 'api_test_repository_three',
                 'description': 'trying_to_post_via_python',
                 'private': False}
    response = requests.patch(url=end_point, headers=headers, json=repo_data)
    pass

# print(os.name)
# print(os.environ)


# def test_create_repository():
#     end_point = 'https://api.github.com/user/repos'
#     repo_data = {'name': 'api_test_repository_5',
#                  'description': 'trying_to_post_via_python',
#                  'private': False}
#     response = requests.post(url=end_point, headers=headers, json=repo_data)
#     new_repo_name = response.json().get('html_url')
#     # assert new_repo_name.endswith(repo_data.get('name'))
#     requests.delete(url=new_repo_name, headers=headers)
#     pass
