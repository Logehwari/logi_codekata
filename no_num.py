input_string = input()
count = 0
for i in input_string:
	if i.isdigit() == True:
		count = count + 1

print(count)
