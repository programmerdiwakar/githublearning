import turtle
t=turtle.Pen()
t.shape('turtle')
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.reset()
for i in range(20):
    t.circle(5*i)
    t.left(45)
    
