from bs4 import BeautifulSoup
import requests

# url에 주소 입력
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8'

# url에 저장된 주소에서 자료를 가져와라
res = requests.get(url)

# html을 파이썬이 알아먹을 수 있게 파싱(parsing)하기
soup = BeautifulSoup(res.text, 'lxml')

# 필요한 정보를 find 하기
current_temp = soup.find('span', 'weather before_slash').get_text()

# 필요한 정보 출력을 위한 처리
result = '[오늘의 날씨]\n' + current_temp + '\n\n오늘 하루도 행복하세요. 화이팅!'
print(result)




