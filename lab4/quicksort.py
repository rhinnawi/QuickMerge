"""
quicksort

This module contains a class for running an iterative quicksort algorithm while
tracking the number of exchanges and comparisons done.

Author: Rani Hinnawi
Date: 2023-08-22
"""
from typing import List, Tuple


class Quicksort:
    """
    Class for running and tracking a quicksort run on a Python list.
    """

    def __init__(self, data: List[int], pivot_option: str,
                 insertion_threshold: int) -> "Quicksort":
        self._data = data
        self._num_comparisons = 0
        self._num_exchanges = 0
        self._illustrate_sort = len(data) <= 50
        self._comparisons = []
        self._exchanges = []
        self._pivot_option = pivot_option
        self._insertion_threshold = insertion_threshold

    def q_sort(self) -> List[int]:
        """
        Sorts the data using an iterative quicksort algorithm

        Returns:
            List[int]: sorted data
        """
        # Initialize the stack with the entire array
        stack = [(0, len(self._data) - 1)]
        while stack:
            low, high = stack.pop()
            if low < high:
                # Log comparison
                if self._illustrate_sort:
                    self._comparisons.append((low, high))
                self._num_comparisons += 1

                if high - low + 1 <= self._insertion_threshold:
                    # Log comparison
                    if self._illustrate_sort:
                        self._comparisons.append(
                            (high - low + 1, self._insertion_threshold))
                    self._num_comparisons += 1

                    self._insertion_sort(low, high)
                else:
                    pivot_index = self._choose_pivot(low, high)
                    pivot_index = self._partition(low, high, pivot_index)
                    stack.append((low, pivot_index - 1))
                    stack.append((pivot_index + 1, high))

        return self._data

    def _choose_pivot(self, low: int, high: int) -> int:
        """
        Chooses the pivot index based on the selected pivot_option.

        Args:
            low (int): The low index of the partition
            high (int): The high index of the partition

        Returns:
            int: The selected pivot index
        """
        if self._pivot_option == "first":
            return low
        elif self._pivot_option == "median_of_three":
            return self._median_of_three(low, high)
        else:
            return high

    def _insertion_sort(self, low: int, high: int) -> "Quicksort":
        """
        Sorts a partition of the data using insertion sort.

        Args:
            low (int): The low index of the partition
            high (int): The high index of the partition

        Returns:
            Quicksort: current object instance
        """
        for i in range(low + 1, high + 1):
            key = self._data[i]
            j = i - 1

            # Compare and potentially move elements to the right
            while j >= low and self._data[j] > key:
                # Log comparison
                if self._illustrate_sort:
                    self._comparisons.append((self._data[j], low))
                self._num_comparisons += 1

                # Move the element to the right and log exchange
                self._data[j + 1] = self._data[j]
                if self._illustrate_sort:
                    self._exchanges.append((self._data[j + 1], self._data[j]))
                self._num_exchanges += 1

                j -= 1

            # Insert key at correct position and log exchange
            self._data[j + 1] = key
            if self._illustrate_sort:
                self._exchanges.append((self._data[j + 1], key))
            self._num_exchanges += 1

        return self

    def _partition(self, low: int, high: int, pivot_index: int) -> int:
        """
        Partitions the data around the pivot.

        Args:
            low (int): The low index of the partition
            high (int): The high index of the partition
            pivot_index (int): The index of the pivot element

        Returns:
            int: The final position of the pivot element
        """
        # Set up pivot
        pivot_value = self._data[pivot_index]
        self._swap(pivot_index, high)

        # Partition around pivot
        i = low
        for j in range(low, high):
            if self._data[j] <= pivot_value:
                # Swap around pivot
                if self._illustrate_sort:
                    self._comparisons.append((self._data[j], pivot_value))
                self._num_comparisons += 1

                self._swap(i, j)
                i += 1

        # Reset element in "high" position and return final pivot index
        self._swap(i, high)
        return i

    def _median_of_three(self, low: int, high: int) -> int:
        """
        Chooses the pivot index as the median of three values (low, high, and 
        middle).

        Args:
            low (int): The low index of the partition
            high (int): The high index of the partition

        Returns:
            int: The selected pivot index
        """
        mid = (low + high) // 2
        candidates = [(low, self._data[low]),
                      (mid, self._data[mid]), (high, self._data[high])]
        candidates.sort(key=lambda x: x[1])
        return candidates[1][0]

    def _swap(self, i: int, j: int) -> "Quicksort":
        """
        Helper method for swapping two list elements and logging the swap

        Args:
            i (int): index of the first element
            j (int): index of the second element

        Returns:
            Quicksort: current object instance
        """
        self._num_exchanges += 1
        self._exchanges.append((self._data[i], self._data[j]))
        self._data[i], self._data[j] = self._data[j], self._data[i]
        return self

    def get_num_comparisons(self) -> int:
        """
        Method for indicating the number of comparisons that occurred during
        the quicksort processes

        Returns:
            int: number of comparisons
        """
        return self._num_comparisons

    def get_num_exchanges(self) -> int:
        """
        Method for indicating the number of exchanges that occurred during
        the quicksort processes

        Returns:
            int: number of exchanges
        """
        return self._num_exchanges

    def get_comparisons(self) -> List[Tuple[int, int]]:
        """
        Method for retrieving all logged comparisons that occurred during
        the quicksort processes

        Returns:
            int: number of comparisons
        """
        return self._comparisons

    def get_exchanges(self) -> List[Tuple[int, int]]:
        """
        Method for retrieving all logged exchanges that occurred during
        the quicksort processes

        Returns:
            int: number of exchanges
        """
        return self._exchanges
