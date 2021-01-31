import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置
time_set = ["2020-09-30","2020-06-30","2020-03-31","2019-12-31","2019-09-30","2019-06-30"
,"2019-03-31","2018-12-31","2018-09-30","2018-06-30","2018-03-31","2017-12-31","2017-09-30","2017-06-30"
,"2017-03-31","2016-12-31","2016-09-30","2016-06-30","2016-03-31","2015-12-31","2015-09-30","2015-06-30"
,"2015-03-31","2014-12-31"]

num11 = []
num12 = []
num13 = []
num21 = []
num22 = []
num23 = []
date = "2020-12-31"
data = pd.read_csv('.\转换后\\' + date + '.csv', encoding="gb18030")
data = data[['持有基金家数', '持股变动比例%', '相对沪深300指数的收益率1', '相对沪深300指数的收益率2', '相对沪深300指数的收益率3']]
num11.append(data.corr('spearman').loc['持有基金家数'].loc['相对沪深300指数的收益率1'])
num12.append(data.corr('spearman').loc['持有基金家数'].loc['相对沪深300指数的收益率2'])
num13.append(data.corr('spearman').loc['持有基金家数'].loc['相对沪深300指数的收益率3'])
num21.append(data.corr('spearman').loc['持股变动比例%'].loc['相对沪深300指数的收益率1'])
num22.append(data.corr('spearman').loc['持股变动比例%'].loc['相对沪深300指数的收益率2'])
num23.append(data.corr('spearman').loc['持股变动比例%'].loc['相对沪深300指数的收益率3'])
# 持有基金家数、持股变动和相对沪深123的相关系数


for i in time_set:
    date = i
    mycsv = pd.read_csv('.\转换后\\' + date + '.csv', encoding="gb18030")
    mycsv = mycsv[['持有基金家数', '持股变动比例%', '相对沪深300指数的收益率1', '相对沪深300指数的收益率2', '相对沪深300指数的收益率3']]
    data = pd.concat([data, mycsv], axis=0)
    mycsv = mycsv.corr('spearman')
    num11.append(mycsv.loc['持有基金家数'].loc['相对沪深300指数的收益率1'])
    num12.append(mycsv.loc['持有基金家数'].loc['相对沪深300指数的收益率2'])
    num13.append(mycsv.loc['持有基金家数'].loc['相对沪深300指数的收益率3'])
    num21.append(mycsv.loc['持股变动比例%'].loc['相对沪深300指数的收益率1'])
    num22.append(mycsv.loc['持股变动比例%'].loc['相对沪深300指数的收益率2'])
    num23.append(mycsv.loc['持股变动比例%'].loc['相对沪深300指数的收益率3'])
data = data.dropna(axis=0, how='any')
# pearson spearman kendall
data.corr('spearman').to_csv("correlation.csv",encoding="gb18030")
num11.reverse()
num12.reverse()
num13.reverse()
num21.reverse()
num22.reverse()
num23.reverse()
# time_set.reverse()
# time_set.append('2020-12-31')
time_set = list(range(1,26))
num11 = list(map(abs, num11))
num12 = list(map(abs, num12))
num13 = list(map(abs, num13))
num21 = list(map(abs, num21))
num22 = list(map(abs, num22))
num23 = list(map(abs, num23))
plt.figure()
plt.plot(time_set, num11, label="持有基金家数与过去一季相对沪深300指数的收益率", linestyle=":",)
plt.plot(time_set, num12,label="持有基金家数与后一个月相对沪深300指数的收益率", linestyle="--")
plt.plot(time_set, num13, label="持有基金家数与后两到三个月相对沪深300指数的收益率", linestyle="-.")
plt.plot(time_set, num21, label="持股变动比例%与过去一季相对沪深300指数的收益率", linestyle=":",)
plt.plot(time_set, num22,label="持股变动比例%与后一个月相对沪深300指数的收益率", linestyle="--")
plt.plot(time_set, num23, label="持股变动比例%与后两到三个月相对沪深300指数的收益率", linestyle="-.")
plt.legend()
plt.title("基金家数、持股变动和收益率相关系数")
plt.xlabel("日期")
plt.ylabel("相关系数")
plt.show()





