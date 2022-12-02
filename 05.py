import requests
import json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
url = "https://api.github.com/repos/richkempinski/hellogitworld/commits"
r = requests.get(url, headers = headers)
html = r.content.decode('utf-8', 'ignore')
my_page = BeautifulSoup(html, 'lxml')

for tag in my_page.find_all('r', class_='Repo'):
    introduction = tag.get_text()
    disease_introduction = introduction

for tag in my_page.find_all('c', class_='commits'):
    sub_tag = tag.find('cm',class_="commit") 
    my_span = sub_tag.findAll('span')
    #my_span is a list
    is_yibao = my_span[1].text   
    othername = my_span[3].text  
    fbbw = my_span[5].text        
    is_infect = my_span[7].text   
    dfrq = my_span[9].text       
    my_a = sub_tag.findAll('a')
    xgzz = my_a[2].text+' '+my_a[3].text+' '+my_a[4].text 
