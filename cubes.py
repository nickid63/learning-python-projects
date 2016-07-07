cubes = []
for cube in range(1,11):
	cubes.append(cube ** 3)
print(cubes)
cubes = list(range(1,11))
for cube in cubes:
	cubed_num = cube ** 3
	print(cubed_num)
cubes = [cube ** 3 for cube in range(1,11)]
print(cubes)
input('...')