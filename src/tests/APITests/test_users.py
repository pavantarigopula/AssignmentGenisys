import requests
import pytest
import json

url = "https://crudcrud.com/api/eb112b0689bd4cfb962d39f89122cfba/users"
headers ={"Content-Type":"application/json"}

@pytest.mark.smoke
def test_create_user():
    payload = json.dumps({
    "name":"Test1",
    "email":"Test1@gmail.com",
    "age":23
    })
    response = requests.post(url=url,headers=headers,data=payload)
    assert response.status_code == 201
    result = response.json()
    assert result["_id"] is not None
    assert result["name"] == "Test1"
    assert result["email"] == "Test1@gmail.com"
    assert result["age"] == 23

@pytest.mark.smoke
def test_get_user():
    response = requests.get(url=url,headers=headers)
    assert response.status_code == 200
    result = response.json()
    if len(result) > 0:
        for data in result:
            assert data["_id"] is not None
            assert data["name"] is not None
            assert data["email"] is not None
            assert data["age"] is not None

@pytest.mark.smoke
def test_update_user():
    response = requests.get(url=url, headers=headers)
    result = response.json()
    id = result[0]["_id"]
    temp_url = url +'/'+id
    data =json.dumps({
    "name":"Test12",
    "email":"Test12@gmail.com",
    "age":32
    })
    response = requests.put(temp_url,headers=headers,data=data)
    assert response.status_code == 200


@pytest.mark.smoke
def test_delete_user():
    response = requests.get(url=url, headers=headers)
    result = response.json()
    id = result[0]["_id"]
    temp_url = url +'/'+id
    response = requests.delete(temp_url)
    assert response.status_code == 200

