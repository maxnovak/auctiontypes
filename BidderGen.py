#A random bidder generator that creates bidders in the form of nodes
#and returns a list of bidders, with the user's bid appended at the end

from NodeClass import *
import random


def makeBidders(numberOfBidders, usersBid, usersItems, numberOfItems):
    #creates an empty list to add new bidders to
    listOfBidders = []

    #for loop that loops through for each bidder and creates random stats for
    #him/her it uses one less than the number of bidders to keep space for the
    #users bid which will be appended at the end
    for i in range(numberOfBidders-1):
        bid = random.randrange(1,2*usersBid)
        items = random.randrange(1,numberOfItems+1)
        bidder = Node(bid, i+1, items)
        listOfBidders.append(bidder)

    #Appends the users bid and then returns the list
    listOfBidders.append(Node(usersBid, numberOfBidders, usersItems))
    return listOfBidders
        
