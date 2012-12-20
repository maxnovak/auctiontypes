# Max Novak
# Release 2012
# Version 1.0

#Implements the Knapsack Alg
from GreedyAlgs import *

def KnapsackAlg(listOfBidders, KnapsackCapacity):
    #Creates and empty list to hold the bidders who dont bid on over half the number
    #of items in the knapsackcapacity.
    NPrime = []
    #Goes through the listOfBidders and adds bidders with less than half the capacity
    #to NPrime and discards the rest of the bidders.
    while len(listOfBidders) != 0:
        bidder = listOfBidders.pop()
        if bidder.getItems() < (KnapsackCapacity/2):
            NPrime.append(bidder)
    #The Greedy Alg is then run on the remaining bidders to determine the winners.
    GreedyAlg(NPrime, KnapsackCapacity)
