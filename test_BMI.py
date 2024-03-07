from main import calculate_bmi, classify_bmi
# Test the classify_bmi function

# Test ability to correctly classify BMI as "Underweight"
def test_classify_bmi_underweight():
    assert classify_bmi(18.4) == "Underweight"
# Test lower boundary for "Normal weight" classification
def test_classify_bmi_normal_weight_lower_boundary():
    assert classify_bmi(18.5) == "Normal weight"
# Test upper boundary for "Normal weight" classification
def test_classify_bmi_normal_weight_upper_boundary():
    assert classify_bmi(24.9) == "Normal weight"
# Test lower boundary for "Overweight" classification
def test_classify_bmi_overweight_lower_boundary():
    assert classify_bmi(25) == "Overweight"
# Test upper boundary for "Overweight" classification
def test_classify_bmi_overweight_upper_boundary():
    assert classify_bmi(29.9) == "Overweight"
# Test ability to correctly classify BMI as "Obese"
def test_classify_bmi_obese():
    assert classify_bmi(30) == "Obese"

# Test the calculate_bmi
# Test with a basic set of inputs for normal BMI calculation
def test_calculate_bmi_basic():
    assert calculate_bmi(6, 0, 180) == 24.4
# Test with boundary conditions to ensure it handles extreme cases
def test_calculate_bmi_boundary():
    assert calculate_bmi(2, 0, 50) > 0  # Extremely short and light
    assert calculate_bmi(7, 0, 300) > 0  # Extremely tall and heavy
# Test ability to round the BMI value to one decimal place
def test_calculate_bmi_decimal_precision():
    assert calculate_bmi(5, 10, 172) == 24.7

# Test both functions together
# Integrated tests: calculating BMI to classifying it for the "Underweight" category
def test_bmi_underweight():
    assert classify_bmi(calculate_bmi(5, 2, 100)) == "Underweight"
# Integrated tests: calculating BMI to classifying it for the "Normal weight" category
def test_bmi_normal_weight():
    assert classify_bmi(calculate_bmi(5, 9, 145)) == "Normal weight"
# Integrated tests: calculating BMI to classifying it for the "Overweight" category
def test_bmi_overweight():
    assert classify_bmi(calculate_bmi(5, 6, 180)) == "Overweight"
# Integrated tests: calculating BMI to classifying it for the "Obese" category
def test_bmi_obese():
    assert classify_bmi(calculate_bmi(5, 3, 200)) == "Obese"
