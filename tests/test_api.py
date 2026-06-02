import httpx
import pytest
import json
import datetime
from fastapi.encoders import jsonable_encoder
from faker import Faker

fake = Faker()

@pytest.mark.parametrize('name',
                         ['Jambo', fake.first_name(), '5555'])
def test_hello(name: str):
    data = {"name": name}
    response = httpx.post('http://127.0.0.1:8000/hi', json=data)
    res_json = response.json()

    assert res_json == f"Hello, {name}", f"\nResponse: {res_json}\nText: {name}"

@pytest.fixture()
def data():
    return datetime.datetime.now()

def test_json_dump(data):
    with pytest.raises(Exception):
        _ = json.dumps(data)

def test_encoder(data):
    out = jsonable_encoder(data)
    assert out
    json_out = json.dumps(out)
    assert json_out
    print(f"\nout: {out}\njson: {json_out}")


