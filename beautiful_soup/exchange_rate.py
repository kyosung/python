from bs4 import BeautifulSoup
import requests
import tkinter as tk
import datetime

# BeautifulSoup 와 requests로 환율정보 가져오기
url_usd = 'https://www.google.com/finance/quote/USD-KRW'
url_jpy = 'https://www.google.com/finance/quote/JPY-KRW'
res_usd = requests.get(url_usd)
res_jpy = requests.get(url_jpy)
soup_usd = BeautifulSoup(res_usd.text, 'lxml')
soup_jpy = BeautifulSoup(res_jpy.text, 'lxml')
usd = soup_usd.find('div', {'class' : 'YMlKec fxKbKc'}).get_text()
jpy = soup_jpy.find('div', {'class' : 'YMlKec fxKbKc'}).get_text()

# tkinter 설정
window = tk.Tk()
window.geometry('650x400')
window.title('환율맨')
font_date = ('맑은고딕', 15)
font_label = ('맑은고딕', 20, 'bold')
font_button = ('맑은고딕', 20)

# datetime으로 날짜설정
now = datetime.datetime.now()
now_date = now.strftime('%Y-%m-%d %H:%M:%S')

# 함수 설정
def refresh() :
    global now, now_date
    now = datetime.datetime.now()
    now_date = now.strftime('%Y-%m-%d %H:%M:%S')
    label_date.configure(text = now_date)
    label_main1.configure(text = '달러환율 : ' + usd +'원')
    label_main2.configure(text = '엔환율 : ' + jpy +'원')


# tkinter Label 설정
label_date = tk.Label(text = now_date, font = font_date)
label_main1 = tk.Label(text = '달러환율 : ' + usd +'원', font = font_label)
label_main2 = tk.Label(text = '엔환율 : ' + jpy +'원', font = font_label)

label_date.place(relx = 0.5, rely = 0.1, anchor = tk.CENTER)
label_main1.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)
label_main2.place(relx = 0.5, rely = 0.4, anchor = tk.CENTER)

# tkinter button 설정
button = tk.Button(text = '새로고침', width = 8, height = 1, font = font_button, command = refresh)
button.place(relx = 0.5, rely = 0.7, anchor = tk.CENTER)

# 계속 켜놓기
tk.mainloop()