# custom-functions/my_functions.py

# TODO: define temperature conversion function here

# TODO: define gradebook function here

if __name__ == "__main__":

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")

#1.8C + 32 = Fahrenheit

c = 30

def celsius_to_fahrenheit(c):
    return (c*1.8 + 32)

print("--------------------")
print("THE CELSIUS TEMP IS:", c, "DEGREES")
f = celsius_to_fahrenheit(c)
print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")
    
score = 92

def numeric_to_letter_grade(score):
    if (score > 90):
        return ("A") 
    elif (score > 80):
        return ("B")
        
print("--------------------")
print("THE NUMERIC SCORE IS:", score)
grade = numeric_to_letter_grade(score)
print("THE LETTER-GRADE EQUIVALENT IS:", grade)