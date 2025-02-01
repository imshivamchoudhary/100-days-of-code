# python decorators
# A decorator is a function that takes another function as an argument and return a new function that modifies the behavior
# of the original function.THe new function is often refered to as a 'decorated' function.


def deco (fx):
    def mfx(*args,**kwargs):
        print("Hey Shivam")
        fx(*args,**kwargs)
        print('thank you for using our service\n')
    return mfx
@deco
def hello():
    print("hello")

@deco
def add(a,b):
    print(f'sum is {a+b}' )

hello()
add(10,20)
