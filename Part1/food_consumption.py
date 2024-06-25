cafeteria_frequency = int(input("How many times a week do you eat at the student cafeteria?"))
lunch_price = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week?"))
days_at_the_university = int(input("How many days were you at the university this week?"))

if days_at_the_university == 0:
   weekly = cafeteria_frequency * lunch_price + groceries

   print("Average food expenditure:")
   print(f"Weekly: {weekly} euros")

if days_at_the_university != 0:
    daily = (cafeteria_frequency * lunch_price + groceries) / days_at_the_university
    weekly = cafeteria_frequency * lunch_price + groceries

    print("Average food expenditure:")
    print(f"Weekly: {weekly} euros")
    print(f"Daily: {daily} euros")