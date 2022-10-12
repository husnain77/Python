
#Python Intrductory Guide

name = input("What is your name?")
print ("Hello, " + name)  

#Fundamental Data Types
#int and #float--- Integers and Decimals
print (2 * 4)
#to see data types use
print(type(4 + 2)) #int
print(type(6 / 3)) #float---as 2.0 decimel 
print (2 ** 4) #2^4 power of integer
print (5 // 2) #division answer roundedoff to integer
print (5 % 2) #modulo is remainder of divison
complex
bin
bool
str
greet = '''
How are you?
o  o
____  
''' + name
print(greet)
 
list
tuple
set
dict

#string concetenation
goodcar = ('mercedes ' + 'benz')
carnumber = ("mercedes" )
print(goodcar)

# math function
print (round(3.69)) #roundoff
print (abs(-20)) #returns absolute number(no negative number)

# type Conversion
print(type(str(100))) #int 100 converted to string
print(type(int(str(100)))) #into 100 converted to string, then again to int

#escape sequence
print(str(" \t It\'s a good \'type\' of weather. \nIs it?"))   #\t ----tab ,  \n ----newline,  \' ---- apostrophy

# formatted sequences
username = 'Jhon'
age = 55
print ('Hi,' + username + '. You are ' + str(age) + ' year\'s old') 
# ^ this can be written in formatted sequence as 
print (f'Hi, {username} you are {age} year\'s old.')       #best way of writing is into formatted sequence
#can also be written as                            0      1
print ('Hi, {1} you are {0} year\'s old.'.format(age, username)) # can also be written in this form

#string indexes -------immutable(cannot reasssign)
selfish = "me me me"
        #   01234567
print(selfish[3]) #so this will print m
        # [start:stop]
print(selfish[2:5])

#string slicing
stepover = "0123456789"        
        #   0123456789
        #[start:stop:stepover]
print(stepover[0:6:2])  #skip on to every second string starting from 0
print(stepover[1:9:3])  #skip on to every third string starting from 1


#reverse the string selfish and stepover
print(selfish[::-1])
print(stepover[::-1])

#Immutability
#We cannot reassign/edit a particular index on a string we have to reassign the whole string
#But we can add another index into the string e.g
stepover = stepover + "69"
print(stepover)

#length of string
print(len(stepover))

#print to a specific length
print(stepover[0:7])

#upper case the letters
print(selfish.upper())

#capitilize the first letter
print(selfish.capitalize())

#find if me exist in selfish
print(selfish.find('e'))  #output will tell us that e is located in following index
#find if 9 exist in stepover
print(stepover.find('9'))  

#replace me with you (in replace we are not reassigning the value to same string but making a new string with replacement value)
print(selfish.replace('me','you'))

#type conversion
birthdate = input("What year were you born? ")
intbirthdate = int(birthdate)
intage = 2020 - intbirthdate
age = str(intage)
print('Your age is: ' + age)

#or can be coded as
age = 2020 - int(birthdate)
print(f'Your age is: {age}')


# Augmented Assignment operator
# for example
iq = 120
iq = iq + 20 # can also be written as iq += 20 
print(iq)
#something like this can also be written for aq as
aq = 120
aq += 20
print(aq)

#Custom Data types --- classes

#Specialized Data types --- Modules

#password checker
usersname = input('Give username: ')
userpassword = input('Set password: ')
passlength = len(userpassword)
encryptedpass = '*' * passlength
print(f'{usersname}, your password {encryptedpass} is {passlength} long!' )

#list  ----- form of arrays that we can get reassign(hence mutable) unlike strings   -----Data Struscture (container with multiple types of data types)
examplelist = [1, 2.5, 'a', True]
#arraryindex#  0   1    2    3
print(examplelist[2])   #accessing purticular array index

#list slicing
amazon_cart = ['Hands on ML book', 'Grapes', 'Core i7', 'toys', 'RTX Titan','bananas']
print(amazon_cart[0:4:2])
#reassigning value on index 0
amazon_cart[0] = 'Deeplearning book'
print(amazon_cart) 
#making new separate list for grapes and bananas ----must include [:] after the name of list you are making new one 
new1_cart = amazon_cart[1::4]  #upon reassigning value to this new1_cart list, this will not assign value to the amazon_cart  
print(new1_cart)
new2_cart = amazon_cart #this will reassign the values to orignal amazon_cart list because this doesnot have [:]
new2_cart[0] = 'PapaPig book' 
print(new2_cart)

#Matrix   MULTIDEMENTIONAL arrays or lists

gigi = [   #two dimentional in this example
    [4,6,7],
    [7,5,9],
    [2,6,8]
    ]
print(gigi[2][1])  #printing specific index from matrice

# append ---  to add object to original data types' array but doesnot give any return None to new datatype 
basket = [1,2,3,4,5,6]
#new1basket = basket.append(7) #this is wrong and it will result to none because append doesnot give any result(=None)
#print(new1basket)                                # instead we should something like we have done at bottom
basket.append(7)  #first add 7
new1basket = basket #then create new 
print(new1basket)

#insert -----to insert/modify object to a specific index in array but doesnot out put any result to new datatype
basket.insert(3, 69)
print(basket)

#extend
basket.extend([67, 63])
print(basket)

#pop----remove at indexvalue at specific index
basket.pop(-2) #popping 67
print(basket)

#remove ----specific value
basket.remove(63)
print(basket)

#clear ---clear whole array
basket.clear()
print(basket)

#index. -------finding index value of object stored in array
##print(basket.index(3,0,4))

#Python keywords 
#in
print('d' in basket)
print('2' in (basket))
print ('s' in 'Hi my name is Husnain')

#count
print(basket.count(3))


#sorted-----sorts and produces a new array and then sort
tokri = ['a','c','d','b','e']
print(sorted(tokri))

#sort ------sorts the original array
tokri.sort()
print(tokri)

#copy ----copy the array(list) and produces new array(list)
newtokri = tokri.copy()
newtokri.sort()
print(newtokri)

#reverse ------ swititches indexes to opposite direction on the original list
tokri.reverse()
print(tokri)

#reverse -----switiches indexes to opposite direction while creating the new list
print(tokri[::-1])

# Question; Reverse a list into ascending order
tokri.sort()
tokri.reverse()
print(tokri)

#range
print(list(range(10,101)))

#join
sentence = ' muskarake '
newsentence = sentence.join(['my', 'name', 'is', 'Husnian'])
print(newsentence)
another_sentence = 'muskranake '.join(['my','name''is', 'Ali'])
print(another_sentence)


#list unpacking
a,b,c,*other = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)

#dictionary ------unordered key value pair stored in various spots in memory(unlike lists which are stored right next to each other)
dicdict = {     #dictionary made with name dickdict and can have any type of data type values
   #key : value,
    'a' : [1,2,3], 
    'b' : 'Hello Bishes',
    'x' : True    
}  #[itemindex]][key][valueindex]
print(dicdict['b'][1])  #in this case there is only one iteminset({key;value}) so we will not state itemsetindex suchas "[0]" in this case

#create a dictionary in a list and return value
mlist = [
    {     #firsts itemset dictionary created
    'a' : [9,4,7], 
    'b' : 'Hello Bishes',
    'x' : True    
 },#note this comma
    {    #second itemset dictionary created
    'a' : [7,6,9], 
    'b' : 'yooo',
    'x' : True     
 }
 ]
#   [itemindex][key][value]
print(mlist[1]['a'][2])


# #Dictionary
userA1 = {
   'basket':[1,2,3],
   'greet':'hello',
    'age':100
}
#.get method is used to stop the occurance of error printing info from the key as it prints the default value if the key is unavailable in the dictionary
#             (key, default value)
print(userA1.get('age' , 'none'))
print('basket' in userA1) #this checks in keys as well as the values
print('basket' in userA1.keys()) #this checks in keys only
print('basket' in userA1.values()) #this checks in values only

# #Second way to create dictionary
# user61 = dict(houselen =269,househeight=69)
# print(user61) 

#copy dict into newly created dict 
userA2 = userA1.copy()

#clear dictionary
print(userA1.clear())

print(userA2)
print(userA1)

# #remove particular key from existing dict or the last one as default
# userA2.pop("age")
# print(userA2)

# #removes a random key from a dict
# userA2.popitem()   
# print(userA2)

#turn hash '#' on for upper two examples of 'remove'
#update a particular key from existing dict/or add if the key doesnot exist in the dict
userA2.update({"age":62})
print(userA2)


#Tuple---immutable
MLbits=(67,78,54,106,67)
x = MLbits[1]
y = MLbits[0]

print(x) 

# this ^ tuple can also be written as
     # (*other)
x,y,z, *d = (34,87,56,93,98)
print(d)
print(x)
print(y)
print(z)

#Tuple has only two methods ('count' , 'index')
#count ----counts how many time a certain value occured in a tuple
print(MLbits.count(67))
#index ----states at which index does the value(that u input) occurs at first
print(MLbits.index(67))
     
#sets-----only returns unique items
aiset = {4,56,78,23,23}
print(aiset)
aiset.add(4)     #will not add another 4 cuz is already in there
print(aiset)
     
#Convert list into set with set function

mllist = [27,93,75,23]
mlbj = set(mllist)
print(mlbj)
     
# #conditional statements
is_old = False
is_licenced = True
#condition 1
if is_old:
    print('You are old enough to Drive')
elif is_licenced:
    print('you can drive now!')
else:
    print('You are not old enough') 
print("okok")
#condition 2 (make condition one sstatement before running condition two)
if is_old and is_licenced:
    print("Car is ready to be drive!")

else:
    print('You are not old enough') 
print("okok")

#Truthy and Falsy
print(bool("Hello"))   
print(bool(5))
print(bool(""))
print(bool(0))

#using Truthy and falsy values
is_old = "Hello"
is_licenced = 5
#condition 1
if is_old:
    print('You are old enough to Drive')
elif is_licenced:
    print('you can drive now!')
else:
    print('You are not old enough') 
print("okok")

#Ternary Operator---322

# True_condition "if" condition "else" False_condition
is_friend = True
message = "Message Allowed" if is_friend else "Message not Allowed"
print(message)

#Short Circuit
#example of short circuiting on "or"
isFriend = True
isUser = False

if isFriend or isUser:  #Interpreter doesnot read isUser in "or" logical operator if isFriend is True because condition has been met already
    print("You can message")

#example of short circuiting on "and"
isFriend = False
isUser = True

if isFriend and isUser:  #Interpreter doesnot read isUser in "and" logical operator if isFriend(First condition) is false.
    print("You can message")

#Logical Operators ....>,<,>=,<=,==,and, or, not
print(4==5) #it will output false
print('hello' == 'hello')   
print('a'<'b') #b is greater than a and its True
print('a'>'A')  # a is greater than A and its True

#"not" Logical operator
print(not(4==5))

# MAGICIAN EXCERSICE
magician = True
expert = False
if magician and expert:
    print("You are a master magician")
# elif magician or expert: #this will shortcircuit so its must to be magician before becomig expert
#this ^ line can also be written as 
elif magician and not expert:
    print("Atleast you are getting there")
# else:
#  print("You need magic powers")
#these above ^ two lines can also be written as:
elif not magician:
    print("You need magic powers!")


print(True == 1) #True
print('' == 1)   #False
print([] == 1)   #False
print(10 == 10.0) #True
print([] == [])  #True


#FOR LOOP----327
for my_car in (1,2,3,6,4,5):
    print(my_car)
    print(my_car)
print(my_car)  #last variable in the string will be printed

for aicar in (1,2,3,4,5): #run first variable to last in this first loop
    for airbagstype in ('a','b','c'): #run a to c for '1' and go back to 2 and run the loop again
        print(aicar,airbagstype) 

# Iterables-----One by one check each item in the collection----328
# iterable items are as following -- list,dictionary,tuple,set,string but not integer/int etc!
userofAI = {
    'name' : 'Golem',
    'age': 5006,
    'can_swim' : False
}
for item in userofAI.keys():
    print(item)
for item in userofAI.items():
    print(item)  
for item in userofAI.values():
    print(item)
    
    
crusher={
    #key : values      this dict has 3 items 
    'Name':'Crusher ANC',   
    'ANC Enabled': True,
    'Watt(Power)': 125
}


for item in crusher.keys():
    print(item)
for item in crusher.values():
    print(item)
for item in crusher.items():    
    print(item)
    
    
#converting and unpacking the items in the dict to tuple(using crusher example)
#There are two ways
#Long route (way)
for item in crusher.items():
    (key, value) = item;    #converting to tuple
    print(key, value)
#Short-hand way    
for (key, value) in crusher.items():
    print(key,value)
#key and value can also be named as k and v
for (k,v) in crusher.items():
    print(k,v)

#Trickycounter---329
counterlist = [1,2,3,4,5,6,7,8,9,10]

counter = 0
for item in counterlist:
    counter= counter + item
print(counter)


#range----330
print(range(100))
# ^is same as :
print(range(0, 100))

for item in range (0,100):
    print(item)
    
#Stepover
for _ in range (0,100,10):  #this would skip to 10th value
    print(_)
   
#stepback or range in reverse
for _ in range(10,0,-1):
    print(_) 

#create two list of 0-10 int
for _ in range (2):
    print(list(range(0,11)))
    
    
#enumerate ----331   apply index to the iteratable objects
#it takes an iterable object and gives an indexvalue and item of them index   indexnum(enum)+iteratableitem(arate-------------------)=enumarate
for i,char in enumerate("Hellooooooo bitches"):
    print(i,char)
    
for i,char in enumerate([1,2,3,4,5]):
    print(i,char)
    
#print the index at 50int
for i,char in enumerate(list(range(0,100,10))):
    if char == 50:
        print(fr'index of 50 = {i}') #creating fr string 

#While loops --332

i=0
while i<50:
    print(i)
    i += 1   #i= i + 1  <<Shorthand
else:
    print('Done with all the work')

# #Printing same output on both for and while loop
gg_list = [1,2,3]
for item in gg_list:
    print(item)
    
i = 0
while i < len([gg_list]):  
    print(gg_list[i])
    i += 1
    break

 #Repetetive asking
while True:
    input('say something: ')
    break

 #Repetetive asking until answer received
while True:  
    response = input('say something: ')
    if (response == 'bye'):
        break
    
  #pass ----to avoid the bug in loops when there is no code under loop----334
gb_list = [1,2,3]
for item in gb_list:
    pass    #This will bug if there is no pass bcuz there is no code to loop on so it will just pass 


  #Continue-----continues on the top and start from top of enclosing loop ---334
gc_list = [1,2,3]
for item in gc_list:
    continue           #nothing will be printed as the loop will continue to top from here and never reach print(item)
    print(item)

#First GUI
#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

 #iterate over picture;
   #if 0 -->print ' '
   #if 1 -->print *
for row in picture:
  for pixel in row:
    if (pixel == 1):
      print("*", end='')
    else:
      print(" ", end='')
  print('')   #need a new line after every row
    
#clean
#Readability
#Predictability
#DRY-----donot repeat yourelf

 #Duplicates finding excersice ---337
dupli_list = ['a','b','c','d','b','m','n','m']
duplicates = []
for value in dupli_list:
  if dupli_list.count(value) > 1:
    if value not in duplicates: #cant understand this
      duplicates.append(value)
print(duplicates)      

#functions -----to make code DRY
def say_hello():
  print('helllooooo')
  
say_hello() 

#making XmasTree function from above code and producing to xmastrees 3 times
def xmastree(): 
  picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
  ]

  #iterate over picture;
    #if 0 -->print ' '
    #if 1 -->print *
  for row in picture:
    for pixel in row:
      if (pixel == 1):
        print("*", end='')
      else:
        print(" ", end='')
    print('')   #need a new line after every row
    
xmastree()
xmastree()
xmastree()


#parameters ------Used to define functions so u first set parameters
def speak_hello(name="DeatVader",emoji="{:)"):
    print(f'helloooo { name}{ emoji}')
    
#Argument --------Used to call Funtions so then to call the set parameters we use arguments
#Positional Arguments-----------we have to care that position of nameparameter and emojiparameter afterward comes first 
speak_hello('husnain',':)')    #as stated in the parameters above, while calling parameters
#keword Argument --- we dont care about position of the stated parameters while calling
speak_hello(emoji=':(',name='Hussnain')  #BUt THIS IS BADD PRACTISE
speak_hello()

#Return ---its also a function
#function either modifies something or return something  and do a the required job to be done really well
def sum(num1,num2):
  return (num1 + num2)

print(sum(10,sum(10, 5)))   
#^this is same as :
total = sum(10,5)
print(sum(10, total))

#return a function inside a function
def sum(num1,num2):
  def another_func(num1,num2):    
    return (num1 + num2)       #returning num1 and num2 addition
  return another_func(num1, num2)  #returning the function where the num1 and num2 addition was made

total = sum(10,5)
print(total)

#Tesla Excersice ------342
#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?
def checkDriverAge():
    age = input("What is your age?: ")
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge()

#2 Instead of using the inp
#ut(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

def checkkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are just a baby to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
checkkDriverAge(9)     


#Docstring-----give info of the function when we we comment using 3 single qoutes
def test(a):
    
    '''
    Info:this function tests and prints param a
    '''
    print(a)
test('aaaa')

#Help----this function is used to help u out to print out what the function can do (or to print the doc string)
help(test)
#can also be seen while printing 
print(test.__doc__)


#Clean code -- Following example1 is shown as raw code which can be cleaned further to example 2
#Exampe 1 ---raw code
def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False
    
print(is_even(42))

# Example 2  --- can be cleaned to this example
def is_even(num):
    if num % 2 == 0:
        return True
    return False
