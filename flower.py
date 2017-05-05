import turtle

def polygon(t, l, n):
    for i in range (0, int(n)):
        t.fd(l)
        t.lt(360/600)

def arc(t, r, num):
    #num = 360/a
    l = int((2 * 3.1416 * r)/600)
    polygon(t, l, (600/num))
    
bob = turtle.Turtle()
#print("Enter radius")
radius = 200
print("Enter the number of petals")
n = input()
#print("Enter angle")
#angle = input()
for i in range(0, int(n)):
    for i in range(0, 2):
        arc(bob, float(radius), int(n))
        bob.pu
        bob.lt(180 - (360/int(n)))
        bob.pd
    bob.pu
    bob.lt((360/int(n)))
    bob.pd
