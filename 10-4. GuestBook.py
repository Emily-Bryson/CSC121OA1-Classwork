filename = 'guest_book.txt'
print("Enter 'quit' when finished.")
while True:
    name = input("\nPlease enter your name:")  
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print(f"Hello {name}, you've been added to the guest book.")

                                            