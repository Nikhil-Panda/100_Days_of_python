
num1, num2 = map(str,input().split(","))
#comma-seperated integers as input
res = list(num1) + list(num2)

#interlacing integers
res[::2] = num1
res[1::2] = num2
print(res)
# print(type(res))
# final_number = "".join(str(i) for i in res)
finalNum = int("".join(str(i) for i in res))
print(finalNum)
print(type(finalNum))



#map() -> map(function, *iterables)
#any no.of inputs can be taken
#map function can be used to take space seperated integers or output as per our requirement

# print(num1,num2)
# print(type(num1))
