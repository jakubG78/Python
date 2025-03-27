import math

# write your code here
principal = float(input("Enter the loan principal:\n"))
print("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:""")
user_choice = input()
if user_choice == "m":
    monthly_payment = float(input("Enter the monthly payment:\n"))
    print("It will take ", int(math.ceil(principal / monthly_payment)), " months to repay the loan", )
elif user_choice == "p":
    periods = int(input("Enter the number of months:\n"))
    print()
    if principal % periods == 0:
        print(f"Your monthly payment = {int(principal // periods)}")
    else:
        payment_average = math.ceil(principal / periods)
        payment_last = principal - (periods - 1) * payment_average
        print(f"Your monthly payment = {payment_average} and the last payment = {int(payment_last)}.")
