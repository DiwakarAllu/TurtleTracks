from turtle import *
speed(0)
hideturtle()
bgcolor('black')
for i in range(100):
    color('cyan')
    for j in range(6):   # for 18 => same as for 6
                          # for 4 multiples => 3 head_fans
        fd(i)
        rt(50*3)
        lt(20*3)
    rt(120*2)

done()