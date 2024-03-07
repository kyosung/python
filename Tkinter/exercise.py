import tkinter as tk # tkinter 라이브러리르 tk로 불러오기

count = 0

def click() :
    global count # 전역변수인 count를 로컬변수에 적용
    if count % 2 == 0 :
        label.configure(text = '클릭하셨습니다')
        count = count + 1
    else :
        label.configure(text = '되돌아갑니다')
        count = count + 1

window = tk.Tk() # tkinter의 객체 설정?

window.title('tkinter 연습') # 맨 위 제목 지정
window.geometry('400x300') # 윈도우 창의 크기 지정

font = ('맑은고딕', 20, 'bold') # font를 미리 정의(글꼴,크기,굵기)
label = tk.Label(text = '라벨', font = font) # 창 안에 글씨 입력
button = tk.Button(text = '클릭', font = font, command = click) # 창 안에 버튼 생성

label.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER) # 글씨 위치 지정
button.place(relx = 0.5, rely = 0.7, anchor = tk.CENTER) # 버튼 위치 지정

window.mainloop() # 창이 계속 떠있게 함
