import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
time_set = ["2020-12-31","2020-09-30","2020-06-30","2020-03-31","2019-12-31","2019-09-30","2019-06-30"
,"2019-03-31","2018-12-31","2018-09-30","2018-06-30","2018-03-31","2017-12-31","2017-09-30","2017-06-30"
,"2017-03-31","2016-12-31","2016-09-30","2016-06-30","2016-03-31","2015-12-31","2015-09-30","2015-06-30"
,"2015-03-31","2014-12-31"]

file = open('等权组合减持随机20.csv', 'w', newline='', encoding='gbk')

csvwriter = csv.writer(file)
csvwriter.writerow(["时间","过去一季平均收益率","相对沪深300指数的收益率1","未来一个月平均收益率","相对沪深300指数的收益率2",
                    "两到三月平均收益率","相对沪深300指数的收益率3","过去一季收益率方差","相对沪深300指数的收益率方差1","未来一月收益率方差",
                    "相对沪深300指数的收益率方差2","两到三月收益率方差","相对沪深300指数的收益率方差3"])
for date in time_set:
    mycsv = pd.read_csv('.\转换后\\' + date + '.csv', encoding="gb18030")

    # 选出所有增持的
    increase = mycsv.loc[mycsv['持股变化'] == '减持']
    increase = increase.sort_values('持股变动比例%', ascending=False)

    col1 = []
    col2 = []
    col3 = []
    col4 = []
    col5 = []
    col6 = []

    count = 0
    while count < len(increase) * 10:
        # 随机抽样：DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)[source]
        increase_sample = increase.sample(n=20, replace=False, random_state=None, axis=0)
        #increase_sample = increase.head(20)
        col1.append(increase_sample['过去一季收益率'].sum()/20)
        col2.append(increase_sample['相对沪深300指数的收益率1'].sum()/20)
        col3.append(increase_sample['未来一个月'].sum()/20)
        col4.append(increase_sample['相对沪深300指数的收益率2'].sum()/20)
        col5.append(increase_sample['两到三月'].sum()/20)
        col6.append(increase_sample['相对沪深300指数的收益率3'].sum()/20)
        count += 1

    row = [date,np.average(col1),np.average(col2),np.average(col3),
           np.average(col4),np.average(col5),np.average(col6),
           np.var(col1), np.var(col2), np.var(col3), np.var(col4),
           np.var(col5), np.var(col6)]
    csvwriter.writerow(row)
file.close()



