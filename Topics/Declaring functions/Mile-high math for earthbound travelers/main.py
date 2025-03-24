# Function to convert miles to kilometers

def miles_to_kilometers(miles):
    return round(miles * 1.60934, 2)


# Main program
if __name__ == "__main__":
    miles = float(input())
    result = miles_to_kilometers(miles)
    print(f"{result:.2f}")
