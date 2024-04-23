#  write your code here 
my_file = open("/users/paulwade/hs_data.txt", "r", encoding="utf-8")

summer_count = 0

for line in my_file:
	if line == "summer\n":
		summer_count += 1

print(summer_count)
