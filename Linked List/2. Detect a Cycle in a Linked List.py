"""
Problem: Given a linked list, determine if it has a cycle in it. A cycle means the linked list loops back to
a previous node.
Sample Input: 3 -> 2 -> 0 -> -4 (with tail connecting to the second node)
Sample Output: true
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
            if temp:
                print(' -> ', end='')
        print('\n')

    def make_loop(self):
        self.tail.next = self.head.next.next

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            fast = fast.next
            slow = slow.next
            if fast.next is None:
                return False
            fast = fast.next
            if slow == fast:
                return True


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(3)
linked_list.append(4)
linked_list.append(6)
linked_list.append(12)
linked_list.append(9)
linked_list.print_list()
linked_list.make_loop()
if linked_list.detect_cycle():
    print("Loop is found")
else:
    print("No Loop is found")
