import requests,pyquery,os,csv,matplotlib
os.makedirs('logo',exist_ok=True)
url = 'https://www.shanghairanking.cn/rankings/bcur/2022'
heards = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'
}
res = requests.get(url=url,headers=heards)
res.encoding = res.apparent_encoding
res.status_code
html = res.text
doc = pyquery.PyQuery(html)
logo = doc("div[class='logo']").items()
a = 1
for i in logo:
    docc = pyquery.PyQuery(i)
    print(docc('img').attr('src'))
    urllogo = docc('img').attr('src')
    reslogo = requests.get(url=urllogo, headers=heards)
    reslogo.encoding = res.apparent_encoding
    reslogo.status_code
    logopng = reslogo.content
    with open(fr'logo/top{a}.png','wb') as f:
        f.write(logopng)
    a+=1
css = ['.ranking','.name-cn','table.rk-table tbody tr td:nth-child(3)','table.rk-table tbody tr td:nth-child(4)','table.rk-table tbody tr td:nth-child(5)','table.rk-table tbody tr td:nth-child(6)']
list0  = [排名,学校名称,省市,类型,总分,办学层次]=[[],[],[],[],[],[]]
def tianjia(name,csss):
    con = doc(csss).items()
    for i in con:
        name.append(i.text())
        #print(i.text())
j = 0
while j<len(css):
    tianjia(list0[j],css[j])
    j+=1
import numpy as np
new_array = np.array(list0)
new_array = new_array.T
# 表头
header = ['排名', '学校名称', '省市', '类型', '总分', '办学层次']
with open('2022中国大学排名Top30.csv', 'w', encoding='utf-8-sig', newline='') as file_obj:
    # 创建对象
    writer = csv.writer(file_obj)
    # 写表头
    writer.writerow(header)
    # 遍历，将每一行的数据写入csv
    for p in new_array:
        writer.writerow(p)
import matplotlib.pyplot as plt
import matplotlib

"""
font:设置中文
"""
matplotlib.rcParams['font.family'] = ['KaiTi']

#设置大小
plt.rcParams['figure.figsize']=[10,10]
#定义饼状图的标签，标签是列表
place = {}
for p in list0[2]:
    print(p)
    if p not in place:
        place[p]=1
    elif p in place:
        place[p]+=1
    else:
        continue
labels =list(place.keys())
#每个标签占多大，会自动按照百分比绘制
data = list(place.values())
# 绘制饼图
plt.pie(data,labels=labels,autopct='%.1f%%')
plt.title("各省学校数量分布情况")
plt.show()
