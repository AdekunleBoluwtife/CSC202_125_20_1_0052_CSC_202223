#This_donation_project_is_based_off_the_tip_calculator_projet_off_day_2
print("Hello and welcome to the Food.co orphange donation calculator")
bill = float(input("What was the total bill?"))
donation = int(input("How much money would you like to donate? 10, 20, or 30"))
people = int(input("How many people to split the bill?"))
donation_as_percent = donation / 100
total_donation_amount = bill * donation_as_percent
total_bill = bill + total_donation_amount
bill_per_person = total_bill / people
final_amount= round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")
print("Thank you for patronization and donation")


