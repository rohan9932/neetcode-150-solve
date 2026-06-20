# 10. Reverse a Linked List: https://leetcode.com/problems/reverse-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        nxt = head

        while curr != None and nxt != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
    
# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_head1 = solution.reverseList(head1)
    print("Test 1 Results:", end=" ")
    while reversed_head1:
        print(reversed_head1.val, end=" ")
        reversed_head1 = reversed_head1.next
    print()  # Expected Output: 5 4 3 2 1

    # Test Case 2
    head2 = ListNode(1, ListNode(2))
    reversed_head2 = solution.reverseList(head2)
    print("Test 2 Results:", end=" ")
    while reversed_head2:
        print(reversed_head2.val, end=" ")
        reversed_head2 = reversed_head2.next
    print()  # Expected Output: 2 1

    # Test Case 3
    head3 = None
    reversed_head3 = solution.reverseList(head3)
    print("Test 3 Results:", end=" ")
    while reversed_head3:
        print(reversed_head3.val, end=" ")
        reversed_head3 = reversed_head3.next
    print()  # Expected Output: (no output, as the list is empty)
