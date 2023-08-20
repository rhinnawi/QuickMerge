"""
doubly_linked_list

This module holds a class that implements a basic doubly linked list object.

Author: Rani Hinnawi
Date: 2023-08-22
"""
from typing import List, TypeVar
from support.node import Node

# Set up generic type for stack to remain type-agnostic
T = TypeVar('T')


class DoublyLinkedList:
    """
    Doubly linked list class
    """

    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def __str__(self) -> str:
        """
        Output string representation of DoublyLinkedList

        Returns:
            str: string representation of list
        """
        return ", ".join(self.to_list)

    def __len__(self) -> int:
        """
        Returns the number of nodes in the DoublyLinkedList

        Returns:
            int: size of the list
        """
        return self._size

    def append_list(self, p_list: List[T]) -> "DoublyLinkedList":
        """
        Method for adding entire Python list to current doubly linked list

        Args:
            p_list (List[T]): Python list being converted

        Returns:
            DoublyLinkedList: current instance of DoublyLinkedList
        """
        for item in p_list:
            self.append(item)

        return self

    def index(self, position: int) -> "Node":
        """
        Retrieve the node in the DoublyLinkedList at the provided position.

        Args:
            position (int): index position of desired node

        Returns:
            Node: node at the requested index

        Raises:
            ValueError: if position is less than zero or larger than list size
        """
        if position < 0 or position >= self._size:
            error = "Position is out of bounds. Must be between 0 and "
            error += str(self._size)
            raise ValueError(error)

        current = self._head
        current_index = 0

        while current and current_index < position:
            current = current.get_next()
            current_index += 1

        return current

    def to_list(self) -> List[T]:
        """
        Return current DoublyLinkedList data as a regular Python list

        Returns:
            List[T]: list of all data items in doubly linked list nodes
        """
        current = self._head
        new_list = []
        while current:
            new_list.append(current.get_data())
            current = current.get_next()

        return new_list

    def append(self, data: T) -> "DoublyLinkedList":
        """
        Method for adding new item to the end of the linked list.

        Args:
            data (T): new item to be added

        Returns:
            DoublyLinkedList: Current linked list instance
        """
        new_node = Node(data)
        if not self._head:
            # Case: empty list
            self._head = new_node
            self._tail = new_node
        else:
            # Default case: add to end of non-empty list
            new_node.set_prev(self._tail)
            self._tail.set_next(new_node)
            self._tail = new_node

        # Keep track of linked list size
        self._size += 1

    def remove(self, data: T) -> "DoublyLinkedList":
        """
        Method for removing an item of a specific value from the list

        Args:
            data (T): value of item being removed

        Returns:
            DoublyLinkedList: current DoublyLinkedList instance
        """
        current = self._head
        while current:
            if current.get_data() == data:
                if current.get_prev():
                    # Update previous node's next pointer
                    current.get_prev().set_next(current.get_next())
                else:
                    self._head = current.get_next()

                if current.get_next():
                    current.get_next().set_prev(current.get_prev())
                else:
                    self._tail = current.get_prev()

                self._size -= 1
                return self

            current = current.get_next()
