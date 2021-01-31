import jqdatasdk
from jqdatasdk import *
import pandas as pd
import csv
import datetime
import DateTransfer
auth('13926248003','Lxy123456') #账号是申请时所填写的手机号；密码为聚宽官网登录密码，新申请用户默认为手机号后6位
print(get_query_count())





# time_set = ["2020-12-31","2020-09-30","2020-06-30","2020-03-31","2019-12-31","2019-09-30","2019-06-30"
# ,"2019-03-31","2018-12-31","2018-09-30","2018-06-30","2018-03-31","2017-12-31","2017-09-30","2017-06-30"
# ,"2017-03-31","2016-12-31","2016-09-30","2016-06-30","2016-03-31","2015-12-31","2015-09-30","2015-06-30"
# ,"2015-03-31","2014-12-31"]

# time_set = ["2016-03-31","2015-12-31","2015-09-30","2015-06-30"
# ,"2015-03-31","2014-12-31"]

#time_set = ["2017-03-31","2016-12-31","2016-09-30","2016-06-30"]

#time_set = ["2018-09-30","2018-06-30","2018-03-31","2017-12-31","2017-09-30","2017-06-30"]


time_set = ["2020-12-31","2020-09-30","2020-06-30","2020-03-31","2019-12-31"]


for time_item in time_set:
    mycsv = pd.read_csv('.\基金持仓数据研究\基金持仓\\'+ time_item + '.csv', encoding="gb18030")
    # mycsv = pd.read_csv('.\基金持仓数据研究\基金持仓\\2014-12-31.csv', encoding="gb2312")
    # print(df[['股票代码']])
    mycsv['过去一季收益率'] = ''
    mycsv['相对沪深300指数的收益率1'] = ''
    mycsv['未来一个月'] = ''
    mycsv['相对沪深300指数的收益率2'] = ''
    mycsv['两到三月'] = ''
    mycsv['相对沪深300指数的收益率3'] = ''

    # 这样写数据会少？？？
    # code = normalize_code(mycsv['股票代码'].tolist())
    # print(get_price(code,start_date='2019-1-1', end_date='2019-3-31', frequency='90d', fields=['open', 'close']))

    date = time_item
    HS300LastSeason = get_price('000300.XSHG', start_date=DateTransfer.last3monthstart(date), end_date=date,
                                frequency='90d', fields=['open', 'close'])
    rate1 = (HS300LastSeason['close'][0] - HS300LastSeason['open'][0]) / HS300LastSeason['open'][0]

    HS300NextMonth = get_price('000300.XSHG', start_date=DateTransfer.nextmonthstart(date),
                               end_date=DateTransfer.nextmonthend(date),
                               frequency='30d', fields=['open', 'close'])
    rate2 = (HS300NextMonth['close'][0] - HS300NextMonth['open'][0]) / HS300NextMonth['open'][0]

    HS300Next2Month = get_price('000300.XSHG', start_date=DateTransfer.next2monthstart(date),
                                end_date=DateTransfer.next2monthend(date),
                                frequency='60d', fields=['open', 'close'])
    rate3 = (HS300Next2Month['close'][0] - HS300Next2Month['open'][0]) / HS300Next2Month['open'][0]


    t = 0
    for i in mycsv['股票代码']:
        code = normalize_code(i)

        df = pd.DataFrame(get_price(code, start_date=DateTransfer.last3monthstart(date), end_date=date, frequency='90d',
                                    fields=['open', 'close']))
        # print(df)
        # print((df['close'][0]-df['open'][0])/df['open'][0])
        mycsv.loc[t, '过去一季收益率'] = (df['close'][0] - df['open'][0]) / df['open'][0]
        mycsv.loc[t, '相对沪深300指数的收益率1'] = (df['close'][0] - df['open'][0]) / df['open'][0] - rate1

        df = pd.DataFrame(
            get_price(code, start_date=DateTransfer.nextmonthstart(date), end_date=DateTransfer.nextmonthend(date),
                      frequency='30d', fields=['open', 'close']))
        mycsv.loc[t, '未来一个月'] = (df['close'][0] - df['open'][0]) / df['open'][0]
        mycsv.loc[t, '相对沪深300指数的收益率2'] = (df['close'][0] - df['open'][0]) / df['open'][0] - rate2

        df = pd.DataFrame(
            get_price(code, start_date=DateTransfer.next2monthstart(date), end_date=DateTransfer.next2monthend(date),
                      frequency='60d', fields=['open', 'close']))
        # print(df)
        mycsv.loc[t, '两到三月'] = (df['close'][0] - df['open'][0]) / df['open'][0]
        mycsv.loc[t, '相对沪深300指数的收益率3'] = (df['close'][0] - df['open'][0]) / df['open'][0] - rate3

        t += 1
        # if t == 10:
        #     break

    mycsv.to_csv('.\转换后\\' + time_item + '.csv', encoding="gb18030", index=False)
    print(time_item+"完成")
