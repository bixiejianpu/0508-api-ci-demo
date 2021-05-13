from flask import Flask
from flask import request
from redis import Redis
import json

app = Flask(__name__)

redis_client = Redis()


@app.route('/set_username')
def set_username():
    username = request.args.get("username")
    password = request.args.get("password")
    redis_client.set(username, json.dumps({'username': username, 'password': password}))
    return json.dumps({"code": 200, "data": None, "msg": "请求成功"})


@app.route('/get_username')
def get_username():
    username = request.args.get("username")
    response = {"code": 200, "msg": '请求成功', "data": json.loads(str(redis_client.get(username), encoding='utf8'))}
    print(response)
    return json.dumps(response)


if __name__ == '__main__':
    app.run()
