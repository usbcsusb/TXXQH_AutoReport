# -*- coding: utf-8 -*-
import os
import requests
import datetime
import so2022
requests.packages.urllib3.disable_warnings()


##Github Action 环境变量

user_account = os.environ['UA']  # 学号
user_password = os.environ['UP']  # 一般是身份证后六位
mqszd = os.environ['MQ']  # 目前所在地 填写 "沈阳市" 、 "辽宁省非沈阳市" 、"其他地区（非辽宁省）"
sfybh = os.environ['SF']  # 前一日填报到目前为止，目前所在地（第 1 题）是否存在变化？ 填写 “是” 、 “否”
jrcltw = os.environ['JW']  # 今日测量体温,如"36.5"
sjhm = os.environ['SJ']  # 请填写目前个人手机号码,如"159*****"
jrlxfs = os.environ['JS']  # 请填写家人联系方式,如"#159******"
zddw1 = os.environ['ZA']  # 目前所在地第一行,如"中国,辽宁省,沈阳市"
zddw2 = os.environ['ZB']  # 目前所在地第二行,如"**大学"
# 微信推送 key 在 https://sct.ftqq.com/login 中使用微信扫码获取，信息会推送到你扫码的微信号上。
SendKey = os.environ['SK']


# 以下代码就不要乱动了
# 暂时先写这些变量了 ，临时够用 ，别的选项如果需要修改，正常来讲应该停止使用脚本
# 地区变动,体温不正常，接触其他人员等情况要 立刻 马上 跟导员汇报的！！！！！
# 调用一言接口实现 每日一言
def get_msg():
    url = "https://v1.hitokoto.cn/"
    r = requests.get(url)
    content = r.json()['hitokoto']
    return content


# 微信推送打卡成功
def server_turbo(state):
    # state ==1 打卡成功 state == 0 打卡失败
    stateHanzi = "打卡成功"

    if state == 1:
        stateHanzi = "打卡成功!"
    else:
        stateHanzi = "打卡失败!"

    urltemp="https://sctapi.ftqq.com/"+SendKey+".send"
    url =urltemp
    # url = "https://sctapi.ftqq.com/SCT131816TkxW9qOYXKbIJQiKu4nUdOFZt.send"
    note = get_msg()
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\nGA 打卡成功! " + note + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"desp\"\r\n\r\nGitHubAction 打卡成功 ! \r\n\r\n 每日一言 ：" + note +"\r\n\r\n您的打卡账号为： "+ user_account+"\r\n\r\n请确认上述为您的账号\r\n\r\n本程序仅供学习交流使用，打卡所有关键内容（如体温以及身份信息，目前所在地，接触情况等）均为用户自行填写，与作者无关，作者不负任何责任。如有身体不适，体温异常等请立即上报辅导员。" +"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    payload_error = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n打卡失败!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"desp\"\r\n\r\n赶快登陆 https://yqtb.sut.edu.cn/login/base#home 手动打卡吧\r\n\r\n 每日一言：" + note + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache"
    }
    so2022.sendmailjiami(user_account, user_password, mqszd, sfybh, jrcltw, sjhm, jrlxfs, zddw1, zddw2, SendKey,stateHanzi)
    if state == 1:
        response = requests.request("POST", url, data=payload.encode("utf-8"), headers=headers)
    else:
        response = requests.request("POST", url, data=payload_error.encode("utf-8"), headers=headers)
    # print(response.text)
    return response.json()['code']

# 在线获取时间并+1
def timeplus():
    # 使用苏宁时间api
    url_time = "http://quan.suning.com/getSysTime.do"
    payload_time = ""
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
    }
    suning = requests.request("POST", url_time, data=payload_time, headers=headers, verify=False)
    suningtime_str = str(suning.text)
    time_plus_pre = suningtime_str.split('"')
    # print(time_plus_pre)
    time_plus = time_plus_pre[3]
    # print(time_plus)

    try:
        # 创建临时变量time_type
        time_type = datetime.datetime.strptime(time_plus, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        print("error")
    # print(type(time_type))
    # print(time_type)
    time_type = time_type + datetime.timedelta(days=1)
    time_plus = str(time_type)
    # print(time_type)
    time_plus = time_plus.split(' ')
    time_plus = time_plus[0]
    # print(time_plus)
    return time_plus
    # return "2022-03-24"




# 打卡成功状态


# 打卡程序
def request_dk():
    # 打卡信息
    date_time = timeplus()

    # 头部信息
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36",
        'cache-control': "no-cache"
    }
    login_url = "https://yqtb.sut.edu.cn/login"  # 登录url
    # 登录信息(账号密码)
    payload_login = "{\"user_account\":\"" + user_account + "\",\"user_password\":\"" + user_password + "\"}"

    # ------------------------------------------------------------------------
    # 登录操作
    login_page = requests.request("POST", login_url, data=payload_login, headers=headers, verify=False)
    if login_page.status_code == 200:
        print('登录成功')
    # 记录cookie
    # print(login_page.cookies)
    cookies_login = str(login_page.cookies)
    JSESSIONID = cookies_login.split(' ')
    # print(JSESSIONID[1])
    # print(JSESSIONID[5])
    cookie_value = JSESSIONID[1] + '; ' + JSESSIONID[5]
    print(cookie_value)

    # 登录成功，开始打卡(提交表单)
    # 将获得的cookie放入headers中
    headers_cookie = {
        'Content-Type': "application/json",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36",
        'cache-control': "no-cache",
        'Cookie': cookie_value
    }
    dk_url = "https://yqtb.sut.edu.cn/home#home"
    dk_page = requests.request("GET", dk_url, headers=headers_cookie, verify=False)
    # 测试进入打卡选项页面
    # print(dk_page.text)
    # 提交打卡表单
    url_dk_punch = "https://yqtb.sut.edu.cn/punchForm"  # 提交url

    # 确认无误再解除下方代码注释
    payload_punch = "{\n    \"punch_form\": \"{\\\"mqszd\\\":\\\"" + mqszd + "\\\",\\\"sfybh\\\":\\\"" + sfybh + "\\\",\\\"mqstzk\\\":\\\"良好\\\",\\\"jcryqk\\\":\\\"未接触下述五类人员\\\",\\\"glqk\\\":\\\"自行做好防护\\\",\\\"jrcltw\\\":\\\"" + jrcltw + "\\\",\\\"sjhm\\\":\\\"" + sjhm + "\\\",\\\"jrlxfs\\\":\\\"" + jrlxfs + "\\\",\\\"xcsj\\\":\\\"\\\",\\\"gldd\\\":\\\"\\\",\\\"zddw\\\":\\\"" + zddw1 + "<@>" + zddw2 + "\\\"}\",\n    \"date\": \"" + date_time + "\"\n}"
    print(payload_punch)



    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36",
        'Cookie': cookie_value,
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "8b5f7737-df4d-458f-bfed-c91bf3afe654"
    }


    try:
        punch_response = requests.request("POST", url_dk_punch, data=payload_punch.encode("utf-8"), headers=headers,
                                          verify=False)
        content = punch_response.json()['code']
        #print(content)
        if content == 200:
            server_turbo(1)
            print("打卡成功")
    except:
        print
        server_turbo(0)
        "Error: 打卡失败"



if __name__ == "__main__":
    request_dk()
    print("程序结束")
