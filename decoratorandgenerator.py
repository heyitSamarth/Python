def gen(n):
    for i in range(n):
        # yield i
        print(i)
        yield i

g=gen(5)
g.__next__()


#Decorator 
def dec1(func1):
    def nowexe():
        print("execute")
        func1()
        print("executed")
    return nowexe
@dec1
def sam():
    print("sam")


# sam=dec1(sam)#this is decoreator
sam()

