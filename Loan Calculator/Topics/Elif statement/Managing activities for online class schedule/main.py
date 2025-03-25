# The program starts here

def activity(day):
    # Use elif to set conditions for days of the week
    # Remember, the days are represented as follows:
    # 0 to 4 for Monday to Friday respectively
    # 5 for Saturday
    # 6 for Sunday

    if day < 5:
        return 'Study!'
    elif day == 5:
        return 'Rest!'
    else:
        return 'Leisure!'


# Do not change anything below!

day = int(input())
print(activity(day))
