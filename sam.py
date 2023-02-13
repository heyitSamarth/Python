# reassign
s="sam"
s=[1,2,3]  #can change data type of same variable
print(s)

#STRING
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
print(f.readlines())#read for wole data and read lines for everything


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

#in keyword operator
print(1 in list1)