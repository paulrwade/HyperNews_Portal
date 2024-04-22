def tallest_people(**kwargs):

	max_height = max(kwargs.values())

	sorted_dict = sorted(kwargs.items())

	for key, value in sorted_dict:
		if value == max_height:
			print(key, ":", value)

# tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)
