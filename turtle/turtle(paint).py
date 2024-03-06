import turtle as t
import random

def go_right() :
    t.setheading(0)
    t.fd(10)

def go_up() :
    t.setheading(90)
    t.fd(10)

def go_left() :
    t.setheading(180)
    t.fd(10)

def go_down() :
    t.setheading(270)
    t.fd(10)

def pen_updown() :
    if t.isdown() :
        t.penup()
    else :
        t.pendown()

def pen_color() :
    color = ['red', 'blue', 'green', 'orange', 'black']
    choice = random.choice(color)
    t.color(choice)

def clear() :
    t.clear()
    t.color('black')


t.shape('turtle')
t.onkeypress(go_right, 'Right') 
t.onkeypress(go_up, 'Up') 
t.onkeypress(go_left, 'Left') 
t.onkeypress(go_down, 'Down') 
t.onkeypress(pen_updown, 'Return') 
t.onkeypress(pen_color, 'c')
t.onkeypress(clear, 'Escape')  

t.listen()
t.mainloop()
