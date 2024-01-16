#!/usr/bin/env python3
"""
Task 0 - Regex-ing
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str, separator: str):
    return re.sub(fr'({separator.join(fields)})=[^{separator}]+', f'\\1={redaction}', message)