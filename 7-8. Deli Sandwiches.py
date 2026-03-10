sandwich_orders = ['tuna', 'roast beef', 'chicken', 'Italian BMT', 'BLT']
finished_sandwiches =[]
while sandwich_orders:
    sandwich_now = sandwich_orders.pop(0)
    print(f"I made your  {sandwich_now}  sandwich.")
    finished_sandwiches.append(sandwich_now)
    print(f"Sandwiches that were made:") 
    for sandwich in finished_sandwiches:
        print(sandwich + " sandwich")
