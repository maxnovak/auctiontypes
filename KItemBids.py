#K-item bids
import random

def K_Items():
    #K identical items
    
    K = eval(input("Please select a value for K between 2 and 99\n"))
    while K < 2 or K > 99: # error check
        print("Invalid input. Please try again.")
        K = eval(input("Please select a value for K between 2 and 99\n"))
    print("There are "+str(K)+" identical items available.")
    print("Each bidder can only win a maximum of one item.")
    print("Each winner will pay the price bid by the first losing bidder.")
    NumBids = random.randrange((K+1), (2*K)) # random number of bidders > K
    #What is your bid?
    UserBid = eval(input("How much would you like to bid?\n"))
    BidList = [UserBid]
    for i in range(NumBids):# Generate a list of random bids
        bid = random.randrange(1, 2*UserBid)
        while bid == UserBid:
            bid = random.randrange(1, 2*UserBid)
        BidList.append(bid)
    # Sort list
    BidList.sort()
    BidList.reverse()
    WinnerList = []
    for i in range(K): # number of winner = number of items
        winner = BidList[0]
        BidList.remove(winner)
        WinnerList.append(winner)

    # Determine price
        # Highest bidder remaining in BidList is the first loser

    Price = BidList[0]
    
    if UserBid in WinnerList:
        print("Congratulations! You are a winner!")
        
        
    else:
        print("Sorry, you are not a winner.")
        print("Shouldn't have been so stingy, I guess.")

    print("These are the winning bids:")
    for bid in WinnerList:
        print(bid)
    print("The cost of each item is " + str(Price))
    print("")
    print("Would you like to see the other bids?")
    print("A) Yes\nB) No")
    choice = input("").lower()
    if choice == "a":
        for bid in WinnerList:
            print(bid)
        for bid in BidList:
            print(bid)

    print("Press the enter key to return to the main menu")
    menu = input("")
    main()
