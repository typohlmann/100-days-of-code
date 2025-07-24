print("Welcome to the tip calculator")

bill_cost = float(input("What was the total bill? "))
tip_amount = int(input("What percentage tip would you like to leave? ")) / 100
amount_of_people = int(input("How many people to split the bill? "))

total_bill = bill_cost + tip_amount 
amount_per_person = round((total_bill) / (amount_of_people), 2)

print(f"Each person should pay: {amount_per_person}")