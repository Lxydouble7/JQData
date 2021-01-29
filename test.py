import jqdatasdk
from jqdatasdk import *
import pandas as pd
import csv
import datetime
import DateTransfer

auth('13926248003','Lxy123456')
code = normalize_code('300750')
date = '2020-12-31'
print(get_price(code, start_date=DateTransfer.last3monthstart(date), end_date=date, frequency='90d',
                                    fields=['open', 'close']))
print(get_price(code, start_date=DateTransfer.nextmonthstart(date), end_date=DateTransfer.nextmonthend(date), frequency='30d',
                                    fields=['open', 'close']))
print(get_price(code, start_date=DateTransfer.next2monthstart(date), end_date=DateTransfer.next2monthend(date), frequency='60d',
                                    fields=['open', 'close']))