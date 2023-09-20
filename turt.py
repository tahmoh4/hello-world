import turtle
window = turtle.Screen()
t = turtle.Turtle()
t.speed(1)
def turtlePacket():
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.left(45)
    t.backward(140)
for _ in range(1,9):
    turtlePacket()
window.exitonclick()        
