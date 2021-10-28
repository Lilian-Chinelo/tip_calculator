print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? : $"))
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? :")
number_of_people = input("How many people to split the bill? :")
percentage_tip = int(percentage_tip) / 100

tip_per_person = total_bill * percentage_tip
total = tip_per_person + total_bill
amount_to_pay = round(total / int(number_of_people), 2)
print(f"Each person should pay: ${amount_to_pay}")
input('Press ENTER to exit')

