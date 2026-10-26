# 141. Linked List Cycle: https://leetcode.com/problems/linked-list-cycle/

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Cycle exists
    head1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    head1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Cycle: 3 -> 2 -> 0 -> -4 -> 2
    print("Test 1 Results:", solution.hasCycle(head1))  # Expected: True

    # Test Case 2: No cycle
    head2 = ListNode(1)
    head2.next = ListNode(2)
    print("Test 2 Results:", solution.hasCycle(head2))  # Expected: False

    # Test Case 3: Single node with cycle
    head3 = ListNode(1)
    head3.next = head3  # Cycle: 1 -> 1
    print("Test 3 Results:", solution.hasCycle(head3))  # Expected: True

    # Test Case 4: Single node without cycle
    head4 = ListNode(1)
    print("Test 4 Results:", solution.hasCycle(head4))  # Expected: False

    # Test Case 5: Empty list
    head5 = None
    print("Test 5 Results:", solution.hasCycle(head5))  # Expected: False
    
