print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
threeReminder = int(input())
fiveReminder = int(input())
sevenReminder = int(input())
age = (threeReminder * 70 + fiveReminder * 21 + sevenReminder * 15) % 105
print("Your age is ", age, "; that's a good time to start programming!", sep="")
