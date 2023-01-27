class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None


# class for linking nodes

class LinkedList:
    def __init__(self):
        self.head=None


    # traversal of linked list
    #1. empty or not
    def printll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref


    # add node at begin of linked list
    def add_begin(self,data):
        # node class creaete new node
        new_node=Node(data) #node with data and reference None
        new_node.ref=self.head
        self.head=new_node


LL1=LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.printll()



# below program add node at end of linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None


# class for linking nodes

class LinkedList:
    def __init__(self):
        self.head=None


    # traversal of linked list
    #1. empty or not
    def printll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.ref


    # add node at begin of linked list
    def add_begin(self,data):
        # node class creaete new node
        new_node=Node(data) #node with data and reference None
        new_node.ref=self.head
        self.head=new_node

    # add node at d end of linked list
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
            


LL1=LinkedList()
LL1.add_begin(10)
LL1.add_end(100)
LL1.add_begin(20)
LL1.printll()





 # create linked list

class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.ref=None

# linked each node to other node initial linkedlist
class LinkedList:
    def __init__(self) -> None:
        self.head=None

    # traversal list
    def traversal(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end="-->")
                n=n.ref

    # add element in linked list
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node


    # add node at d end of linked list
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node


    # add node after given node
    def add_after(self,data,x):
        n=self.head

        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("\nNode is not present in ll")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is  empty")
            return

        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return

        n=self.head

        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref

        if n.ref is None:
            print("Node is not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node


LL1=LinkedList()
LL1.add_before(10,100)
LL1.traversal()


