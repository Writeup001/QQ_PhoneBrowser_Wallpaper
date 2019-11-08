# -*- coding=utf8 -*-

# 腾讯手机QQ浏览器每日特辑发布的第一张图片
# https://today.html5.qq.com/share?idList=2516073
# 小于这个 ID 的全部是 202 错误，即不存在
# 腾讯一般是下午4点多左右更新图片，这时候也可以进行爬取，但是个人不建议

import os
import time
import requests
from lxml import etree


url = "https://today.html5.qq.com/share?idList=%s"
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br'
}

# 开始 ID 的路径
f = open("./startID.txt")
line = f.readline()
f.close

num = 0
tomorrowID = 0
startID = int(line) + 1
# 上一天最后的 ID 的下一个作为今天开始的 ID
endID = startID + 100
# 向后读取 100 张进行测试，一般来说腾讯每天更新图片不会超过 10 张，而图片 ID 值间隔最大不会超过 100

for i in range(startID,endID):
    r = requests.get(url % i,headers=headers)
    # 出于人性化考虑可休眠一秒
    # time.sleep(1)
    if r.status_code == 200:
        # 解析
        html_xpath = etree.HTML(r.text)
        data = html_xpath.xpath('/html/body/div/div[2]/span/img/@src')
        # print(data[0])
        r = requests.get(url=data[0],headers=headers)
        # 出于人性化考虑可休眠一秒
        # time.sleep(1)
        num += 1        
        
        # 保存路径
        time_path = time.strftime('%Y_%m_%d',time.localtime(time.time()))
        root = "./" + time_path + "/"
        path = root + str(num) + '.png'

        # 创建时间目录
        if not os.path.exists(root):
            os.mkdir(root)

        # 写入文件
        with open(path,'wb') as f:
            f.write(r.content)
        f.close()
        # 最新一次正常获得图片的 ID 值作为第二天开始进行的 ID
        tomorrowID = i
        print("爬取成功，ID：",i,r.status_code)
            
    else:
    	print("爬取失败，ID：",i,r.status_code)
    
print("今天获得图片",num,"张")
# 重置下一次开始的 ID
with open("./startID.txt","w") as f:
        f.write(str(tomorrowID))