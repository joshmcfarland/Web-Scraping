# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from sqlite3 import SQLITE_CREATE_INDEX
from urllib import request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title.text)

table_rows = soup.findAll("tr")

state_death_ratio = ''
state_best_testing = ''
state_worst_testing = ''
highest_death_ratio = 0.0
highest_test_ratio = 0.0
lowest_test_ratio = 100.0

for row in table_rows[2:51]:
    td = row.findAll('td')

    state = td[1].text
    tot_cases = int(td[2].text.replace(',',''))
    tot_deaths = int(td[4].text.replace(',',''))
    tot_tested = int(td[10].text.replace(',',''))
    '''
    print(f'State:{state}')
    print(f'Total Cases:{tot_cases}')
    print(f'Total Deaths:{tot_deaths}')
    print(f'Total Tested:{tot_tested}')
    input()
    '''

    death_ratio = tot_deaths / tot_cases
    test_ratio = tot_cases / tot_tested

    if highest_death_ratio < death_ratio:
        state_death_ratio = state
        highest_death_ratio = death_ratio
    if highest_test_ratio < test_ratio:
        state_worst_testing = state
        highest_test_ratio = test_ratio
    if lowest_test_ratio > test_ratio:
        state_best_testing = state
        lowest_test_ratio = test_ratio

print(f'Highest Death Ratio: {highest_death_ratio}, {state_death_ratio}')
print('Death Ratio: ')
print(f'Highest Positive Test Ratio: {highest_test_ratio}, {state_worst_testing}')    
print(f'Lowest Positive Test Ratio: {lowest_test_ratio}, {state_best_testing}')


#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

