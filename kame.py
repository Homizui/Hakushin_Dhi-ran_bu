import turtle
kame = turtle.Turtle()

kame.shape('turtle')
kame.shapesize(0.2,0.2,0.3)

a = 0
b = 1

f = 3

for i in range(10):
    a = a+b
    a,b = b,a
    print (a)

    kame.forward(f * a)
    kame.left(90)
    kame.circle(f * a,90)
    kame.right(90)
    kame.backward(f * a)
    kame.right(90)

    for j in range(3):
        kame.forward(f * a)
        kame.left(90)
    kame.forward(b * f)
    kame.left(180)
