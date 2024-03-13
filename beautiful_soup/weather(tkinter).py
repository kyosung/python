from bs4 import BeautifulSoup
import requests
import tkinter as tk

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

current_temp = soup.find('span', 'weather before_slash').get_text()


window = tk.Tk()
window.geometry('640x400')
window.title('now weather')

font = ('맑은고딕', 25, 'bold')
label = tk.Label(text = current_temp , font = font)

label.place(relx = 0.5, rely = 0.5 , anchor = tk.CENTER)

window.mainloop()