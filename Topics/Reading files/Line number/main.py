my_file = open('sample.txt', 'r')

num_lines = 0

for line in my_file:
	my_file.readline()
	num_lines += 1

print(num_lines)

my_file.close()