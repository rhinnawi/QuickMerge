"""
node

This module holds a class that implements a basic doubly linked list node 
object.

Author: Rani Hinnawi
Date: 2023-08-22
"""
from typing import TypeVar

# Set up generic type for stack to remain type-agnostic
T = TypeVar('T')


class Node:
    """
    Simple node built for a doubly-linked list. Methods can be chained.
    """

    def __init__(self, data: T) -> "Node":
        self._data = data
        self._next = None
        self._prev = None

    def __lt__(self, other: "Node") -> bool:
        """
        Less-than comparison for DoublyLinkedList Nodes. It is based on data
        value.

        Args:
            other (Node): The other Node with which to compare

        Returns:
            bool: True if this node is less than the other node.
        """
        return self._data < other.get_data()

    def __gt__(self, other: "Node") -> bool:
        """
        Greater-than comparison for DoublyLinkedList Nodes. It is based on data
        value.

        Args:
            other (Node): The other Node with which to compare

        Returns:
            bool: True if this node is less than the other node.
        """
        return self._data > other.get_data()

    def __ge__(self, other: 'Node') -> bool:
        """
        Greater-than-or-equal comparison for Node objects.

        Args:
            other (Node): The other Node with which to compare

        Returns:
            bool: True if this node is greater than or equal to the other node.
        """
        return not self.__lt__(other)

    def __le__(self, other: 'Node') -> bool:
        """
        Less-than-or-equal comparison for Node objects.

        Args:
            other (Node): The other Node with which to compare

        Returns:
            bool: True if this node is greater than or equal to the other node.
        """
        return not self.__gt__(other)

    def __eq__(self, other: 'Node') -> bool:
        """
        Equality comparison for Node objects. Two nodes are equal if they have
        the same data value.

        Args:
            other (Node): The other Node with which to compare

        Returns:
            bool: True if this node is equal to the other node.
        """
        return self._data == other.get_data()

    def __ne__(self, other: 'Node') -> bool:
        """
        Inequality comparison for Node objects.

        Args:
            other (Node): The other Node with which to compare

        Returns:
            bool: True if this node is not equal to the other node.
        """
        return not self.__eq__(other)

    def set_data(self, new_data: T) -> "Node":
        """
        Setter for updating the data attribute

        Args:
            new_data (T): new data to be stored in current node

        Returns:
            Node: Current node instance
        """
        self._data = new_data
        return self

    def get_data(self) -> T:
        """
        Getter for retrieving the data attribute

        Returns:
            T: Current node instance's data value
        """
        return self._data

    def set_next(self, new_next: "Node") -> "Node":
        """
        Setter for updating the next pointer

        Args:
            new_next (Node): new node for next pointer

        Returns:
            Node: Current node instance
        """
        self._next = new_next
        return self

    def get_next(self) -> "Node":
        """
        Getter for retrieving the next node

        Returns:
            Node: next node
        """
        return self._next

    def set_prev(self, new_prev: "Node") -> "Node":
        """
        Setter for updating the previous pointer

        Args:
            new_prev (Node): new node for previous pointer

        Returns:
            Node: Current node instance
        """
        self._prev = new_prev
        return self

    def get_prev(self) -> "Node":
        """
        Getter for retrieving the previous node

        Returns:
            Node: previous node
        """
        return self._prev
