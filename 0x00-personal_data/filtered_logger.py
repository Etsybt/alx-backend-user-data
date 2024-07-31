#!/usr/bin/env python3
"""
filtered_logger
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(rf'({"|".join(fields)})=[ ^ {separator}]*',
                         lambda m: f'{m.group().split("=")[0]}={redaction}',
                         message)
    return message
