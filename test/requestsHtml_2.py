from requests_html import HTMLSession
#动态页面获取

def wei_bo():
    session = HTMLSession()  # 创建一个会话
    url = 'https://weibo.cn/pub/'  # 请求的网址
    # 浏览器请求头
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Connection':'close'
    }
    r = session.get(url=url,headers=headers)     # get请求
    r.html.render()  # 重点关注
    first_one_name = r.html.xpath('/html/body/table[1]/tbody/tr/td[2]/a[1]/text()')[0]
    print('第一个明星的名字:', first_one_name)
    first_one_fans = r.html.xpath('/html/body/table[1]/tbody/tr/td[2]/text()')[0]
    print('第一个明星的粉丝数:', first_one_fans)
    second_one_name = r.html.xpath('/html/body/table[2]/tbody/tr/td[2]/a[1]/text()')[0]
    print('第二个明星的名字:', second_one_name)
    second_one_fans = r.html.xpath('/html/body/table[2]/tbody/tr/td[2]/text()')[0]
    print('第二个明星的粉丝数:', second_one_fans)

wei_bo()

