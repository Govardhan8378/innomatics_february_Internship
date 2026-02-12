messages = ["Hi", "Welcome to the platform", "OK"]

for i in messages:
    length = len(i)
    print("Message:", i)
    print("Length:", length)
    
    if length > 10:
        print("Long Message (More than 10 characters)")
    else:
        print("Short Message")
    
    
