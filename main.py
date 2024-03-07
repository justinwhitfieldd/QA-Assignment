def calculate_bmi(height_feet, height_inches, weight_pounds):
    '''
    This function accepts height in feet and inches, and weight in pounds as parameters. 
    It calculates the BMI by converting the height to inches, applying the BMI formula, 
    and returns the BMI value rounded to one decimal place.
    '''
    height_inches_total = (height_feet * 12) + height_inches
    bmi = (703 * weight_pounds) / (height_inches_total ** 2)
    return round(bmi, 1)

def classify_bmi(bmi):
    '''
    This function takes a BMI value as its parameter and classifies it into one of four 
    categories based on the BMI range. It returns a string indicating the category
    '''
    if bmi < 18.5:
        return "Underweight"
    elif 18.4 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator")
    height_feet = int(input("Enter your height (feet): "))
    height_inches = int(input("Enter your height (inches): "))
    weight_pounds = int(input("Enter your weight (pounds): "))
    bmi = calculate_bmi(height_feet, height_inches, weight_pounds)
    category = classify_bmi(bmi)
    print(f"Your BMI is {bmi}, which is considered {category}.")

if __name__ == '__main__':
    main()
