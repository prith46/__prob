"""
Problem: Given a non-empty, singly linked list with head node head, return a middle node of the linked list.
Sample Input: 1 -> 2 -> 3 -> 4 -> 5
Sample Output: 3
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def middle_element(self):
        fast = self.head
        slow = self.head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
        return slow.value
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end='')
            if temp.next is not None:
                print(' -> ', end='')
            temp = temp.next
        print('\n')


linked_list = Linkedlist()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
print(linked_list.middle_element())
