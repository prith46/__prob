"""
Problem: Remove all elements from a linked list of integers that have value val.
Sample Input: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6, val = 6
Sample Output: 1 -> 2 -> 3 -> 4 -> 5
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

    def remove_element(self, value):
        if self.length == 0:
            return None
        temp = self.head
        before = self.head
        while temp is not None:
            if temp.value == value:
                after = temp.next
                before.next = after
                temp.next = None
                if temp == self.head:
                    self.head = after
                temp = after

            else:
                before = temp
                temp = temp.next
        return True


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(6)
linked_list.append(3)
linked_list.append(4)
linked_list.append(6)
linked_list.append(5)
linked_list.append(6)
print("Linked List: ")
linked_list.print_list()
linked_list.remove_element(6)
print("Linked List after removing that element: ")
linked_list.print_list()
