import turtle as t
t.bgcolor('black')
t.shape('turtle')
t.speed(0)

color = ['deeppink', 'deepskyblue', 'greenyellow']

i = 0

while True :
    t.color(color[i % 3])
    t.fd(i)
    t.lt(114)
    i = i + 1
