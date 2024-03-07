import tkinter as tk
import random

try_count = 0
answer = []
score = 0

def click_try() :
    global try_count
    global answer
    if try_count == 0 :
        answer1 = random.randint(1,45)
        answer.append(answer1)
        label_num1.configure(text = answer[0])
        try_count += 1
    elif try_count == 1 :
        answer2 = random.randint(1,45)
        answer.append(answer2)
        label_num2.configure(text = answer[1])
        try_count += 1
    elif try_count == 2 :
        answer3 = random.randint(1,45)
        answer.append(answer3)
        label_num3.configure(text = answer[2])
        try_count += 1
    elif try_count == 3 :
        answer4 = random.randint(1,45)
        answer.append(answer4)
        label_num4.configure(text = answer[3])
        try_count += 1
    elif try_count == 4 :
        answer5 = random.randint(1,45)
        answer.append(answer5)
        label_num5.configure(text = answer[4])
        try_count += 1
    elif try_count == 5 :
        answer6 = random.randint(1,45)
        answer.append(answer6)
        label_num6.configure(text = answer[5])
        try_count += 1
    else :
        pass

def click_result() :
    global score
    for i in range(6) :
        for j in range(6) :
            if number[i] == answer[j] :
                score += 1
    if score < 3 :
        label_result.configure(text = '꽝')
    elif score == 3:
        label_result.configure(text = '5등 5천원!!')
    elif score == 4:
        label_result.configure(text = '4등 5만원!!')
    elif score == 5:
        label_result.configure(text = '3등 150만원!!')
    elif score == 6:
        label_result.configure(text = '1등 10억!!!')

def clear() :
    global try_count, answer, score, number
    try_count = 0
    answer = []
    score = 0
    number = []
    label_num1.configure(text = '')
    label_num2.configure(text = '')
    label_num3.configure(text = '')
    label_num4.configure(text = '')
    label_num5.configure(text = '')
    label_num6.configure(text = '')
    label_result.configure(text = '')


number1 = random.randint(1,45)
number2 = random.randint(1,45)
number3 = random.randint(1,45)
number4 = random.randint(1,45)
number5 = random.randint(1,45)
number6 = random.randint(1,45)

number = [number1, number2, number3, number4, number5, number6]


window = tk.Tk()
window.title('lotetery game')
window.geometry('400x600')

font_label_title = ('맑은고딕', 35, 'bold')
font_label_result = ('맑은고딕', 35, 'bold')
font_button = ('맑은고딕', 25, 'bold')
font_num = ('맑은고딕', 25, 'bold')

label_title = tk.Label(text = '로또 뽑아보기', font = font_label_title)
label_result = tk.Label(text ='', font = font_label_result )
label_num1 = tk.Label(text ='', font = font_num)
label_num2 = tk.Label(text ='', font = font_num)
label_num3 = tk.Label(text ='', font = font_num)
label_num4 = tk.Label(text ='', font = font_num)
label_num5 = tk.Label(text ='', font = font_num)
label_num6 = tk.Label(text ='', font = font_num)
button1 = tk.Button(text = '뽑기', font = font_button, command = click_try)
button2 = tk.Button(text = '결과보기', font = font_button, command = click_result)
button3 = tk.Button(text = '초기화', font = font_button, command = clear)

label_title.place(relx = 0.5, rely = 0.2, anchor = tk.CENTER)
label_result.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
label_num1.place(relx = 0.11, rely = 0.35, anchor = tk.CENTER)
label_num2.place(relx = 0.27, rely = 0.35, anchor = tk.CENTER)
label_num3.place(relx = 0.43, rely = 0.35, anchor = tk.CENTER)
label_num4.place(relx = 0.59, rely = 0.35, anchor = tk.CENTER)
label_num5.place(relx = 0.75, rely = 0.35, anchor = tk.CENTER)
label_num6.place(relx = 0.91, rely = 0.35, anchor = tk.CENTER)
button1.place(relx = 0.2, rely = 0.7, anchor = tk.CENTER)
button2.place(relx = 0.7, rely = 0.7, anchor = tk.CENTER)
button3.place(relx = 0.5, rely = 0.85, anchor = tk.CENTER)

tk.mainloop()

