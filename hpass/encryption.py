import random
import hmac
import base64
from hashlib import sha256


def random_password(length):
    base_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'h', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4',
                 '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*']
    password = ''
    for j in range(length):
        m = random.randint(0, len(base_char) - 1)
        password = password + base_char[m]
    return password


def rc4_init_s_box(key):
    print("我这里没管秘钥小于256的情况，小于256不断重复填充即可")
    s_box = list(range(256))
    print("原来的 s 盒：%s" % s_box)
    j = 0
    for i in range(256):
        j = (j + s_box[i] + ord(key[i % len(key)])) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
    print("混乱后的 s 盒：%s" % s_box)
    return s_box


def rc4_res_program(s_box, message):
    res = []
    i = j = 0
    for s in message:
        i = (i + 1) % 256
        j = (j + s_box[i]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
        t = (s_box[i] + s_box[j]) % 256
        k = s_box[t]
        res.append(chr(ord(s) ^ k))
    return res


def encryption_rc4(key, message):
    print("RC4加密主函数")
    s_box = rc4_init_s_box(key)
    print("调用加密程序成功。")
    res = rc4_res_program(s_box, message)
    print("res用于加密字符串，加密后是：%res" % res)
    cipher = "".join(res)
    print("加密后的字符串是：%s" % cipher)
    print("加密后的输出(经过编码):")
    cipher_text = str(base64.b64encode(cipher.encode('utf-8')), 'utf-8')
    print(cipher_text)
    return cipher_text


def decrypt_rc4(key, message):
    print("RC4解密主函数调用成功")
    s_box = rc4_init_s_box(key)
    print("调用解密程序成功。")
    plain = base64.b64decode(message.encode('utf-8'))
    plain = bytes.decode(plain)
    res = rc4_res_program(s_box, plain)
    print("res用于解密字符串，解密后是：%res" % res)
    cipher = "".join(res)
    print("解密后的字符串是：%s" % cipher)
    print("解密后的输出(没经过任何编码):")
    print(cipher)
    return cipher


def hmac_sha256_digest(value, key='35a07615d258ae2e067879a472e050cc3716'):
    app_secret = key.encode('utf-8')
    data = value.encode('utf-8')
    signature = base64.b64encode(hmac.new(app_secret, data, digestmod=sha256).digest())
    return signature


if __name__ == '__main__':
    encryption_rc4('123456', '我是要加密的内容')
    decrypt_rc4('123456', '5oiR5puX6Ke/5YuH5a+i55q35YaQ5ayl')
