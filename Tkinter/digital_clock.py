import tkinter as tk
import time

def clock() :
    now = time.strftime('%Y년 %m월 %d일 \n %H  : %M  : %S')
    label.configure(text = now)
    label.after(100, clock)

window = tk.Tk()
window.title('Digital Clock')
window.geometry('400x300')

font = ('맑은고딕', 25, 'bold')
label = tk.Label(text = '시간 버튼을 누르세요', font = font)
button = tk.Button(text = '시간', font = font, command = clock)

label.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)
button.place(relx = 0.5, rely = 0.7, anchor = tk.CENTER)

window.mainloop()
