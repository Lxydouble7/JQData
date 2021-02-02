import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置
time_set = ["2020-09-30","2020-06-30","2020-03-31","2019-12-31","2019-09-30","2019-06-30"
,"2019-03-31","2018-12-31","2018-09-30","2018-06-30","2018-03-31","2017-12-31","2017-09-30","2017-06-30"
,"2017-03-31","2016-12-31","2016-09-30","2016-06-30","2016-03-31","2015-12-31","2015-09-30","2015-06-30"
,"2015-03-31","2014-12-31"]

name_set = ['等权组合增持max20.csv','等权组合增持r20m40.csv','等权组合增持家数max20.csv','等权组合增持家数r20m40.csv']
plt.figure(figsize=(10,10))

for i in name_set:
    if i == '等权组合增持max20.csv':
        plt.subplot(221)
    if i == '等权组合增持r20m40.csv':
        plt.subplot(222)
    if i == '等权组合增持家数max20.csv':
        plt.subplot(223)
    if i == '等权组合增持家数r20m40.csv':
        plt.subplot(224)
    plt.axis([1,25,-0.15,0.3])
    data = pd.read_csv(i, encoding="gb18030")
    data = data.dropna(axis=0, how='any')
    data = data.drop(0, axis=0, inplace=False)
    # data = data[['相对沪深300指数的收益率1', '相对沪深300指数的收益率2', '相对沪深300指数的收益率3']]
    # print(data)
    # time_set.reverse()
    time_set = list(range(1, 25))
    col1 = list(data['相对沪深300指数的收益率1'])
    col2 = list(data['相对沪深300指数的收益率2'])
    col3 = list(data['相对沪深300指数的收益率3'])
    #print(col1)
    #print(col2)
    #print(col3)
    plt.yticks([-0.15,-0.1,-0.05,0,0.05,0.1,0.2,0.3])
    # plt.scatter(time_set, col1, label="过去一个月相对沪深300收益率", linestyle=":")
    plt.scatter(time_set, col2, label="后一个月相对沪深300收益率", linestyle=":")
    plt.scatter(time_set, col3, label="后两到三月相对沪深300收益率", linestyle=":")
    plt.legend()
    plt.title("基金增持股票中持有家数最大的40只中随机抽样40只")
    plt.xlabel("日期")
    plt.ylabel("相对沪深收益率")

    print(np.average(col1))
    print(np.average(col2))
    print(np.average(col3))
    print(np.var(col1))
    print(np.var(col2))
    print(np.var(col3))
plt.show()



