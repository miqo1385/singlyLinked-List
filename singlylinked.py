import unittest


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def to_list(self):
        data_list = []
        current = self.head
        while current:
            data_list.append(current.data)
            current = current.next
        return data_list

    @staticmethod
    def from_list(lst):
        linked_list = SinglyLinkedList()
        for item in lst:
            linked_list.append(item)
        return linked_list


def isHealthRecordSymmetric(head):
    # Helper function to reverse a linked list
    def reverse_linked_list(node):
        prev = None
        current = node
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    # Helper function to find the middle of a linked list
    def find_middle(node):
        slow = node
        fast = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    if not head or not head.next:
        return True

    # Find the middle of the list
    middle = find_middle(head)

    # Reverse the second half of the list
    reversed_second_half = reverse_linked_list(middle.next)

    # Compare the first half and reversed second half
    current_first_half = head
    current_second_half = reversed_second_half
    while current_second_half:
        if current_first_half.data != current_second_half.data:
            return False
        current_first_half = current_first_half.next
        current_second_half = current_second_half.next

    return True


# Example usage:
# Create a singly linked list with symmetric data
# linked_list1 = SinglyLinkedList.from_list([70, 80, 80, 70])
# linked_list2 = SinglyLinkedList.from_list([90, 100, 110, 100, 90])
# linked_list3 = SinglyLinkedList.from_list([120 / 80, 130 / 85, 125 / 82])

# Check if the health record is symmetric
# print(isHealthRecordSymmetric(linked_list1.head))  # Output: True
# print(isHealthRecordSymmetric(linked_list2.head))  # Output: True
# print(isHealthRecordSymmetric(linked_list3.head))  # Output: False

class TestingSingly(unittest.TestCase):

    def test01(self):
        linked_list1 = SinglyLinkedList.from_list([70, 80, 80, 70])
        self.assertEqual(isHealthRecordSymmetric(linked_list1.head), True)

    def test02(self):
        linked_list2 = SinglyLinkedList.from_list([90, 100, 110, 100, 90])
        self.assertEqual(isHealthRecordSymmetric(linked_list2.head), True)

    def test03(self):
        linked_list2 = SinglyLinkedList.from_list([120 / 80, 130 / 85, 125 / 82])
        self.assertEqual(isHealthRecordSymmetric(linked_list2.head), False)

    def test04(self):
        linked_list2 = SinglyLinkedList.from_list([120 / 80, 130 / 85, 140 / 82])
        self.assertEqual(isHealthRecordSymmetric(linked_list2.head), False)

    def test04(self):
        linked_list2 = SinglyLinkedList.from_list([100, 90, 80])
        self.assertEqual(isHealthRecordSymmetric(linked_list2.head), False)

    def test05(self):
        linked_list2 = SinglyLinkedList.from_list([])
        self.assertEqual(isHealthRecordSymmetric(linked_list2.head), True)




if __name__ == '__main__':
    unittest.main()
