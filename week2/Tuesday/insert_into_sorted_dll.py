class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"{self.data}"


def sortedInsert(head, data):
    # Create a new node with value of data.
    # Check if the head of the Linked list is None.

        # If the head is None, then the new node will become the head and the tail and sortedInsert will return a sorted linked list of length 1.

    # Compare the value of the new node to the value of the linked list's head:

        # If the value of the new node < the value of the head node, then then new node will become the new head and the old head will become the next node of the new head.

        # If the value of the new node > the value of the head node, then implement a traversal as long as the value of the next node is not None. And we will compare the value of the new node to the value of the current node.

        # If we get to None then the new node becomes the tail and the old tail will have the next pointer updated to the new tail, and the new tail prev pointer will point to the new tail.

        # If we find a value Greater than the new node before reaching None, then will update the next pointer of the prev node before the current node to point to the new node update the prev pointer of the new node to point to the prev node of the current node, then the next pointer of the new node will be updated to point to the value of the current node. Finally, the prev pointer of the current node will be updated to point to the new node.

        # If the value of the new node == to the value of any node in the Linked list then will just return to avoid creating duplicates.

    node = DoublyLinkedListNode(data)
    current = head
    if data < node.data:
        node.next = head
        head.prev = node
        head = node
        return head
    while current is not None:
        if data < current.data:
            node.next = current
            node.prev = current.prev
            current.prev.next = node
            current.prev = node
            break

        elif current.next is None:
            node.next = None
            node.prev = current
            current.next = node
            break

        current = current.next
    return head
