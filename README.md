
# [打卡自动化——基于Python requests](https://github.com/usbcsusb/SUT-AutoReport-python)
## 推送bug已经修复 需要重新fork
![GitHub last commit](https://img.shields.io/github/last-commit/usbcsusb/SUT_AutoReport)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/usbcsusb/SUT_AutoReport)  

友情链接 https://github.com/BioniCosmos/auto-report

## 食用方法

本分支为GitHub Action 版本 ，可以使用GitHub Action 托管打卡

打卡时间：每天的 13:30 15:30 .有能力的建议自己修改一下时间,避免拥挤导致打卡失败.
打卡成功或者打卡失败在微信上均有推送,失败请手动打卡.


### 1、fork 此仓库
直接fork此仓库到自己的GitHub；

### 2、设置账号信息
Settings→Secrets→New repository secret；  
<img src="images/img 4 .jpg" width="100%">
<img src="images/img 5 .jpg" width="100%">
设置以下 Secret:
    
    UA | "*********"  # 学号
    UP | "*******"  # 身份证后六位
    MQ | "沈阳市"  # 目前所在地 填写 "沈阳市" 、 "辽宁省非沈阳市" 、"其他地区（非辽宁省）"
    SF | "否"  # 前一日填报到目前为止，目前所在地（第 1 题）是否存在变化？ 填写 “是” 、 “否”
    JW | "36.5"  # 今日测量体温
    SJ | "159*****"  # 请填写目前个人手机号码
    JS | "159******"  # 请填写家人联系方式
    ZA | "中国,辽宁省,沈阳市"  # 目前所在地第一行
    ZB | "****大学"  # 目前所在地第二行
    # 微信推送 key 在 https://sct.ftqq.com/login 中使用微信扫码获取，信息会推送到你扫码的微信号上。
    SK } "****************************************"

最后是这样的
<img src="images/img 6 .jpg" width="100%">
微信推送 key 在 https://sct.ftqq.com/login 中使用微信扫码获取，信息会推送到你扫码的微信号上。
<div align="center">
	<img src="images/img 0.png" width="100%">
</div>
    扫码之后点继续
    <img src="images/img 1 .png" width="100%">
    点击复制
    <img src="images/img 2 .png" width="100%">

最后将复制的SendKey填入GitHub Action的对应Secrets中即可
    

### 3、启用Acitons
启用GitHub Actions，并修改任意文件Commit一次即可运行。 (如果有"I understand my workflows ,go ahead and enable them",请点击它) 
可在Actions→Update...→build→SignIn查看运行结果。

## TODO (已经鸽了)
1.添加根据上次打卡内容，获取打卡信息功能，这样只需要输入账号密码即可

2.基于Flask开发一个可以添加账号的 web界面 ，提升交互性。

## 许可证声明：
本项目采用MIT许可证
* 你可以使用，复制和修改软件
* 你可以免费使用软件或出售
* 唯一的限制是，它是必须附有MIT授权协议


# 郑重声明：
**本项目初衷为学习python基础！**

**本项目使用者在使用前应了解本项目所带来的风险！**

**本人不对此项目所造成的一切后果担责！**
