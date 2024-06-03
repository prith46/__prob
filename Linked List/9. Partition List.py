"""
Problem: Given a linked list and a value x, partition it such that all nodes less than x come before nodes
greater than or equal to x.
Sample Input: 1 -> 4 -> 3 -> 2 -> 5 -> 2, x = 3
Sample Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5
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
            self.tail.next = None
        self.length += 1
        return True

    def partition(self, value):
        lesser = LinkedList()
        greater = LinkedList()
        temp = self.head
        while temp is not None:
            if temp.value < value:
                lesser.append(temp.value)
            else:
                greater.append(temp.value)
            temp = temp.next
        lesser.tail.next = greater.head
        return lesser.head


def print_list(temp):
    while temp is not None:
        print(temp.value, end='')
        if temp.next is not None:
            print('->', end='')
        temp = temp.next
    print('\n')


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(4)
linked_list.append(3)
linked_list.append(2)
linked_list.append(5)
linked_list.append(2)
print("Linked List: ")
print_list(linked_list.head)
partition_list = linked_list.partition(3)
print("After Partition: ")
print_list(partition_list)
