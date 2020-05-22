# Part 1
firstNum = float(input("Enter a number: "))
secondNum = float(input("Enter another number: "))
print("The total is", firstNum + secondNum)
# Part 2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
print("The answer is", (num1 + num2) / num3)
# Part 3
bill = float(input("What is the total price for the bill? "))
diners = int(input("How many diners are there? "))
print("Each person has to pay", '$' + str(bill / diners))
# Part 4
total = float(input("Enter an amount of days: "))
hours = total * 24
minutes = hours * 60
seconds = minutes * 60
print(total, "days is the same as:\n", hours, "hours\n", minutes, "minutes\n",
seconds, "seconds")
