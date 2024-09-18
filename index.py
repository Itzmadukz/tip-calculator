total_bill = int(input("What was the total bill? \n"))
tip_percentage = int(input("How much would you like to tip? 10,12, or 15? \n"))
split_ratio = int(input("How many people to split the bill?\n"))

if (split_ratio == 0):
    split_ratio = 1

split_amount = int((total_bill * (tip_percentage/100)) / split_ratio)

print(f"Each person should pay: {split_amount}")
