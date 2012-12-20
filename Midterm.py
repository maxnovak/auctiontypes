# Erica Stockwell-Alpert and Max Novak
# Midterm Project
import random
from NodeClass import *
from BidderGen import *
from KItemBids import *
from SingleItemBids import *
from GreedyAlgs import *
from KnapsackAlg import *
        
def main():
    print("Welcome to the Auction Generator 4000")
    print("Please enter the letter of your selection from the following options: ")
    print("A) Single Item Auction\nB) Combinatorial Auction")
    choice = input("").lower()
    while choice != "a" and choice != "b": # Error correcting: user does not pick on of the choices
        print("Invalid choice. Please try again")
        choice = input("").lower() # repeat until valid selection is made
        
    if choice == "a": # selected Single Item auction
        print("What type of Single Item Auction would you like to run?")
        print("A) One item\nB) K identical items")
        auction = input("").lower()
        while auction != "a" and auction != "b":
            print("Invalid choice. Please try again")
            auction = input("").lower()

        if auction == "a": # run One-Item Auction
            print("You have selected: SINGLE ITEM AUCTION.")
            print("There is one item available to be bid on. \nIt is super great. \nYou want to win it.")
            print("You will win if you have the highest bid.")
            print("If you win, you will pay the price bid by the second-highest bidder.")
            print("") # space between intro and beginning
            SingleItem()

        elif auction == "b": # run K-items auction
            print("You have selected the K-ITEMS AUCTION.")
            K_Items()
        
    elif choice == "b": # combinatorial auctions
        print("What type of Combinatorial Auction would you like to run?")
        print("A) Knapsack Auction\nB) NGA1\nC) NGA2\nD) GA\nE) Fixed Price")
        auction = input("").lower()
        while auction != "a" and auction != "b" and auction != "c" and auction != "d" and auction != "e":
            print("Invalid choice. Please try again")
            auction = input("").lower()

        print("Do you know how many other bidders have entered the auction\n and how many items are in the auction?")
        print("A) Yes\nB) No")
        choice = input("").lower()
        while choice != "a" and choice != "b":
            print("Invalid input. Please enter 'a' or 'b'")
            choice = input("").lower()

        if choice == "a": # User-input number of bids
            print("How many bidders are in this auction?")
            bidders = eval(input(""))
            print("How many items are there in this auction?")
            numberOfItems = eval(input(""))

        elif choice == "b": # Random number of bids
            bidders = random.randrange(5,100)
        
        print("How much would you like to bid?")
        bidAmount = eval(input(""))
        print("On how many items?")
        usersItems = eval(input(""))

        #Tells the user what number they are
        print("You are bidder number:", bidders)

        #Creates a random number of items based on the number of items the user is bidding on 
        if choice == "b":
            numberOfItems = random.randrange(usersItems,usersItems*4)

        if auction == "a":
            #Creates a list of random bidders and has the users bid at the end
            listOfBidders = makeBidders(bidders, bidAmount, usersItems, numberOfItems)
            #Runs Knapsack Alg on the list of bidders
            KnapsackAlg(listOfBidders, numberOfItems)        
            
        elif auction == "b":
            #Creates a list of random bidders and has the users bid at the end
            listOfBidders = makeBidders(bidders, bidAmount, usersItems, numberOfItems)
            #Runs Naive Greedy Alg #1 on the list of bidders
            NaiveGreedyAlgOne(listOfBidders, numberOfItems)


        elif auction == "c":
            #Creates a list of random bidders and has the users bid at the end
            listOfBidders = makeBidders(bidders, bidAmount, usersItems, numberOfItems)
            #Runs Naive Greedy Alg #2 on the list of bidders
            NaiveGreedyAlgTwo(listOfBidders, numberOfItems)

        elif auction == "d":
            #Creates a list of random bidders and has the users bid at the end
            listOfBidders = makeBidders(bidders, bidAmount, usersItems, numberOfItems)
            #Runs Greedy Alg on the list of bidders
            GreedyAlg(listOfBidders, numberOfItems)

    print("Press the enter key to return to the main menu")
    menu = input("")
    main()

main()
