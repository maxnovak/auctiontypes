#Nodes Class
class Node:
    #When called will create a new Node with the bidders information
    def __init__(self, value, bidder, items):
        self.value = value
        self.bidder = bidder
        self.items = items
        self.valuePerItems = value/items

    #Getter for value of the bid
    def getValue(self):
        return self.value

    #Getter for bidder's number
    def getBidder(self):
        return self.bidder

    #Getter for number of items bid on
    def getItems(self):
        return self.items

    #Getter for value / number of items
    def getValuePerItems(self):
        return self.valuePerItems

'''  
def main():
    print("start")
    test = Node(100, 1, 10)
    
    print(test.getValue())
    print(test.getBidder())
    print(test.getItems())

''' 



