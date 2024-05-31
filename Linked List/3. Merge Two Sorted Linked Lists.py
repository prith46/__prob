"""
Problem: Given the heads of two sorted linked lists, merge them into a single sorted linked list.
Sample Input: 1 -> 2 -> 4 and 1 -> 3 -> 4
Sample Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
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


def merge_linked_list(first, second):
    final = LinkedList()
    while first and second:
        if first.value < second.value:
            final.append(first.value)
            first = first.next
        elif first.value == second.value:
            final.append(second.value)
            second = second.next
        else:
            final.append(second.value)
            second = second.next

    while first:
        final.append(first.value)
        first = first.next

    while second:
        final.append(second.value)
        second = second.next

    print("Final Linked List")
    final.print_list()


def make_linked_list(my_list1, my_list2):
    first = LinkedList()
    for value in my_list1:
        first.append(value)
    print("First Linked list")
    first.print_list()
    second = LinkedList()
    for value in my_list2:
        second.append(value)
    print("Second Linked list")
    second.print_list()
    merge_linked_list(first.head, second.head)


make_linked_list([1, 2, 4], [1, 3, 4])
