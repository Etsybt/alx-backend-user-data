#!/usr/bin/env python3
"""
filtered_logger
"""
import re
import logging


def filter_datum(fields, redaction, message, separator):
    """
    returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(rf'({"|".join(fields)})=[ ^ {separator}]*',
                         lambda m: f'{m.group().split("=")[0]}={redaction}',
                         message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        return super().format(record)
