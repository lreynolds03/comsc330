class NodeConstructionException(Exception):
    def __init__(self):
        super().__init__("Cannot make Node element out of Node")

class NodeNotFoundException(Exception):
    def __init__(self):
        super().__init__("Node does not exist")

class Node:
    
    # Makes a bidirectional node, used for LinkedList class
    def __init__(self, element):
        if type(element) == Node:
            raise NodeConstructionException

        self.next = None
        self.prev = None
        self.element = element

    def __str__(self):
        return str(self.element)
    
    def setElement(self, element):
        if type(element) == Node:
            raise NodeConstructionException
        
        self.element = element
    
    # Function that wraps the given item in a node, if it is not already a node
    def convertToNode(item):
        if type(item) != Node:
            item = Node(item)
        return item
    
    # Procedure that sets the next pointer of this node
    def setNext(self, item):
        self.next = None    #If item is none, should point to none
        if item != None:    #If item is not none, create two way connection between these nodes
            item = Node.convertToNode(item) #Ensure that this item is a node
            self.next = item
            item.prev = self

    # Procedure that sets the previous pointer of this node
    def setPrev(self, item):
        self.prev = None    #If item is none, should point to none
        if item != None:    #If item is not none, create two way connection between these nodes
            item = Node.convertToNode(item) #Ensure that this item is a node
            self.prev = item
            item.next = self
        
    # Procedure that removes the pointers between this node and its following node
    def removeNext(self):
        if self.next != None:   #If this node points to nothing, don't need to do anything
            nextNode: Node = self.next
            nextNode.prev = None    #Remove pointers
            self.next = None

    # Procedure that removes the pointers between this node and its previous node
    def removePrev(self):
        if self.prev != None:   #If this node points to nothing, don't need to do anything
            prevNode: Node = self.prev
            prevNode.next = None    #Remove pointers
            self.prev = None

    # Procedure that swaps this node with its next node
    def swapNext(self):
        try:
            x = self.element
            self.element = self.next.element
            self.next.element = x
        except AttributeError:
            raise NodeNotFoundException

    # Procedure that swaps this node with its previous node
    def swapPrev(self):
        try:
            x = self.element
            self.element = self.prev.element
            self.prev.element = x
        except AttributeError:
            raise NodeNotFoundException