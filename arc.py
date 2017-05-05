import turtle

def polygon(t, l, n):
    for i in range (0, n):
        t.fd(l)
        t.lt(360/500)

def arc(t, r, a):
    num = 360/a
    l = int((2 * 3.1416 * r)/500)
    polygon(t, l, int(500/num))
    
bob = turtle.Turtle()
print("Enter radius")
radius = input()
print("Enter angle")
angle = input()
arc(bob, float(radius), int(angle))
