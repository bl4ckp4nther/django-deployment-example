# s="GLOBAL VARIABLES"
#
# def func():
#     mylocal = 10
#     print(locals())
#     print(globals()['s'])
#
# func()

# def hello(name="Jose"):
    # return "hello "+name
#
# print (hello())
#
# mynewgreet = hello #I'm setting mynewgreet equal to tha function itself not what the function returns
#
# print(mynewgreet())

# def hello(name="jose"):
    # print("THE HELLO() FUNCTION HAS BEEN RUN!")
#
    # def greet():
        # return "THIS STRING IS INSIDE GREET()"
#
    # def welcome():
        # return "THIS STRING IS INSIDE WELCOME!"
#
    # if name == "jose":
        # return greet#returning the function itself!!
    # else:
        # return welcome
    # print(greet())
    # print(welcome())
    # print("End of hello()")

#welcome() #error bcoz welcome inside scope of hello
#
# x = hello()
# print(x())



#function as argument
# def hello():
    # return "Hi JOSE!"
#
# def other(func):
    # print("HELLO")
    # print(func())
#
# other(hello)#passing function as arguments





#DECORATORS
def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func


@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR")

# func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()
