from .Node import Node as n

class LinkedList:

    # Instantiates a new linked list
    def __init__(self, item = None):
        self.startNode = None
        self.endNode = None
        self.length = 0
        if item != None:
            self.startNode = n.convertToNode(item)
            self.endNode = self.startNode
            self.length = 1

    def __str__(self):
        s = ""

        if self.length == 0:
            return s

        currentNode = self.startNode
        for i in range(self.length):
            s += str(currentNode) + ", "
            currentNode = currentNode.next
        return s[0:-2]
    
    # Function that returns a node from a given index
    def getNode(self, index: int):
        if index >= self.length or index < 0:
            raise IndexError("index %d out of range for list of length %d" % (index, self.length))
        
        if index == 0:
            return self.startNode
        
        if index == self.length - 1:
            return self.endNode
        
        if (self.length - index > index):
            currentNode = self.startNode
            while index > 0:
                currentNode = currentNode.next
                index -= 1
            return currentNode
        else:
            currentNode = self.endNode
            while index < self.length - 1:
                currentNode = currentNode.prev
                index += 1
            return currentNode
    
    # Function that reassigns the start node to the first one in the list
    # Note:  This function is useful when making changes to the order of the list,
    # as the head node may be changed.
    def reassignHead(self):
        if self.length > 0:

            # The head node should be the node with no previous, so reassign head until this node is found
            while self.startNode.prev != None:  
                self.startNode = self.startNode.prev

    def reassignTail(self):
        if self.length > 0:

            #The tail node should be the node with no next, so reassign tail until node is found
            while self.endNode.next != None:
                self.endNode = self.endNode.next

    # Procedure that inserts a node at the given index, pushing up all of
    def insert(self, item, index: int):
        if index > self.length or index < 0:
            raise IndexError("index %d out of range for list of length %d" % (index, self.length))
        
        targetNode = n.convertToNode(item)

        if self.length == 0:
            self.startNode = targetNode
            self.endNode = targetNode
        else:
            if index == 0:
                targetNode.setNext(self.startNode)
            else:
                currentNode = self.getNode(index - 1)
                nextNode = currentNode.next
                currentNode.setNext(targetNode)
                targetNode.setNext(nextNode)

            self.reassignHead()
            self.reassignTail()

        self.length += 1

    def remove(self, index: int):
        if index >= self.length or index < 0:
            raise IndexError("index %d out of range for list of length %d" % (index, self.length))
        
        if self.length == 1:
            self.startNode = None
            self.endNode = None
        else:
            if index == 0:
                self.startNode = self.startNode.next
                self.startNode.removePrev()
            elif index == self.length - 1:
                self.endNode = self.endNode.prev
                self.endNode.removeNext()
            else:
                currentNode = self.getNode(index - 1)
                targetNode: n = currentNode.next
                currentNode.setNext(targetNode.next)

        self.length -= 1

    def prepend(self, item):
        self.insert(item, 0)

    def append(self, item):
        self.insert(item, self.length)

    def insertionSort(self):

        currentNode = self.startNode
        compars = 0

        while currentNode != None:  
            #compars += 3 #three comparison
            if (currentNode.prev != None and currentNode.element < currentNode.prev.element):
                tempNode = currentNode.prev

                #determine where to place the item in the list
                while tempNode.prev != None and tempNode.prev.element > currentNode.element:
                    #compars += 2 
                    tempNode = tempNode.prev
                
                #at the current place in the list, break the connection, skipping over the current node
                placehold = currentNode.next
                currentNode.prev.setNext(currentNode.next)

                #insert node at desired slot
                currentNode.setPrev(tempNode.prev)
                currentNode.setNext(tempNode)

                currentNode = placehold
            else:
                currentNode = currentNode.next

        self.reassignHead()

        return {"compars": compars}