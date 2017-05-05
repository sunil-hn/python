import turtle

def random_fractal(t, x):
    if ( x < 3 ):
        t.fd(x)
        return
    else:
        random_fractal(t, int(x/3))
        t.lt(90)
        random_fractal(t, int(x/3))
        t.rt(90)
        random_fractal(t, int(x/3))
        t.lt(90)
        random_fractal(t, int(x/3))
        t.rt(90)
        random_fractal(t, int(x/3))
        

bob = turtle.Turtle()
random_fractal(bob, 300)
