# custom-functions/my_functions.py

# TODO: define temperature conversion function here

# TODO: define gradebook function here

#1.8C + 32 = Fahrenheit
def celsius_to_fahrenheit(celsius_temp):
    f_temp = (c*1.8 + 32)
    return f_temp

#Grade Scale
def numeric_to_letter_grade(score):
    if (score > 90):
        return ("A") 
    elif (score > 80):
        return ("B")
    else:  
        return ("C")

if __name__ == "__main__":

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")


    c = 0
    print("--------------------")
    print("THE CELSIUS TEMP IS:", c, "DEGREES")
    f = celsius_to_fahrenheit(c)
    print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")
    
    score = input("Please input a numeric letter grade (from 0 to 100): ")
    #score = float.input("Please input a numeric number")
    
    score = float(score)

    # todo: ensure the provided input value is valid before passing it into the function below

    print("--------------------")
    print("THE NUMERIC SCORE IS:", score)
    grade = numeric_to_letter_grade(score)
    print("THE LETTER-GRADE EQUIVALENT IS:", grade)