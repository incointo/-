import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
#票房单位亿元
movies = {
    "上汽":68.8,
    "长安":58.5,
    "吉利":53.0,
    "长城":41.8,
    "奇瑞":31.3,
    "比亚迪":19.5,
    "东风":19.0,
    "广汽":16.5,
    "一汽":15.1,
    "江淮":6.3,
    "华晨":5.4,
    "北汽":3.8,
    "理想":2.2,
    "合众新能源":1.6,
    "隼庆小鹏":1.5,
}
# 中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 13
# 设置图大小
plt.figure(figsize=(15,8))

x = list(movies.keys()) # 获取x轴数据(字典的键)
y = list(movies.values()) # 获取y轴数据(字典的值)

plt.barh(x, y, height=0.8, left=None,  align='center')


# 绘制标题
plt.title("2021年1-5月中国乘用车销量Top15（单位：万辆）",size=26)


plt.show()

