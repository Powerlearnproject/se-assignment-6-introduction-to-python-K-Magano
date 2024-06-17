#  3. Python Syntax and Semantics:

print("Hello, World!")

# Explanation:


# 4. Data Types and Variables: 

# Integer
age = 25
print(f"My age is {age}")  # f-string for formatted output

# Float
pi = 3.14159
print(f"Pi is approximately {pi:.4f}")  # Format to 4 decimal places


# Conditional Statements (if-else):


age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# Loops (for loop):

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}.")

# Example Function:

def add_numbers(x, y):
    # """This function adds two numbers and returns the sum."""
    sum = x + y
    return sum

# Call the function
result = add_numbers(5, 3)
print(f"The sum of 5 and 3 is {result}.")


# 7. Lists and Dictionaries
numbers = [1, 5, 9, 2, 7]

# Accessing elements by index
first_number = numbers[0]  # Accesses the first element (1)
print(f"The first number is {first_number}.")

# Modifying elements
numbers[2] = 3  # Changes the third element (9) to 3
print(numbers)  # Output: [1, 5, 3, 2, 7]

# Dictionary with key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values by key
age = person["age"]
print(f"{person['name']} is {age} years old.")

# Adding a new key-value pair
person["occupation"] = "Software Engineer"
print(person)  

# Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'occupation': 'Software Engineer'}

# 8. Exception Handling

def calculate_average(numbers):
    try:
      
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except ZeroDivisionError:  # Catch specific exception
        print("Error: Cannot divide by zero.")
    finally:
        print("Calculation completed.")

# Example usage
try:
    result = calculate_average([2, 4, 0])  # Division by zero
    print(f"The average is {result:.2f}.")  # Won't execute due to exception
except ZeroDivisionError:
    print("Handled division by zero error in main program.")

# Writing to Files:

def write_to_file(filename, data):
    try:
        # Open the file in append mode
        with open(filename, 'a') as file:
            # Write each string in the list to the file
            for item in data:
                file.write(f"{item}\n")  # Add newline after each item
        print(f"Successfully wrote data to '{filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Creating a new one.")
        # You can optionally create a new file here (use 'w' mode)


data_to_write = ["This is line 1", "This is line 2"]
write_to_file("my_data.txt", data_to_write)

    