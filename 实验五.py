from selenium import webdriver
from selenium.webdriver.edge.service import Service
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 创建 WebDriver 对象，指明使用chrome浏览器驱动
    wd = webdriver.Edge()

    # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
    wd.get(
        'https://weathernew.pae.baidu.com/weathernew/pc?query=%E6%B2%B3%E5%8C%97%E8%A1%A1%E6%B0%B4%E5%A4%A9%E6%B0%94&srcid=4982')
    resPagesource = wd.page_source
    mysoup = BeautifulSoup(resPagesource, 'html.parser')
    # print(mysoup.select('li[class = "future-weather-item"]'))
    neirong = mysoup.select('span[data-a-47fdbfce=""]')
    minweather = []
    maxweather = []
    a,b = 0,1
for inf in neirong:
    i = inf.text
    if a == 0:
        a+=1
        continue
    else:
        if b==1:
            minweather.append(eval(i))
            a+=1
            b+=1
            continue
        elif b == 2:
            a += 1
            b+=1
            continue
        else:
            qiwen = i.split('°')
            maxweather.append(eval(qiwen[0]))
            b= 1
            a += 1

            continue

print(f"最大值气温平均数{sum(maxweather)/40}'\n'最小值气温平均数{sum(minweather)/40}")

    #BeautifulSoup(i, 'html.parser')
    #print(i.attrs)
