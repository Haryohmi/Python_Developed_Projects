print("Welcome to the tip calculator")
total_bill = int(input("what was the total bill? \n$"))
num_of_people = int(input("How many people to split the bill? \n"))
percentage_input =  int(input("What percentage tip would you like to give?(please, just add the number) \n%"))
total_payment = total_bill + (percentage_input / 100)
Payment = (total_payment / num_of_people)
final_payment = (round(Payment, 2))
final_payment = "{:.2f}".format(total_payment)
print(f"Each person should pay ${final_payment}")