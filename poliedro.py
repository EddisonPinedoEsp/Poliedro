from turtle import *
bgcolor("black")
pencolor("blue")
pensize("7")
line = 7

for i in range(6):
    for i in range(8):
        left(30)
        forward(10 * line)
    for i in range(5):
        if i == 0:
            right(150)
        forward(10 * line)
        right(30 + 30 * i)
        forward(10 * line)
        right(150 - 30 * i)
        forward(10 * line)
        if i == 4:
            right(210)
        else:
            right(180)
            
done()

a = 20
b = 210