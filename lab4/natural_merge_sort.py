"""
natural_merge_sort

This module contains a class for running an iterative natural merge sort while
tracking the number of exchanges and comparisons done.

Author: Rani Hinnawi
Date: 2023-08-22
"""
from typing import List, Tuple
from support.doubly_linked_list import DoublyLinkedList


class NaturalMergeSort:
    """
    Class for running and tracking a natural merge sort run on a Python list.
    Original list is converted to a DoublyLinkedList for space optimization.
    """

    def __init__(self, data: List[int]) -> "NaturalMergeSort":
        self._data = DoublyLinkedList().append_list(data)
        self._num_comparisons = 0
        self._num_exchanges = 0
        self._illustrate_merge = len(data) <= 50
        self._comparisons = []
        self._exchanges = []

    def n_merge_sort(self) -> "DoublyLinkedList":
        """
        Sort the data using an iterative natural merge sort algorithm. Data 
        has already been converted into a DoublyLinkedList. 

        Returns:
            DoublyLinkedList: sorted data in a doubly linked list structure 
        """
        if not self._data:
            # Case: Empty list
            return self._data

        # Partition into sorted runs then merge
        runs = self._find_sorted_runs()
        while len(runs) > 1:
            runs = self._merge_runs(runs)

        return runs[0]

    def _find_sorted_runs(self) -> List["DoublyLinkedList"]:
        """
        Find and return a list of sorted runs in the data.

        Returns:
            List[DoublyLinkedList]: List of sorted runs as DoublyLinkedLists.
        """
        runs = []
        current = self._data.get_head()

        # Cycle through data and identify runs. Add runs as smaller lists
        while current:
            sorted_run = DoublyLinkedList()

            while current and (not current.get_next() or
                               current.get_next() >= current):
                # Log comparison
                if current.get_next() and self._illustrate_merge:
                    self._comparisons.append((current.get_data(),
                                              current.get_next().get_data()))
                    self._num_comparisons += 1

                temp = self._data.remove_head_node()
                sorted_run.append_node(temp)
                # Update the current pointer after removal
                current = self._data.get_head()

            runs.append(sorted_run)

        return runs

    def _merge_runs(self, runs: List["DoublyLinkedList"]) \
            -> List["DoublyLinkedList"]:
        """
        Merge the runs and return a new list of merged runs.

        Args:
            runs (List[DoublyLinkedList]): List of runs to be merged.

        Returns:
            List[DoublyLinkedList]: List of merged runs.
        """
        merged_runs = []
        i = 0
        while i < len(runs):
            if i + 1 < len(runs):
                merged_run = self._merge(runs[i], runs[i + 1])
                merged_runs.append(merged_run)
                i += 2
            else:
                merged_runs.append(runs[i])
                i += 1
        return merged_runs

    def _merge(self, left: "DoublyLinkedList", right: "DoublyLinkedList") \
            -> "DoublyLinkedList":
        """
        Merge two runs (DoublyLinkedLists) into one. This is done without
        creating new nodes.

        Args:
            left (DoublyLinkedList): Left run to be merged.
            right (DoublyLinkedList): Right run to be merged.

        Returns:
            DoublyLinkedList: Merged run.
        """
        merged_run = DoublyLinkedList()
        left_node = left.get_head()
        right_node = right.get_head()

        while left_node and right_node:
            # Log the comparison
            if self._illustrate_merge:
                self._comparisons.append((left_node.get_data(),
                                          right_node.get_data()))
            self._num_comparisons += 1

            if left_node <= right_node:
                # Case: left list head has a value <= right list's head
                temp = left.remove_head_node()
                left_node = left.get_head()
                merged_run.append_node(temp)
            else:
                # Default case: right list's head node value is > the left's
                temp = right.remove_head_node()
                right_node = right.get_head()
                merged_run.append_node(temp)

                # Log exchange: a farther-right number is being moved forward
                if self._illustrate_merge:
                    self._exchanges.append((left_node.get_data(),
                                            temp.get_data()))
                self._num_exchanges += 1

        while left_node:
            # Case: entire right list has been added
            temp = left.remove_head_node()
            left_node = left.get_head()
            merged_run.append_node(temp)

        while right_node:
            # Case: entire left list has been added
            temp = right.remove_head_node()
            right_node = right.get_head()
            merged_run.append_node(temp)

        # Return merged list
        return merged_run

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

    def get_comparisons(self) -> List[Tuple[int, int]]:
        """
        Method for retrieving all logged comparisons that occurred during
        the sorting and merging processes

        Returns:
            int: number of comparisons
        """
        return self._comparisons

    def get_exchanges(self) -> List[Tuple[int, int]]:
        """
        Method for retrieving all logged exchanges that occurred during
        the sorting and merging processes

        Returns:
            int: number of exchanges
        """
        return self._exchanges
