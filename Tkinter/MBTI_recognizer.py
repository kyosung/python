# tkinter import 하기
import tkinter as tk

# tkinter 기본 세팅
window = tk.Tk()
window.geometry('640x400')
window.title('MBTI 판별기')

# 변수 초기설정
question = [
            '1. 처음 보는 사람과도 어렵지 않게 이야기를 나누는 편인가요?',
            '2. 자유 시간에 다양한 관심사를 탐구하는 것을 좋아하나요?',
            '3. 다른 사람이 울고 있으면 자신도 울고 싶어질 때가 많나요?',
            '4. 일이 잘못될 때를 대비해 여러 대비책을 세우는 편인가요?'
           ]
result = [['E','I'], ['N','S'],['F','T'],['J','P']]
answer = []
value = []
mbti = ''
selected = tk.StringVar()
selected.set('nothing')

# 사용 함수 정의하기
def start() :
    label.configure(text = question.pop(0))
    btn.configure(text = '다음질문', command = next)
    
    radio_yes.place(relx = 0.3, rely = 0.6, anchor = tk.CENTER)
    radio_no.place(relx = 0.6, rely = 0.6, anchor = tk.CENTER)

def next() :
    global answer, value
    answer = selected.get()
    if answer == 'nothing' :
        label.configure(text = '답변을 선택해주세요!')
    else :
        value.append(answer)
        selected.set('nothing')

        if len(question) != 0 :
            label.configure(text = question.pop(0))

        else :
            label.configure(text = '결과를 확인하시겠습니까?')
            radio_yes.place_forget()
            radio_no.place_forget()
            btn.configure(text = '결과 확인하기', command = end)

def end() :
    global mbti
    for i in range(len(value)) :
        if value[i] == 'yes' :
            mbti += result[i][0]
        else :
            mbti += result[i][1]
    label.configure(text = '당신의 MBTI는' + mbti + '입니다')
    btn.place_forget()
    


# 폰트 정의하기
font = ('맑은고딕', 25, 'bold')

# 라벨 정의하기
label = tk.Label(text = 'MBTI 판별기', font = font, wraplength = 500)

# 버튼 정의하기
btn = tk.Button(text = '시작하기', font = font, bg = 'pink', fg = 'white', width = 15, height = 1, command = start)
radio_yes = tk.Radiobutton(window, text = 'Yes', font = font, fg = 'blue', variable = selected, value = 'yes')
radio_no = tk.Radiobutton(window, text = 'no', font = font, fg = 'red', variable = selected, value = 'no')

# 라벨 배치하기
label.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)

# 버튼 배치하기
btn.place(relx = 0.5, rely = 0.8, anchor = tk.CENTER)

window.mainloop()
