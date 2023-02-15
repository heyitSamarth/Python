import one
def fuc2():
    print("function from 2 .py ")

if __name__=="__main__":
    print("if it is executed directly for 2.py ")
    one.fuc1()
    fuc2()
else:
    print("it is emported  for 2.py")