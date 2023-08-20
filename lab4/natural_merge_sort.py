"""
natural_merge_sort

This module contains a class for running a natural merge sort while tracking
the number of exchanges and comparisons done.

Author: Rani Hinnawi
Date: 2023-08-22
"""
from typing import List
from support.doubly_linked_list import DoublyLinkedList
from support.node import Node


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

    ##########################################################
    def merge_sort(self) -> "DoublyLinkedList":
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
        runs = self.find_sorted_runs()
        while len(runs) > 1:
            runs = self.merge_runs(runs)

        return runs[0]

    def find_sorted_runs(self) -> List["DoublyLinkedList"]:
        """
        Find and return a list of sorted runs in the data.

        Returns:
            List[DoublyLinkedList]: List of sorted runs as DoublyLinkedLists.
        """
        runs = []
        current = self._data.get_head()
        while current:
            start = current
            while current.get_next() and \
                    current.get_next().get_data() >= current.get_data():
                current = current.get_next()

            runs.append(DoublyLinkedList().append_list(
                self.cut_run(start, current)))

            current = current.get_next()
        return runs

    def cut_run(self, start: "Node", end: "Node") -> List[int]:
        """
        Cut a run from the data and return it as a list.

        Args:
            start (Node): Start node of the run.
            end (Node): End node of the run.

        Returns:
            List[int]: List containing the run data.
        """
        run_data = []
        current = start
        while current != end.get_next():
            run_data.append(current.get_data())
            current = current.get_next()
        return run_data

    def merge_runs(self, runs: List["DoublyLinkedList"]) \
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
                merged_run = self.merge(runs[i], runs[i + 1])
                merged_runs.append(merged_run)
                i += 2
            else:
                merged_runs.append(runs[i])
                i += 1
        return merged_runs

    def merge(self, left: "DoublyLinkedList", right: "DoublyLinkedList") \
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

    ##########################################################################
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
