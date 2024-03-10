import tkinter as tk

def submit() :
    value = selected.get()
    if value == 'nothing' :
        button.configure(text = '대답해주세요!')
    else :
        button.configure(text = value + '선택 완료!')

window = tk.Tk()
window.title('좋아하는 음식 조사')
window.geometry('800x800')

font = ('맑은고딕', 25, 'bold')
label = tk.Label(window, text = '다음 중 가장 좋아하는 음식을 고르세요!', font = font)
button = tk.Button(window, text = '완료', width = 15, height = 1, bg = 'green', command = submit)

label.place(relx = 0.5, rely = 0.1, anchor = tk.CENTER)
button.place(relx = 0.5, rely = 0.9, anchor = tk.CENTER)

selected = tk.StringVar()
selected.set('nothing')

food = ['치킨', '피자', '떡볶이', '햄버거', '라면']
for i in range(len(food)) :
    radiobutton = tk.Radiobutton(window, text = food[i], font = font, variable = selected, value = food[i])
    radiobutton.place(relx = 0.5, rely = 0.2 + (i * 0.1), anchor = tk.CENTER)

window.mainloop()
