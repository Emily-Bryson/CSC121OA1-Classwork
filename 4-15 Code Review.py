threes = list(range(3, 31, 3))
for number in threes:
    print(number)
cubes = [value**3 for value in range (1, 11)]
for cube in cubes:
    print(cube)
million_number = list(range(1, 1000001))
print(min(million_number))
print(max(million_number))
total_sum = sum(million_number)
print(f"Total sum: {total_sum}")