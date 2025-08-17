# 🧮 Simple Calculator

**Created:** 16 August 2025,the first day I stepped into the software  

**Description:** A beginner-friendly Python calculator that can perform basic arithmetic operations: addition, subtraction, multiplication, and division.

## ✨ Features

- ➕ Addition  
- ➖ Subtraction  
- ✖️ Multiplication  
- ➗ Division  
- 🐍 Simple Python project for beginners

## 🚀 How to Use

1. Run the Python file `Simple_Calculator.py`.  
2. Enter two numbers when prompted.  
3. Choose an operation (add, subtract, multiply, divide).  
4. The program will display the result.

## 💻 Code

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == '+':
    print("Result:", num1 + num2)
elif operation == '-':
    print("Result:", num1 - num2)
elif operation == '*':
    print("Result:", num1 * num2)
elif operation == '/':
    print("Result:", num1 / num2)
else:
    print("Invalid operation")
👉 [You can see the code from here](my_first_project.py)
