import jqdatasdk
from jqdatasdk import *
import pandas as pd
import csv
import datetime
auth('13926248003','Lxy123456') #账号是申请时所填写的手机号；密码为聚宽官网登录密码，新申请用户默认为手机号后6位
print(get_query_count())


df = pd.read_csv('.\基金持仓数据研究\基金持仓\\2014-12-31.csv',encoding= "gb2312")
#print(df[['股票代码']])
df['过去一季收益率'] = ''
df['相对沪深300指数的收益率1'] =''
df['未来一个月'] = ''
df['相对沪深300指数的收益率2'] = ''
df['两到三月'] = ''
df['相对沪深300指数的收益率3'] = ''


t=0
for i in df['股票代码']:
    t+=1
    code = normalize_code(i)
    print(normalize_code(i))
    df = pd.DataFrame(get_price(code, start_date='2014-12-31', end_date='2015-03-31', frequency='90d',
                                fields=['open', 'close']))
    if t==10:
        break
#print(df)
df.to_csv('test111.csv',encoding= "gb2312",index=False)

# 沪XSHG 深XSHE
# normalize_code(['000001', 'SZ000001', '000001SZ', '000001.sz', '000001.XSHE'])
# print(df)



# df = pd.DataFrame(get_price('000300.XSHG',start_date='2014-12-31',end_date='2015-03-31',frequency='90d',fields=['open','close']))
# print(df)