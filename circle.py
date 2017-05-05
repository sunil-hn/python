import turtle

def polygon(t, l, n):
    for i in range (0, n):
        t.fd(l)
        t.lt(360/n)

def circle(t, r):
    l = int((2 * 3.1416 * r)/500)
    polygon(t, l, 500)
    

bob = turtle.Turtle()
print("Enter radius")
radius = input()
circle(bob, float(radius))
