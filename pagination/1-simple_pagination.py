#!/usr/bin/env python3
"""Task 1 - implementing index_range to a class"""

import csv
from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple:
    """Returns a range of indexes"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            """Returns a list of lists"""
            assert isinstance(page, int) and page > 0
            assert isinstance(page_size, int) and page_size > 0
            self.__dataset = []
            with open(self.DATA_FILE, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    self.__dataset.append(row)
            indexes = index_range(page, page_size)
            return self.__dataset[indexes[0]:indexes[1]]
