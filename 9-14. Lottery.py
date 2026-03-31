import random
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
winning_numbers = random.sample(lottery_pool[:10], 4)
winning_letter = random.choice(lottery_pool[10:])
winning_ticket = f"{winning_numbers} {winning_letter}"
user_input = input("Enter your ticket (4 numbers and 1 letter)")
if user_input == winning_ticket:
    print(f"Congratulations! {user_input} is a winning ticket!")
else:
    print(f"Sorry you didn't win this time. The winning ticket was: {winning_ticket}")
