with open("animals.txt", "r", encoding="utf-8") as animals_file:

	for animal in animals_file:

		animal = str.strip(animal)

		with open("animals_new.txt", "a", encoding="utf-8") as animals_new:

			animals_new.write(animal + " ")
			animals_new.close()

	animals_file.close()
