#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# encoding: utf8
"""Miscellaneous helpers.

This module contains a few helpers to import in your projects.

    Typical usage example:

    logger = create_logger(__name__, f'./{__name__}.log)
    letter = find_first(('a', 'b', 'c'), lambda x: x == 'b')
"""


import json
import logging
from logging.handlers import RotatingFileHandler
from typing import Any, Callable, Iterable


def pretty_format(dictionary: dict) -> str:
    """
    Formats a dictionary into a pretty string

    Args:
        dictionary: the input dictionary to pretty print

    Returns:
        A pretty printed string
    """
    return json.dumps(dictionary, sort_keys=True, indent=4)


def create_logger(name: str, path: str, level:int=logging.DEBUG, max_size:int=50*1024, backup_count:int=0):
    """
    Creates a logging.Logger object

    Args:
        name: the name of the logger
        path: the path where the logger should write its logs
        level: the desired logging level (defaults to logging.DEBUG)
        max_size: the maximum size in bytes of each log file (defaults to 50 KB)
        backup_count: the number of backup files to keep (defaults to 0)

    Returns:
        A logging.Logger object
    """
    formatter = logging.Formatter('[{asctime}] {levelname:<8s} {funcName:26} L{lineno:03} {message}', style='{')
    logger = logging.getLogger(name)
    logger.setLevel(level)

    log_handler = RotatingFileHandler(path, maxBytes=max_size, backupCount=backup_count)
    log_handler.setFormatter(formatter)

    logger.addHandler(log_handler)
    return logger


def find_first(sequence: Iterable, predicate: Callable, default: Any=None) -> Any:
    """
    Returns the first element of a sequence that matches a certain predicate or a default value

    Args:
        sequence: the sequence to test the predicate against
        predicate: a function that takes one element as input parameter and either return true or false
        default: the default value to return if no sequence element match the provided predicate

    Returns:
        Either the first element in sequence that matches the predicate or a default value
    """
    return next((x for x in sequence if predicate(x)), default)
