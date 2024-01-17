#!/usr/bin/env python3
"""
Task 0 - Regex-ing
"""
from typing import List
import re
import logging
import os
import mysql.connector
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def main():
    """Obtain a database connection,
    retrieve rows from the users table,
    and display each row in a filtered format."""
    db_connector = get_db()

    try:
        cursor = db_connector.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        logger = get_logger()

        for row in rows:
            formated_row = " ".join(
                f"{field}={logger.REDACTION}"
                if field in PII_FIELDS else
                f"{field}={value}" for field,
                value in zip(cursor.column_names, row))

            logger.info(formated_row)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        db_connector.close()


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """formats the message with the filter_datum function"""
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


def get_logger() -> logging.Logger:
    """returns a logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(
        fmt="%(asctime)s - %(levelname)s - %(message)s",
        pii_fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to the database (MySQLConnection object)"""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    dbname = os.getenv("PERSONAL_DATA_DB_NAME")

    # Creating a connection to the database
    connection = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=dbname
    )

    return connection

if __name__ == "__main__":
    # Call the main function if the script is executed directly
    main()
