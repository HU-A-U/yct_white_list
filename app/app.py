# -*- coding:utf-8 -*-
from flask import Flask
from flask import request,jsonify
import base64
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA



app = Flask(__name__)

#建立redis连接池
import redis
redis_pool = redis.ConnectionPool(host='aliyun_redis',port=6379,decode_responses=True)
r = redis.Redis(connection_pool=redis_pool)

# @app.route('/', methods=['get'])
# def get_private_pem():
#     '''随机生成密钥对，返回公密钥'''
#
#     # 伪随机数生成器
#     random_generator = Random.new().read
#     rsa = RSA.generate(1024, random_generator)
#     # 私钥
#     private_pem = rsa.exportKey()
#     # 公钥
#     public_pem = rsa.publickey().exportKey()
#
#     # 将公钥对应的私钥存库,过期时间一小时
#     r.set(public_pem,private_pem,ex=3600)
#
#     # 返回公钥
#     return public_pem
#
# @app.route('/addr')
# def save_addr():
#     '''获取请求的公钥取出redis中的私钥
#         使用私钥进行解密，获取时间戳和token，
#         对比token，时间戳在范围内，放行
#     '''
#
#     ip_addr = request.access_route[0]
#     msg = {}
#     if ip_addr:
#         if r.set(ip_addr,'pass'):
#             msg = {'msg':'ok'}
#     return jsonify(**msg)

@app.route('/', methods=['get'])
def save_addr():
    ip_addr = request.access_route[0]
    msg = {}
    if ip_addr:
        if r.set(ip_addr,'pass'):
            msg = {'msg':'ok'}

    return jsonify(**msg)



if __name__ == '__main__':
    app.run()
