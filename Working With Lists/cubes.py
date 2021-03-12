#First 10 cubed numbers

cubes = [number**3 for number in range(1,11)] #List Comprehension

for cube in cubes:
    print(cube)