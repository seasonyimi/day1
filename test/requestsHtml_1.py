from requests_html import HTMLSession
#静态页面获取
def dou_ban():
    session = HTMLSession() #创建一个会话
    url = 'https://movie.douban.com/top250'  #请求的网址
    #浏览器请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Connection': 'keep-alive'
    }
    r = session.get(url=url,headers=headers)  #get请求

    # 因为提取的是html元素，所以文本文字需要在xpath后面加上/text()，返回值类型是列表，而且只有一个元素，所以是[0]
    name = r.html.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]/text()')[0]
    print('电影名字：',name)
    score = r.html.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]/text()')[0]
    print('评分:',score)
    number = r.html.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[4]/text()')[0]
    print('评价人数：',number)

dou_ban()

