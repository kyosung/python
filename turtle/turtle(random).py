import turtle as t
import random

t.speed(0)
t.shape('turtle')
t.bgcolor('black')

color = ['paleturquoise', 'mediumturquoise', 'lightskyblue', 'powderblue', 'lightblue']

for i in range(10000):
    t.penup()
    
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    
    t.goto(x,y)

    t.pendown()
    
    t.color(random.choice(color))
    size = random.randint(0, 100)
    t.dot(size)

t.mainloop()
    
    

