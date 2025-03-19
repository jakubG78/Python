def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    print("Please, remind me your name.")
    # reading a name
    print("What a great name you have, ", input(), "!", sep="")


# Now we can use these functions
greet("Bob", 2025)
remind_name()
