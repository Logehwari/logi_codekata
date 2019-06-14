input_string = input()
count = 0
for i in input_string:
	if i.isdigit() == False and i.isalpha() == False and i.isspace() == False:
		count = count + 1

print(count)
