"""
Problem: Given a sorted linked list, delete all duplicates such that each element appears only once.
Sample Input: 1 -> 1 -> 2 -> 3 -> 3
Sample Output: 1 -> 2 -> 3
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
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end='')
            if temp.next is not None:
                print(' -> ', end='')
            temp = temp.next
        print('\n')

    def remove_duplicate(self):
        first = self.head
        second = self.head
        while second:
            if first.value == second.value:
                first.next = second.next
                second.next = None
                second = first.next
                self.length -= 1
            else:
                first = first.next
                second = second.next


linked_list = Linkedlist()
linked_list.append(1)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(4)
linked_list.append(5)
print("Linked List")
linked_list.print_list()
linked_list.remove_duplicate()
print("After removing duplicates")
linked_list.print_list()

