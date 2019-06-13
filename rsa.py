# -*- encoding:utf-8 -*-
import base64
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA

# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)
# master的秘钥对的生成
private_pem = rsa.exportKey()
print(private_pem)
public_pem = rsa.publickey().exportKey()
print(public_pem)
#生产私钥私钥并放到文件里
with open('master-private.pem', 'wb') as f:
    f.write(private_pem)
with open('master-public.pem', 'wb') as f:
    f.write(public_pem)

#用公钥加密
#被加密的数据
import time
message = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())).encode()
#打开公钥文件
with open('master-public.pem','rb') as f:
    key = f.read()
rsakey = RSA.importKey(key)
cipher = Cipher_pkcs1_v1_5.new(rsakey)
#加密时使用base64加密
cipher_text = base64.b64encode(cipher.encrypt(message))
# cipher_text = cipher.encrypt(message)
print(cipher_text)


#用私钥解密
#打开秘钥文件
with open('master-private.pem','rb') as f:
    key = f.read()
rsakey = RSA.importKey(key)
cipher = Cipher_pkcs1_v1_5.new(rsakey)
# text = cipher.decrypt(cipher_text, random_generator)
#使用base64解密，(在前端js加密时自动是base64加密)
text = cipher.decrypt(base64.b64decode(cipher_text), random_generator).decode()
print(text)