# reassign
s="sam"
s=[1,2,3]  #can change data type of same variable
print(s)

#STRING (immutable)
s='Hey Sam!'
print(s[2:])
print(s[:2])#exclusive of 2
print(s[::2])
print(s[2:5:3])#last argument  jumps the pointer
print(s[::-1])#reverse the string
#string are immutable means s[0]=w will give error


s=s+" How are u???"
print(s)
print(s*5)

print(s.upper())
print(s.split('H')) # it will split from parameter by defult it is space

print("I am good {b} How are u {a} ???".format(a='Sir .',b='btw'))#Use .formate for adding variable element in middle of string 

print("answer is {ans:1.4f}".format(ans=1.22212231242342))#format follows  value:width.precisionf
print(f'{s}')#use any variable

#----------------------------------------------------------------
#LIST (ordered , mutable )
my_list=['one',2,'three']
print(len(my_list)) 
#same as string but list are mutable
my_list.append(4)#add item to end of list

poped_item=my_list.pop()#remove paramenter index from list by defult it is end.
poped_item=my_list.pop(1)
my_list.sort() #do inplace sorting does not return any element.

print(my_list)

#----------------------------------------------------------------
#Dictonary (unordered ,mutable )
 
my_dict={1:"sam",'two':"samarth",3.14:"sammy"}
print(my_dict[3.14])
print(my_dict['two'])
#can access value by passing key (two value are associated with each other)
my_dict[8]="samarth dubey"#add value in dict 
print(my_dict)
my_dict.values()#return both item in tupple which are in list

#----------------------------------------------------------------
#Tuples( ordered ,immutable)

#same as list
t=(1,2,1,'sam')
print(t.count(1))#can count no of occurance and .index will have first occurance of it



#----------------------------------------------------------------
#SETS(unorderd collection of unique elements)
myset=set()
myset.add(1)
myset.add(2)
myset.add(1)
print(set(t))#ussing set will make any data structure contain unique values 


#----------------------------------------------------------------
#Boolen

True#capital t in true is difined
print(type(1>2))

#----------------------------------------------------------------
#Files
f = open("demofile.txt","w")# use a for append and w to re -write
f.write("samarth dubey watchguard 2")
f.close()
f = open("demofile.txt","r")#use r to read a file
print(f.read())#read for wole data and read lines for everything


#----------------------------------------------------------------
#Condition
#for loop can itrate to list string and dictonary
num=[1,"two",3,"four",5,"six"]
for i in num:
    print(i)
#if u don't need itreator variable u can use "_"
for _ in num:
    print("sam")
for a,b in [("a","b"),("c","d")]:
    print (a)

    #break the current loop
    #continue goes to the next itration from top
    #pass does nothing

#zip
list1=[1,2,3,4]
list2=["one","two","three","four"]

for item in zip(list1,list2):#joint multiple  list and create tuples 
    print(item)

mylist=[n**2 for n in range(0,11) if(n**2)%2==0]
#single line code
print(mylist)
#in keyword operator
print(1 in list1)

#----------------------------------------------------------------
#FUNCTION
#def will tell about function and it is written in snake casing

def function1(num1=1,num2=1):#create defult value
    return num1+num2

print(function1(5,6))

def checkeven(numlist):
    evenlist=[]
    for n in numlist:
        if(n%2==0):
            evenlist.append(n)
    return evenlist

print(checkeven([1,3,5,7,2,4,6,8,0]))

#return multiple item with tupple unpacking

#----------------------------------------------------------------------
#Game
def take_guess():
    n=''
    while n not in ['0','1','2']:
        n=input("Take a Guess! 0  ,  1   or   2  ->>>  ")

    return int(n)
def check_guess(mylist,guess):
    if(mylist[guess]=='0'):
        print("You Win !!!!")
        print(mylist)
    else:
        print("You loose\n")
        print(mylist)


from random  import shuffle
mylist=[' ',' ','0']
shuffle(mylist)
# guess=take_guess()
# check_guess(mylist,guess)

#-------------------------------------------------------------
# *ARGS AND KARGS

#as some time we need more parameters 
def myfunc(*args):
    return sum(args)*0.05

print(myfunc(20,10,30,50))#insert any arguments as u want

#keywordarguments are **kwargs
def myfunction(**kwargs):
    if("fruit" in kwargs):
        print('my fruit is {} .'.format(kwargs['fruit']))
    elif("veggi" in kwargs):
        print ('my veggi is {} .'.format(kwargs['veggi']))
 

myfunction(fruit="Apple",veggi="tomato")



#-------------------------------------------------------------------
def square(num):
    return num**2
def odd(num):
    return num%2==1
for item in map(square,list1):#we can use map function to map a function a data that need to run 
    break
print(list(map(square,list1)))


print(list(filter(odd,list1)))#will map two function but filter it as functio that is passesd and return bollean and return value of input list

square=lambda num:num**2
print(square(2))

print(list(map(lambda num:num**2,list1)))

#scope
#LEGB RULE
#L local within function local scope like lambda or def
#E Enclosing function locals 
#G Global declared global 
#B built in global 



#-------------------------------------------------------------------
#OOPS

class Dog():
    #same for every instance of class
    species='mamal'
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name

    def bark(self,num):
        print("Woof! My name is {} and number is {}".format(self.name,num))


my_dog=Dog("husky","annie")
my_dog.bark(5)


#-------------------------------------------------------------------
#Advance programing modules
from collections import Counter
mylist=[1,1,1,2,3,4,4,4,4,1,1,3,6,2,3,4,5,3]
print(Counter(mylist)) #tell frequency of every element and put it in dictonary 
d=Counter("aihdiahdaihi21hi21ub")
print(d) #can use dictonary modules
print(d['i'])

from collections import defaultdict
#it will assing default value when key error occcour

dd=defaultdict(lambda:0)
dd["kkk"]=879
print(dd['o'])


from collections import namedtuple
Dog=namedtuple('Dog',['age','name','breed'])
sammy=Dog(age=5,breed='Husky',name='sammy')
print(sammy)


f=open('practice.txt','w+')
f.write("MY NEW FILE")
f.close()

#os will help to run os commands
import os
print(os.listdir())
#shutil will hep to use shell comand
import shutil
# shutil.move( "practice.txt",'C:\Users\sdubey\Desktop')


#import date timr for date and time factors

import datetime
mytime=datetime.time(13,4,50,20)
print(mytime)
today=datetime.date.today
print(today())


#Regular expressions
import re
#\d a digit 
#\w a alfanumeric
#\s white space
#\D  a non digit 
#\W  non alphanumeric
#\S non whitespace
#+ occure more then one time
#{3} occure 3 times
#{2,4} occure 2 to 4 times
#{3,} occure 3 or mpre times
#* occure 0 or more times
#? once or none
# | pipe operatore used as or 


#---------------------------------------------------------------------
#WEB SCRAPPING
import requests,bs4,lxml
result=requests.get("https://watchguard.udemy.com/course/complete-python-bootcamp/learn/lecture/20345241#overview")
soup=bs4.BeautifulSoup(result.text,"lxml")#this will make code arranged and sytmatic 
print(soup.select('title')[0].getText())#get text we can just get main text aut of whole content
# for image
print(soup.select('img'))



#---------------------------------------------------------------------
#Image in python (PIL library)
from PIL import Image
mac=Image.open('example.png')
mac.show()
#crop image
mac.crop((0,0,100,100))
  
#----------------------------------------------------------------
#smtplib for email
# import smtplib,getpass
# smtp_object=smtplib.SMTP('smtp.gmail.com',8000,'/')
# email=getpass.getpass("enter email")
# password=getpass.getpass("enter password")
# smtp_object.ehlo()
# smtp_object.login(email,password)

#-----------------------------------------------------------------
#GUI
from ipywidgets import interact ,fixed,interactive
import ipywidgets as widgets


def func(x):
    return x
interact(func,x=10)


#Error Handling
def divide(dividend,divisor):
    if divisor==0:
        raise ZeroDivisionError("Devisior can't be zero")

grades=[]
try:
    average=divide(sum(grades),len(grades))
    print(f"The average grade is {average}.")
except ZeroDivisionError as e:
    print("There are no grades yet in your list .")
else:
    print("This will run if except dont run  ")
finally:
    print("this will run whatever is the case")


from flask import Flask