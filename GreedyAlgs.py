from NodeClass import *
import random



def NaiveGreedyAlgOne(bidders, numberOfItems):
    #sorts the bidders in order of greatest value
    sortBidders = sorted(bidders, key=lambda node: node.getValue())
    currentTotalNumOfItems = 0#Counter for number of items that can be sold
    topBidder = sortBidders.pop()#pops off top node
    print("The following bidders are winners:")
    #cycles through the sorted bids and until the items are gone or the list
    #of bidders is empty adding them to the list of winners
    while currentTotalNumOfItems+topBidder.getItems() <= numberOfItems and len(sortBidders) != 0:
        print("Bidder Number:", topBidder.getBidder())
        currentTotalNumOfItems = currentTotalNumOfItems + topBidder.getItems()
        topBidder = sortBidders.pop()
    print("Number of items bid on:", numberOfItems)
    print("Number of items bidders won:", currentTotalNumOfItems)
    #Uses the last bidder, who did not get added to the list, as the price
    print("And they will pay the price: $", topBidder.getValue())

def NaiveGreedyAlgTwo(bidders, numberOfItems):
    #sorts the bidders in order of bundle size and then reverses it
    #so that the smallest is on top
    sortBidders = sorted(bidders, key=lambda node: node.getItems())
    sortBidders.reverse()
    currentTotalNumOfItems = 0#Counter for number of items that can be sold
    topBidder = sortBidders.pop()#pops off top node
    print("The following bidders are winners:")
    #cycles through the sorted bids and until the items are gone or the list
    #of bidders is empty adding them to the list of winners
    while currentTotalNumOfItems+topBidder.getItems() <= numberOfItems and len(sortBidders) != 0:
        print("Bidder Number:", topBidder.getBidder())
        currentTotalNumOfItems = currentTotalNumOfItems + topBidder.getItems()
        topBidder = sortBidders.pop()
    print("Number of items bid on:", numberOfItems)
    print("Number of items bidders won:", currentTotalNumOfItems)
    #Uses the last bidder, who did not get added to the list, as the price
    print("And they will pay the price: $", topBidder.getValue())

def GreedyAlg(bidders, numberOfItems):
    #sorts the bidders in order of value per number of items
    sortBidders = sorted(bidders, key=lambda node: node.getValuePerItems())
    currentTotalNumOfItems = 0
    winners = []
    losers = []
    #Loops through the bidders and creates a list of winners and losers
    for i in range(len(sortBidders)):
        topBidder = sortBidders.pop()
        if currentTotalNumOfItems+topBidder.getItems() <= numberOfItems:
            currentTotalNumOfItems += topBidder.getItems()
            winners.append(topBidder)
        else:
            losers.append(topBidder)
    #Losers are then sorted so that the greatest value / item is on top
    sortLosers = sorted(losers, key=lambda node: node.getValuePerItems())

    print("The following bidders are winners:")
    #The winners are then listed and the top loser's price is used for the price
    #of the winners bids
    while len(winners) != 0:
        topWinner = winners.pop()
        print("Bidder Number:", topWinner.getBidder())
    print("Number of items bid on:", numberOfItems)
    print("Number of items bidders won:", currentTotalNumOfItems)
    if len(sortLosers) != 0:
        print("And they will pay the price per item: $", sortLosers.pop().getValuePerItems())
    #incase there are no losers the price is set to the value of the last winner
    else:
        print("And they will pay the price per item: $", topWinner.getValuePerItems())

'''
def main():
    bidder1 = Node(101,1,15)
    bidder2 = Node(5,2,1)
    bidder3 = Node(100,3,10)
    numberOfItems = 20

    listOfBidders = [bidder1, bidder2, bidder3]

    NaiveGreedyAlgOne(listOfBidders)
    NaiveGreedyAlgTwo(listOfBidders)
    GreedyAlg(listOfBidders)
    
'''

    

    
        

        
