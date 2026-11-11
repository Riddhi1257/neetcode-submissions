class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Create a dummy node to mark the beginning of the merged list
        dummy = ListNode()

        # Initialize tail at dummy to keep track of the last node
        tail = dummy

        # Continue until one of the two lists becomes empty
        while list1 and list2:

            # Compare the current nodes of both lists
            if list1.val < list2.val:

                # Connect the smaller node from List 1 to the merged list
                tail.next = list1

                # Move List 1 to its next node
                list1 = list1.next

            else:

                # Connect the smaller node from List 2 to the merged list
                tail.next = list2

                # Move List 2 to its next node
                list2 = list2.next

            # Move our tail pointer to the node we just attached
            tail = tail.next

        # Attach the remaining nodes from List 1, if any
        if list1:
            tail.next = list1

        # Attach the remaining nodes from List 2, if any
        elif list2:
            tail.next = list2

        # Return the head of the merged list, skipping the dummy node
        return dummy.next