from re import A
from unicodedata import name
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
##
##
##
##

movie_table = soup.find('table')
#print(movie_table)

rows = movie_table.findAll('tr')
#print(rows[1])

'''for x in range(1,6):
    cols = rows[x].findAll('td')
    rank = cols[0].text
    name = cols[1].text
    gross = int(cols[5].text.replace(',','').replace('$', ''))
    total_gross = int(cols[7].text.replace(',','').replace('$', ''))
    date = cols[8].text
    percent_gross = round((gross/total_gross) * 100, 2)

    print(f"Rank: {rank}")
    print(f"Movie: {name}")
    print(f"Gross: {gross}")
    print(f"Total Gross: {total_gross}")
    input()'''


# create a new excel document
wb = xl.Workbook()
MySheet = wb.active

MySheet.title = 'Box Office Report'
MySheet['A1'] = 'No.'
MySheet['A1'].font = Font(size=16,bold=True)
MySheet['B1'] = 'Movie Title'
MySheet['B1'].font = Font(size=16,bold=True)
MySheet['C1'] = 'Release Date'
MySheet['C1'].font = Font(size=16,bold=True)
MySheet['D1'] = 'Gross'
MySheet['D1'].font = Font(size=16,bold=True)
MySheet['E1'] = 'Total Gross'
MySheet['E1'].font = Font(size=16,bold=True)
MySheet['F1'] = '% of Total Gross'
MySheet['F1'].font = Font(size=16,bold=True)


for x in range(1,6):
    cols = rows[x].findAll('td')
    rank = cols[0].text
    name = cols[1].text
    gross = int(cols[5].text.replace(',','').replace('$', ''))
    total_gross = int(cols[7].text.replace(',','').replace('$', ''))
    date = cols[8].text
    percent_gross = round((gross/total_gross) * 100, 2)

    MySheet['A' + str(x+1)] = rank
    MySheet['B' + str(x+1)] = name
    MySheet['C' + str(x+1)] = date
    MySheet['D' + str(x+1)] = gross
    MySheet['E' + str(x+1)] = total_gross
    MySheet['F' + str(x+1)] = str(percent_gross) + '%'


# change the column width
MySheet.column_dimensions['A'].width = 5
MySheet.column_dimensions['B'].width = 30
MySheet.column_dimensions['C'].width = 25
MySheet.column_dimensions['D'].width = 16
MySheet.column_dimensions['E'].width = 20
MySheet.column_dimensions['F'].width = 26


wb.save('BoxOfficeReport.xlsx')