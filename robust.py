age = int(input("Please enter your age: "))

while(True):
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break


raise Exception("arguments")