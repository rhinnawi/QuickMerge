"""
natural_merge_sort

This module contains a class for running a natural merge sort while tracking
the number of exchanges and comparisons done.

Author: Rani Hinnawi
Date: 2023-08-22
"""
from typing import List
from support.doubly_linked_list import DoublyLinkedList


class NaturalMergeSort:
    """
    Class for running and tracking a natural merge sort run on a Python list.
    """

    def __init__(self, data: List[int]) -> "NaturalMergeSort":
        self._data = DoublyLinkedList().append_list(data)
        self._num_comparisons = 0
        self._num_exchanges = 0
        self._illustrate_merge = len(data) <= 50
        self._comparisons = []
        self._exchanges = []

    def merge_sort(self) -> "DoublyLinkedList":
        """
        Sort the data using an iterative natural merge sort algorithm. Data 
        has already been converted into a DoublyLinkedList. 

        Returns:
            DoublyLinkedList: sorted data in a doubly linked list structure 
        """
        return self._data

    def get_num_comparisons(self) -> int:
        """
        Method for indicating the number of comparisons that occurred during
        the sorting and merging processes

        Returns:
            int: number of comparisons
        """
        return self._num_comparisons

    def get_num_exchanges(self) -> int:
        """
        Method for indicating the number of exchanges that occurred during
        the sorting and merging processes

        Returns:
            int: number of exchanges
        """
        return self._num_exchanges
