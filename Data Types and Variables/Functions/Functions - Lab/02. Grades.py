def get_grade(number=2):
    #number = float(input())

    if number < 2 or number > 6:
        return "Invalid"
    elif 2 <= number <= 2.99:
        return "Fail"
    elif number <= 3.49:
        return "Poor"
    elif number <= 4.49:
        return "Good"
    elif number <= 5.49:
        return "Very Good"
    elif number <= 6:
        return "Excellent"


print(get_grade(3))
