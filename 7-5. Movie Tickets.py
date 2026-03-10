total_cost = 0
num_tickets = int(input("Enter the number of tickes:"))

for i in range (1,num_tickets + 1):
    age = int(input("Enter age of ticket holder #:"))
    if age < 3: 
        price = 0
    elif 3<= age <= 12:
        price = 10
    else:
       price = 15
    total_cost += price
print(f"The total cost of the tickets for {num_tickets} tickets: ${total_cost}")