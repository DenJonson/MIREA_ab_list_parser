import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


MY_SNILS = "177-498-905-45"

URL_TEMPLATE = "https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205826355502390"


request = requests.get(URL_TEMPLATE)

soupLayout = bs(request.text, "html.parser")
namesTable = soupLayout.find_all('tr') # массив из <tr>

for name in namesTable:
  # print(name)
  someFio = name.find('td', 'fio')
  if(someFio.string == MY_SNILS):
    print("___________________________________")
    yourNum = name.find('td', 'num').string
    print("Ваше место в списке: " + yourNum)
    yourMark = name.find('td', 'marks').string
    print("Ваш балл за экзамен: " + yourMark)
    yourAchivments = name.find('td', 'achievments').string
    print("Ваш балл за ИД: " + yourAchivments)
    yourSum = name.find('td', 'sum').string
    print("Ваш общий балл: " + yourSum)
    print("***********************************")
  
pInLayout = soupLayout.find_all('p')

for p in pInLayout:
  if("Всего мест" in p.text):
    word_list = p.text.split()
    tender = [int(num) for num in filter(
    lambda num: num.isnumeric(), word_list)][0]

print("Всего мест на направление: " + str(tender))
print("На " + str(tender) + " месте находится абитуриент с баллами:")
lastAbiturient = namesTable[70]
lastAbiturientNum = lastAbiturient.find('td', 'num').string
print("Место в списке: " + lastAbiturientNum)
lastAbiturientMark = lastAbiturient.find('td', 'marks').string
print("Балл за экзамен: " + lastAbiturientMark)
lastAbiturientAchivments = lastAbiturient.find('td', 'achievments').string
print("Балл за ИД: " + lastAbiturientAchivments)
lastAbiturientSum = lastAbiturient.find('td', 'sum').string
print("Общий балл: " + lastAbiturientSum)
print("___________________________________")

  
  # if(someName == MY_SNILS):
  #   for td in name:
  #     print(td.string)

# print(namesTable[53].text)

# print(namesTable.count)
