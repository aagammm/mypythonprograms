def greet(fx):
    def mfx(*args,**kwargs):
        print("Good morning")
        fx(*args,**kwargs)
        print("Thanks\n")
    return mfx

@greet
def hello():
    print("Hello world")

@greet
def sum(a,b):
    print(a+b)

hello()
sum(2,3)