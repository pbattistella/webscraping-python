import requests
import xlsxwriter
from bs4 import BeautifulSoup

URL = 'https://www.python.org/'
request = requests.get(URL)

html = BeautifulSoup(request.text, 'html.parser')
print("News of Python page")
print("Site:", URL)
print("Title Page: ", html.title.text)

div = html.find('div', class_='medium-widget blog-widget')
listItems = div.findAll('li')

workbook = xlsxwriter.Workbook('news-python.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Date')
worksheet.write('B1', 'News')
row = 2

for li in listItems:
    time = li.find('time')
    link = li.find('a')
    print(time.text, link.text)
    worksheet.write('A' + str(row), time.text)
    worksheet.write('B' + str(row), link.text)
    row += 1

workbook.close()