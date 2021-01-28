import jqdatasdk
from jqdatasdk import *
import pandas as pd
import csv
import datetime
import DateTransfer
auth('13926248003','Lxy123456') #账号是申请时所填写的手机号；密码为聚宽官网登录密码，新申请用户默认为手机号后6位
print(get_query_count())


mycsv = pd.read_csv('.\基金持仓数据研究\基金持仓\\2014-12-31.csv', encoding="gb2312")
#print(df[['股票代码']])
mycsv['过去一季收益率'] = ''
mycsv['相对沪深300指数的收益率1'] = ''
mycsv['未来一个月'] = ''
mycsv['相对沪深300指数的收益率2'] = ''
mycsv['两到三月'] = ''
mycsv['相对沪深300指数的收益率3'] = ''

# 这样写数据会少？？？
# code = normalize_code(mycsv['股票代码'].tolist())
# print(get_price(code,start_date='2019-1-1', end_date='2019-3-31', frequency='90d', fields=['open', 'close']))

t = 0
for i in mycsv['股票代码']:
    t += 1
    print(i)
    code = normalize_code(i)
    date = '2014-12-31'
    df = pd.DataFrame(get_price(code, start_date=DateTransfer.last3monthstart(date), end_date=date, frequency='90d',
                                fields=['open', 'close']))
    print(df)
    print(df['close'][0]-df['open'][0])
    if t == 10:
        break






#print(get_price(mycsv['股票代码'])['open'][:2])




# print(df['close'][0]-df['open'][0])
#





#df.to_csv('test111.csv',encoding= "gb2312",index=False)

