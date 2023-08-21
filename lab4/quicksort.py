"""
quicksort

This module contains a class for running an iterative quicksort algorithm while
tracking the number of exchanges and comparisons done.

Author: Rani Hinnawi
Date: 2023-08-22
"""
from typing import List, Tuple


class NaturalMergeSort:
    """
    Class for running and tracking a quicksort run on a Python list.
    """

    def __init__(self, data: List[int]) -> "NaturalMergeSort":
        self._data = data
        self._num_comparisons = 0
        self._num_exchanges = 0
        self._illustrate_merge = len(data) <= 50
        self._comparisons = []
        self._exchanges = []

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
