import json
import os
import re
import sys
import warnings
from pathlib import Path

import yaml


def read_yaml(file_path: str) -> dict:
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file_path}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML: {e}")


def json_to_str(payload: dict) -> str:
    payload = json.dumps(payload)
    if isinstance(payload, str):
        return payload
    raise Exception("Something wrong in this json_to_str function")


def str_to_json(payload: str, retries=4) -> dict:
    try:
        while retries >= 0:
            payload = json.loads(payload)
            if isinstance(payload, dict):
                break
            retries -= 1
        return payload
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON string: {e}")


def dynamic_dirname(path, depth):
    """
    Recursively traverses the directory path to the specified depth.

    Args:
        path (str): The starting path.
        depth (int): The desired depth to traverse.

    Returns:
        str: The directory path at the specified depth.

    Example:

        current_dir = os.path.dirname(__file__)
        desired_depth = 3  # Adjust the depth as needed

        result = dynamic_dirname(current_dir, desired_depth)
        print(result)  # Output: ./HCMC-AIO2024
    """

    if depth == 0:
        return path

    parent_dir = os.path.dirname(path)
    return dynamic_dirname(parent_dir, depth - 1)


def is_url(query):
    """Checks if a given query is a URL.

    Args:
      query: The query to check.

    Returns:
      True if the query is a URL, False otherwise.
    """

    url_pattern = r"^(http|https)://([\w\d-]+\.)+[\w\d-]+\/([\w\d./?%&amp;=]*)?"

    return re.match(url_pattern, query) is not None
