from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(height_feet, height_inches, weight_pounds):
    ''' This function accepts height in feet and inches, and weight in pounds as parameters.
    It calculates the BMI by converting the height to inches, applying the BMI formula,
    and returns the BMI value rounded to one decimal place. '''
    height_inches_total = (height_feet * 12) + height_inches
    bmi = (0.45 * weight_pounds) / ((height_inches_total * 0.025)**2)
    return round(bmi, 1)

def classify_bmi(bmi):
    ''' This function takes a BMI value as its parameter and classifies it into one of four
    categories based on the BMI range. It returns a string indicating the category '''
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    if request.method == 'POST':
        height_feet = int(request.form['height_feet'])
        height_inches = int(request.form['height_inches'])
        weight_pounds = int(request.form['weight_pounds'])
        bmi = calculate_bmi(height_feet, height_inches, weight_pounds)
        category = classify_bmi(bmi)
        return render_template('index.html', bmi=bmi, category=category)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)