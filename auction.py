from ascii_art import logo

print(logo)
print("Welcome to the secret auction program.")

bids_dict = {}
add_new_bid = True
blank_screen = "\n" * 20

while add_new_bid:

    name = input("What is your name?: ")

    while True:
        try:
            bid = int(input("What is your bid?: $"))
        except:
            print("This is not a number, try again")
        else:
            break

    bids_dict[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    while True:
        if not (other_bidders == 'yes' or other_bidders == 'no'):
            other_bidders = input("This is not an answer I was expecting. Type 'yes' or 'no': ").lower()
        else:
            break

    if other_bidders == 'no':
        add_new_bid = False

    print(blank_screen)

max_bidder = max(bids_dict, key = lambda x: bids_dict[x])

print(f"The winner is {max_bidder} with a bid of ${bids_dict[max_bidder]}")