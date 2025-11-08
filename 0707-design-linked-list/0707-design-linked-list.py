class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size = 0                                   # Set the Initial Size of the Linked List to 0
        self.head = ListNode(0)                         # Add a Sentinel Node

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:             # If index > size of the Linked List, you cannot traverse and get the expected value
            return -1

        curr = self.head                                # Assign Head to a node/variable to traverse
        for _ in range(index+1):                        # Traverse till the expected index
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)                         # Use Add At Index Function with index value 0

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)                 # Use Add At Index Function with index as the size of the Linked List

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:                           # If index is greater than size of LinekdList, you can't add
            return
        
        if index < 0:                                   # If the index is negative, add the new node at the start
            index = 0
        
        self.size += 1
        pred = self.head                                # Find the predecessor node
        for _ in range(index):
            pred = pred.next

        new_node = ListNode(val)                        # Define the new node to add

        new_node.next = pred.next                       # Assign the next of the new node to predecessor's next
        pred.next = new_node                            # Change the predecessor's next to new node 

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size:                           # If index is greater than size of LinekdList, you can't add
            return
        
        if index < 0:                                   # If the index is negative, add the new node at the start
            index = 0

        self.size -= 1
        pred = self.head                                # Find the predecessor node
        for _ in range(index):
            pred = pred.next

        pred.next = pred.next.next                      # Assign the Predecessor's next to Predecessor's next to next, ultimately unlinking the middle node


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)