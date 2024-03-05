import turtle as t
import random

t.speed(0)
t.shape('turtle')
t.bgcolor('black')

color = ['magenta', 'deepskyblue', 'greenyellow', 'deeppink', 'gold']

for i in range(300):
    t.penup()
    
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    
    t.goto(x,y)

    t.pendown()
    
    t.color(random.choice(color))
    draw = random.choice([t.circle, t.dot])
    size = random.randint(0, 100)
    draw(size)

    t.mainloop()
    
    

