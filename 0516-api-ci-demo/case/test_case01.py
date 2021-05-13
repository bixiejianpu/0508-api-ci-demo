import requests


class TestCase01:

    def test01(self):
        params = {"username": "zhangsan", "password": "123"}
        r = requests.get("http://localhost:5000/set_username", params=params).json()
        assert r["code"] == 200

        params1 = {"username": "zhangsan"}
        r = requests.get("http://localhost:5000/get_username", params=params1).json()
        assert r["code"] == 200
        assert r["data"] == params



