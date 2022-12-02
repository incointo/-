import requests
from pyquery import PyQuery as pq

heards = {
    'User-Agent':
}
url = 'https://www.baidu.com/'
res = requests.get(url=url,headers=heards)
res.encoding = res.apparent_encoding
html = res.text #获取网站源码
i = 1#计数用

doc = pq(html)
news = doc('div>div>div>div>div>div>ul>li').items()#找到热搜块
for inf in news:
    name = inf.find('span.title-content-title').text()#提取名字
    wangzhi = inf.find('a').attr.href#提取网址
    with open('file.txt','a',encoding=res.apparent_encoding) as f:
        f.write(str(i)+'.')
        f.write(name)
        f.write(wangzhi)
        f.write('\n')#写入
    i+=1
