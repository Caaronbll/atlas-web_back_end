#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            #truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dictionary with hypermedia pagination information based on index."""
        assert page_size > 0, "Page size must be greater than 0."

        if index is None:
            # If index is None, set it to 0 (start of the dataset)
            index = 0
        else:
            # Validate that index is in a valid range
            assert 0 <= index < len(self.dataset()), "Index is out of range."

        # Calculate the end index of the current page
        end_index = index + page_size

        # Get the actual data for the current page
        current_page_data = self.dataset()[index:end_index]

        # Calculate the next index to query with
        next_index = end_index

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': current_page_data
        }
