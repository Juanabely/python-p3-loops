#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 11
    while i > 1:
        i -= 1
        print(i) 
    if i == 1:
        print( "Happy New Year!")         

def square_integers(int_list):
    # code goes here!
    
   int_list = [num ** 2 for num in int_list]
   print(int_list)
   return int_list

def fizzbuzz():
    # code goes here!
    i = 0
    while i < 100:
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
           print(i)           
    pass

happy_new_year()
fizzbuzz()
square_integers([1,2,3,4,5])