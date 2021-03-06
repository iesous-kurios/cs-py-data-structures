from typing import Optional


class Node:
    """
    Each Node holds a reference to its previous node
    as well as its next_node node in the List.
    """

    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


class DoublyLinkedList:
    """
    Our doubly-linked list class. It holds references to
    the list's head and tail nodes.
    """

    def __init__(self, node_list: Optional[list] = None):
        self.head = self.tail = None  # initialize head and tail to None
        self.size = 0  # number of items stored in DLL
        # if given node_list exists
        if node_list is not None:
            # then add each value in list to tail
            for value in node_list:
                self.add_to_tail(value)

    def __repr__(self):
        """Returns a string representation of this DoublyLinkedList"""

        str_repr = "DLL=["
        if self.size == 0:
            return f"{str_repr}]"
        current_node = self.head
        while current_node is not None:
            str_repr += f"{current_node}{']' if current_node is self.tail else ' -> '}"
            current_node = current_node.next
        return str_repr

    def __len__(self):
        return self.size

    def add_to_head(self, value):
        """
        Wraps the given value in a Node and inserts it
        as the new head of the list. Don't forget to handle
        the old head node's previous pointer accordingly.
        """
        pass

    def remove_head(self):
        """
        Removes the List's current head node, making the
        current head's next_node node the new head of the List.
        Returns the value of the removed Node.
        """
        pass

    def add_to_tail(self, value):
        """
        Wraps the given value in a Node and inserts it
        as the new tail of the list. Don't forget to handle
        the old tail node's next_node pointer accordingly.
        """
        pass

    def remove_tail(self):
        """
        Removes the List's current tail node, making the
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        """
        pass

    def move_to_front(self, node):
        """
        Removes the input node from its current spot in the
        List and inserts it as the new head node of the List.
        """
        pass

    def move_to_end(self, node):
        """
        Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List.
        """
        pass

    def delete(self, node):
        """
        Deletes the input node from the List, preserving the
        order of the other elements of the List.
        """
        pass

    def get_max(self):
        """
        Finds and returns the maximum value of all the nodes
        in the List.
        """
        pass
