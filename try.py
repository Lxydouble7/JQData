import jqdatasdk
from jqdatasdk import *
import pandas as pd
import csv
import datetime
import DateTransfer
auth('13926248003','Lxy123456') #账号是申请时所填写的手机号；密码为聚宽官网登录密码，新申请用户默认为手机号后6位
print(get_query_count())

code = normalize_code('300211')
print(get_price(code,start_date='2020-9-30',end_date='2020-10-31',frequency='30d'))