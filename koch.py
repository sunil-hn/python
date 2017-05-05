import turtle

def koch(t, x):
    if ( x < 3 ):
        t.fd(x)
        return
    else:
        koch(t, int(x/3))
        t.lt(60)
        koch(t, int(x/3))
        t.rt(120)
        koch(t, int(x/3))
        t.lt(60)
        koch(t, int(x/3))

bob = turtle.Turtle()
koch(bob, 300)
