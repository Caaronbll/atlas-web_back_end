#!/usr/bin/env python3
"""
Task 0 - Regex-ing
"""
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        Original_message = record.getMessage()
        New_message = filter_datum(
            self.fields,
            self.REDACTION,
            Original_message,
            self.SEPARATOR
        )
        record.msg = New_message
        return super().format(record)




def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """regexs occurrences of certain field values"""
    for field in fields:
        message = re.sub(f"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message
