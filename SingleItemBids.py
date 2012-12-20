# Erica Stockwell-Alpert
# Release 2012
# Version 1.0

#Single Item bids
import random

def SingleItem():
    # One item available
    # List of all bids, randomly generated
    # Winner is highest bid
    # Price is second highest bid
    print("Do you know how many other bidders have entered the auction?")
    print("A) yes\nB) no")
    choice = input("").lower()
    while choice != "a" and choice != "b":
        print("Invalid input. Please enter 'a' or 'b'")
        choice = input("").lower()
    if choice == "a": # User-input number of bids
        NumBids = eval(input("How many bidders have entered the auction?\n"))

    elif choice == "b": # Random number of bids
        NumBids = random.randrange(5, 100) # at least 5 bidders, at most 100

    UserBid = eval(input("How much would you like to bid?\n$"))
    
    BidList = [UserBid]
    for i in range(NumBids):# for each bidder
        bidPercent = random.randrange(1, 120) # randomly generate a value
        bid = round(UserBid * (bidPercent/100))
        # prevent a random bid from being the same as the user's bid
        while bid == UserBid:
            bidPercent = random.randrange(1, 120)
            bid = round(UserBid * (bidPercent/100))
        BidList.append(bid)

    # time to find the highest bid!
    maxBid = 0 # this will hold the value of the highest bid
    for bid in BidList:
        if bid > maxBid:
            maxBid = bid # by the last iteration, this will hold the highest value
    BidList.remove(maxBid) # take out of list so that second highest value can be found

    if maxBid == UserBid:
        print("Congratulations, you won!")
        RunnerUp = 0 # value of second highest bid
        for bid in BidList:
            if bid > RunnerUp:
                RunnerUp = bid
        payment = RunnerUp
        print("You owe $"+str(payment)+" for this item.")

    elif maxBid > UserBid:
        print("Sorry, you didn't win.")
        print("The highest bid was $"+str(maxBid))
        print("Too bad, that item was really cool too.")
        print("Better luck next time!")

    BidList.append(maxBid)

    # after bidding, show other bids (so we know it is working correctly)
    print("")
    print("Would you like to see the other bids?")
    choice = input("A) yes\nB) no\n").lower()
    if choice == "a":
        print("This was your bid: " + str(UserBid))
        print("Here were the other bids: ")
        BidList.sort()
        BidList.reverse()
        for bid in BidList:
            print("$" + str(bid))


