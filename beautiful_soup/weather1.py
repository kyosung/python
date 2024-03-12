from bs4 import BeautifulSoup
import requests

url = 'https://weather.naver.com/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

