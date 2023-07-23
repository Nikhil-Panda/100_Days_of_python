val = 4474838_9738782.74837
print(val)
# "_" in integer types are ignored 

street_name = "Abbey Road"
print(street_name[4] + street_name[7])
# spaces considered as characters in string datatype

print(type(len("Hello")))
#keep an eye for type errors and solve them by setting the correct datatypes
#int(), float(), str(), type() functions to set the datatypes straight

#PEMDASLR - priority order
print(3 * 3 + 3 / 3 - 3)

# rounding off
print(round(8/3,2))
print(8//3)
# "//" - floor division operator


# fstrings
score = 100
height = 1.8
isWinning = True
# print(f"your score is {score}, your height is {height},\nare you winning?: {isWinning}")

#format function
print("{:.2f}".format(886/3))
#{:.2f} describes that the value in the format() field will be formatted to 2 values 

print("{0:.{1}f}".format(886/3, 3))
#here it is mentioned that {0:.{1}f} : here 0 is replaced by the first value in format() field
#and {1} is replaced by the following value



