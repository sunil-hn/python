import turtle
def square(t, length):
    for i in range (0, 4):
        t.fd(length)
        t.lt(90)

def polygon(t, l, n):
    for i in range (0, n):
        t.fd(l)
        t.lt(360/n)

bob = turtle.Turtle()
print("Enter number of sides")
sides = input()
print("Enter length")
length = input()
polygon(bob, int(length), int(sides))
#turtle.mainloop()
