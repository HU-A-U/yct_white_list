# -*- coding:utf-8 -*-
from flask import Flask
from flask import request,jsonify
app = Flask(__name__)

#建立redis连接池
import redis
redis_pool = redis.ConnectionPool(host='aliyun_redis',port=6379,decode_responses=True)
r = redis.Redis(connection_pool=redis_pool)

@app.route('/', methods=['get'])
def save_ip():
    ip_addr = request.access_route[0]
    msg = {}
    if r.set(ip_addr,'pa'):
        msg = {'msg':'ok'}
    return jsonify(**msg)

if __name__ == '__main__':
    app.run()
