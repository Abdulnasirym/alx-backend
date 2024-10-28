#!/usr/bin/env python3
"""A python module"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """A helper function"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
