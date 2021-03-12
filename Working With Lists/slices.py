#Slicing through or threes list

threes = [number for number in range(3,31,3)]

first_three = threes[:3] 
middle_three = threes[4:7]
last_three = threes[-3:]

print('The first 3 multiples of 3 are:') 
print(first_three)

print('The middle 3 multiples of 3 are: ')
print(middle_three)

print('The last 3 multiples of 3 are: ')
print(last_three)
