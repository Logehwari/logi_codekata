day = input().lower()
if( day == "saturday" or day == "sunday" ):
  print("yes")
elif( day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday" ):
  print("no")
else:
  print("invalid")
