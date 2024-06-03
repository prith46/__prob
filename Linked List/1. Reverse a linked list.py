"""
Problem: Given the head of a singly linked list, reverse the list and return the reversed list.
Sample Input: 1 -> 2 -> 3 -> 4 -> 5
Sample Output: 5 -> 4 -> 3 -> 2 -> 1
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

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True


def reverse_list(my_list):
    linked_list = LinkedList()
    for value in my_list:
        linked_list.append(value)
    print("Linked list")
    linked_list.print_list()
    linked_list.reverse()
    print("Reversed list")
    linked_list.print_list()


reverse_list([1, 2, 3, 4, 5])
