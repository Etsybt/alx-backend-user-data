#!/usr/bin/env python3
"""
filtered_logger
"""
import re
import os
import mysql.connector
import logging
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Returns the log message obfuscated
    """
    pattern = rf'({"|".join(fields)})=[^{separator}]*'
    return re.sub(pattern,
                  lambda m: f'{m.group().split("=")[0]}={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(
            self.fields,
            self.REDACTION,
            record.getMessage(),
            self.SEPARATOR)
        return super().format(record)


def get_db() -> mysql.connector.MySQLConnection:
    """ Connection to MySQL environment """
    return mysql.connector.connect(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME')
    )


def get_logger() -> logging.Logger:
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def main():
    """Main function to connect to the database and log user data"""
    logger = get_logger()
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")

    for row in cursor:
        message = "; ".join(f"{key}={value}" for key, value in row.items())
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
