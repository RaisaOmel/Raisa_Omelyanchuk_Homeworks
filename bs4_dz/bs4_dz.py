#С сайта https://www.21vek.by/mobile/iphone_15/ спарсить все названия смартфонов с их ценами.
#записать в csv файл: 1 колонка - названия телефонов, 2 колонка - на сколько GB, 3 колонка - стоимость
#Обработать файл и выяснить какой телефон с наименьшей стоимостью, а именно определить
# самый дешевый телефон на 128GB и на 256GB. Вывод должен быть следующим образом
# "телефон <название> на <количество GB>GB самый дешевый <цена>"
import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent
import csv
user=fake_useragent.UserAgent().random
headers={'user-agent':user}
url='https://www.21vek.by/mobile/iphone_15/'
response = requests.get(url,headers=headers)
rez=response.text
soup=BeautifulSoup(rez,'lxml')
block=soup.find_all('div',{'class':"style_product__uOVkK"})
minimum={}
for elem in block:
   block_new = elem.find('p', {'class': "CardPrice_currentPrice__EU_7r"})
   if  not (block_new  is None):
      lst = []

      price=float(block_new.text.rstrip(' р.').replace(',','.').replace(' ',''))

      block_new = elem.find('a').find('img')
      name=str(block_new['alt'])

      ind=name.find('GB')
      property=name[ind-4:ind].strip()

      elem=minimum.get(property,False)
      if elem:
          cena = elem[0]
          if price<cena:
             minimum[property]=(price,name)
      else:
         minimum[property] = (price, name)

      try:
         with open('mobile.csv', 'a', encoding='windows-1251', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            lst.append(name)
            lst.append(property)
            lst.append(price)
            writer.writerow(lst)
      except:
         print('ошибка с работой файлом чеки')

for key,val in minimum.items():
   print(f"телефон {val[1]} на {key}GB самый дешевый {val[0]}")