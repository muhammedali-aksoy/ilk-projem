#Get numbers from user
number1=float(input("Enter the first number:"))
number2=float(input("Enter the second number:"))
#Ask which operation to perform
operation=input("Choose an operation(+,-,*,/):")
#Perform the operation
if operation=="+":
	result=number1+number2
elif operation=="-":
	result=number1-number2
elif operation=="*":
	result=number1*number2
elif operation=="/":
	result=number1/number2
else:
	result="Invalid operation!"
#Show the result
print("Result:",result)