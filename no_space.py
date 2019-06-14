input_string = input()
count = 0
for i in input_string:
	if i.isspace() == True:
		count = count + 1
print(count)
