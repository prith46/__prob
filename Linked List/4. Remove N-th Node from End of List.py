"""
Problem: Given the head of a linked list and an integer n, remove the n-th node from the end of the list and
return its head.
Sample Input: 1 -> 2 -> 3 -> 4 -> 5, n = 2
Sample Output: 1 -> 2 -> 3 -> 5
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

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            return temp.value
        pre = None
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        return temp.value

    def pop_first(self):
        if self.length < 2:
            return self.pop()
        temp = self.head
        self.head = temp.next
        temp.next = None
        return temp.value

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
            if temp:
                print(' -> ', end='')
        print('\n')

    def remove_node(self, n):
        if n < 1 or n > self.length:
            return None
        if self.length == n:
            return self.pop_first()
        temp = self.head
        before = None
        for _ in range(self.length-n-1):
            temp = temp.next
        before = temp
        temp = temp.next
        before.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_list()
print(linked_list.remove_node(5))
