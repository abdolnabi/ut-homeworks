
from bs4 import BeautifulSoup
import requests

exportFile = open('slr-pcvfc.csv', 'a')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=%28%22Fog+cloud%22+OR+%22Fog-cloud%22+OR+%22Fog+cloud+computing%22+OR+%22fog-cloud+computing%22%29+AND+%28%22Privacy+challenges%22+or+%E2%80%9CPrivacy%E2%80%9D+or+%E2%80%9CPrivacy+preserving%E2%80%9D%29+AND+%28%22Vehicular%22+OR+%22VFC%22+OR+%22Vehicular+technology%22%29&btnG='
url1 = 'https://scholar.google.com/scholar?start=10&hl=en&as_sdt=0%2C5&q=%28%22Fog+cloud%22+OR+%22Fog-cloud%22+OR+%22Fog+cloud+computing%22+OR+%22fog-cloud+computing%22%29+AND+%28%22Privacy+challenges%22+or+%E2%80%9CPrivacy%E2%80%9D+or+%E2%80%9CPrivacy+preserving%E2%80%9D%29+AND+%28%22Vehicular%22+OR+%22VFC%22+OR+%22Vehicular+technology%22%29&btnG='
for i in range(0,9):
    print(str(i*10))
    url2 = 'https://scholar.google.com/scholar?start='+str(i*10)+'&hl=en&as_sdt=0%2C5&q=%28%22Fog+cloud%22+OR+%22Fog-cloud%22+OR+%22Fog+cloud+computing%22+OR+%22fog-cloud+computing%22%29+AND+%28%22Privacy+challenges%22+or+%E2%80%9CPrivacy%E2%80%9D+or+%E2%80%9CPrivacy+preserving%E2%80%9D%29+AND+%28%22Vehicular%22+OR+%22VFC%22+OR+%22Vehicular+technology%22%29&btnG='
    response=requests.get(url2,headers=headers)
    soup=BeautifulSoup(response.content,'lxml')
    for item in soup.select('[data-lid]'):
        try:
            print(item.select('h3')[0].get_text()+'^'+item.select('a')[0]['href'], file = exportFile)
            #print(item.select('h3')[0].get_text()+'^'+item.select('a')[0]['href'])
            #print('----------------------------------------')
        except Exception as e:
            # raise e
            print('')
