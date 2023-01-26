# chain of node each node contain data field and refer of next node

# create individual node
class Node:
    # constructor of class whenerver we call class it will automatically 
    def __init__(self,data) -> None:# init special method initialization create new instance of class
        self.data=data              # data 
        self.refr=None              # node hase two fields
#node1=Node(10)
#print(node1)

# ll is chain of node each node are connected here

# create another class to connect above nodes
class LinkedList:
    def __init__(self) -> None:
        # ll contain head node staring poinnt of ll
        # head is null means ll is empty
        self.head=None
    # you can add diff methods to ll
    # three operation 1.add 2. remove/delete 3.traversal
    # for that you tp define 
