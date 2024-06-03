"""
Problem: Given the heads of two singly linked lists, find if the two lists intersect and return the
intersecting node. The intersection is defined by reference, not value.
Sample Input: 8 -> 4 -> 5 (for list A), 5 -> 0 -> 1 -> 8 -> 4 -> 5 (for list B)
Sample Output: 8 -> 4 -> 5
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    pointerA = headA
    pointerB = headB
    while pointerA is not pointerB:
        if pointerA:
            pointerA = pointerA.next
        else:
            pointerA = headB

        if pointerB:
            pointerB = pointerB.next
        else:
            pointerB = headA

    return pointerA


# Example usage:
# Creating two linked lists with an intersection
# List A: 4 -> 1 \
#                8 -> 4 -> 5
# List B:    5 -> 0 -> 1 /

# Common part
common = ListNode(8, ListNode(4, ListNode(5)))

# List A
headA = ListNode(4, ListNode(1, common))

# List B
headB = ListNode(5, ListNode(0, ListNode(1, common)))

# Finding intersection
intersection = getIntersectionNode(headA, headB)

# Printing result
if intersection:
    print("Intersection at node with value:", intersection.val)
else:
    print("No intersection")
