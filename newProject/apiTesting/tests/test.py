import pytest
import requests
import json


@pytest.mark.api
def test_get_books():
    response = requests.get(url='https://demoqa.com/BookStore/v1/Books')
    content = json.loads(response.content)
    assert response.status_code == 200
    assert len(content.get('books')) == 8


@pytest.mark.api
def test_post_books():
    user = 'qalight1'
    password = 'P@ssw0rd'
    uri = 'https://demoqa.com'
    end_point = '/Account/v1/Authorized'
    user_data = {'userName': user, 'password': password}
    response = requests.post(url=uri + end_point, data=user_data)
    assert response.status_code == 200


@pytest.mark.api
def get_token():
    user = 'qalight1'
    password = 'P@ssw0rd'
    uri = 'https://demoqa.com'
    end_point = '/Account/v1/GenerateToken'
    url = uri + end_point
    response = requests.post(url=url, data={'userName': user, 'password': password})
    token = json.loads(response.content).get('token')
    return token


@pytest.mark.api
def test_authorize_with_token():
    token = get_token()
    headers = {'Authorization': f'Bearer {token}'}
    post_body = {
        "userId": "string",
        "collectionOfIsbns": [{"isbn": "string"}]}
    response = requests.post(url='https://demoqa.com/BookStore/v1/Books', data=post_body, headers=headers)
    pass
