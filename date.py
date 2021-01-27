from datetime import datetime
from dateutil.relativedelta import relativedelta

def last3month(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    date = date - relativedelta(months=3) + relativedelta(days=1)
    return date

def nextmonth(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    date = date + relativedelta(months=1) 
    return date

print(last3month('2014-3-31'))
print(nextmonth('2014-3-31'))