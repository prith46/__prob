"""
Problem: Given the head of a singly linked list, determine if it is a palindrome.
Sample Input: 1 -> 2 -> 2 -> 1
Sample Output: true
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(temp):
    before = None
    while temp is not None:
        after = temp.next
        temp.next = before
        before = temp
        temp = after
    return before


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

    def check_palindrome(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        first_half = self.head
        second_half = reverse(slow)
        while second_half is not None:
            if first_half.value == second_half.value:
                first_half = first_half.next
                second_half = second_half.next
            else:
                return False
        return True


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(3)
linked_list.append(2)
linked_list.append(1)

if linked_list.check_palindrome():
    print("LL is a Palindrome")
else:
    print("LL is not a Palindrome")
