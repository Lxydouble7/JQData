from datetime import datetime
from dateutil.relativedelta import relativedelta

def last3monthstart(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    date = date - relativedelta(months=3) + relativedelta(days=1)
    return date

def nextmonthstart(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    date = date + relativedelta(days=1)
    return date

def nextmonthend(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    date = date + relativedelta(months=1) 
    return date

def next2monthstart(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    date = date + relativedelta(months=1) + relativedelta(days=1)
    return date

def next2monthend(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    date = date + relativedelta(months=3)
    return date

# print(last3monthstart('2014-3-31'))
# print(nextmonthstart('2014-3-31'))
# print(nextmonthend('2014-3-31'))
# print(next2monthstart('2014-3-31'))
# print(next2monthend('2014-3-31'))