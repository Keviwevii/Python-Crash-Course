#Conditional Tests that check for equality or inequality

feeling = 'happy'
print("Is feeling == 'happy'? I predict True.")
print(feeling == 'happy')

print("Is feeling == 'sad'? I predict False.")
print(feeling == 'sad')

sample_car = 'BMW'
print(sample_car.lower() == 'bmw')

#Numerical Tests

print(3 > 2) #True
print(3 < 2) #False
print(50 >= 3) #True
print(50 <= 3) #False
print(50 > 3 and 40 < 100) #True
print(50 < 2 or 50 < 250) #True

#Using in and not in to check for certain strings in a list
sample_list = ['red', 'blue', 'green']

print('red' in sample_list) #True
print('yellow' in sample_list) #False
print('gray' not in sample_list) #True
print('red' not in sample_list) #False