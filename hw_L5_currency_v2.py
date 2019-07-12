
#Запросить курсы любой валюты за последний год.
#Сохранить полученные данные в базу данных Mongo
#Написать функцию, которая принимает в качестве параметров две даты,
#ищет самую большую разницу между курсами валюты за указанный период
#и возвращает эти дни.
#Сделать вывод информативным: Валюту <Валюта> выгодно было купить <Дата>,
#продать <Дата>. Прибыль: <Разница в цене валюты>


from requests import get
import xml.etree.ElementTree as etree
from zeep import Client
import time
import datetime
import pprint
import pandas as pd
from pymongo import MongoClient
import warnings
warnings.filterwarnings('ignore')

START_DATE = '01/07/2018'
END_DATE = '01/07/2019'
CURRENCY = 'SEK'  #currency code

days_list = pd.period_range(start=START_DATE,end=END_DATE)

def get_rate(days_list=days_list,curr=CURRENCY):

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['currate']
    rate_db = db.currate

    url = 'https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?WSDL'
    client = Client(url)
    
    for day in days_list:
        #Подключаем монго. 
        money = client.service.GetCursOnDate(str(day))
        list_money=money._value_1._value_1
        for item in list_money:
            for k,v in item.items():
                if v.VchCode == CURRENCY:
                    one_day = {
                        'Date': str(day),
                        'Rate': float(v.Vcurs),
                        'Currency': v.Vname}
                    rate_db.insert_one(one_day)



#Call function to get & load data to Mongo
get_rate()
client = MongoClient('mongodb://127.0.0.1:27017')
db = client['currate']
rate_db = db.currate

#Сортируем и фильтруем данные по rate
rate_db.find().sort('Rate')
#count
qty = rate_db.count()
#print(qty)
maximum = rate_db.find({}).limit(1)
for m in maximum:
    max_date = m['Date']
    max_rate = m['Rate']
minimum = rate_db.find({}).skip(qty-1).limit(1)
for n in minimum:
    min_date = n['Date']
    min_rate = n['Rate']
    cur_name = n['Currency']
print(f'В период с {START_DATE} по  {END_DATE} {cur_name}')
print(f'было выгодно купить {min_date} по цене {min_rate:.2f},')
print(f'а продать  {max_date}  по {max_rate:.2f} рублей.')
print(f'Выгода {(max_rate - min_rate):.2f} рублей.')

