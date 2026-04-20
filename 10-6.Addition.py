print("Enter two numbers to add them together.")
first_number = input("First number: ")
second_number = input("Second number: ")
try:
    result = int(first_number) + int(second_number)
    print(f"The sum is: {result}")
except ValueError:
    print("Error: Please enter numerical values only.")