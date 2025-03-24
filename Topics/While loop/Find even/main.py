def is_even(number):
    return number % 2 == 0


n = int(input())
curent_number = 1

while curent_number < n:
    if is_even(curent_number):
        print(curent_number)
    curent_number += 1
