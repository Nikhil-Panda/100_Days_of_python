import random
#loops 


#looping through a list
names= ['andrew','bob','charlie']
for name in names:
    print(name)
#name is a temporary variable
print(names)


#print "Fizz" if divisible by 3
#print "Buzz" if divisible by 5
#print "FizzBuzz" if divisible by both 3 and 5
for i in range(1, 101):
    if i%3 == 0 :
        if i%5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)


#sum(list_name) returns the sum of elements in the list
#len(list_name) returns the number of elements in the list
#min(list_name)
#max(list_name)
    

my_list=[]
for i in range(10):
    my_list.append(random.randint(1,100))

print(my_list)
# print(my_list)
result = "".join(str(item) for item in my_list)
print(result)

# #shuffling a list
# random_order = []
# for i in range(len(my_list)):
#     random_order.append(random.choice(my_list))
#this can lead to repitition of the digits, simply use shuffle function
random.shuffle(my_list)
print(my_list)