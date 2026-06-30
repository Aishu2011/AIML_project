import os
import time
from functools import wraps
from datetime import datetime


def execution_time(func):
    """
    Decorator to calculate execution time of a function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"{func.__name__} executed in {end - start:.4f} seconds")

        return result

    return wrapper


def validate_file(file_path: str) -> bool:
    """
    Checks whether a file exists.
    """
    return os.path.isfile(file_path)


def validate_path(path: str) -> bool:
    """
    Checks whether a directory exists.
    """
    return os.path.exists(path)


def generate_timestamp() -> str:
    """
    Returns current timestamp.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")