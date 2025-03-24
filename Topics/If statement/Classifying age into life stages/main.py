# Read the user's age
age = int(input())

# Check the age and print the corresponding category
if 18 <= age <= 65:
    print("Adult")
else:
    if age < 18:
        print("Minor")
    else:
        print("Senior")
