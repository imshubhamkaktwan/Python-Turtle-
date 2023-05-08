import turtle
win=turtle.Screen()
win.bgcolor("light blue")
win.title("First Turtle program")

colors = ['red', 'purple', 'blue', 'green', 'orange']

t=turtle.Pen()
t.speed(10)
for i in range(30):
    t.pencolor(colors[i%5])
    t.circle(50)
    t.forward(2)
    t.right(15)
    
t.hideturtle()
turtle.done()