from replit import clear

from blind_auction_logo import logo
print(logo)

bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
    highest_amount = 0
    winner = ""
    #bidding record = {"Darshil" : 123, "Aneri" : 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]    # fetch the value from the biding record Ex. 123
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with the highest bid amount {highest_amount}")

while not bidding_finished:
    name = input("Please enter your name = ")
    bid = int(input("Please enter your bid = "))
    bids[name] = bid
    should_countinue = input("Are there any other bidders? Type 'Yes' or 'No' ").capitalize()
    if should_countinue == 'No':
        bidding_finished = True
        highest_bidder(bids)
    elif should_countinue == "Yes":
        clear()
