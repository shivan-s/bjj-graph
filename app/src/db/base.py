"""Contain base classes for models."""

import os

from neo4j import GraphDatabase
from typing import Self

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
URL = os.getenv("URL")


class BaseModel:
    """Base model."""

    def __init__(self) -> None:
        """Construct object."""
        self.driver = GraphDatabase.driver(URL, auth=(USERNAME, PASSWORD))

    def __enter__(self) -> Self:
        """Entering the context."""
        return self

    def __exit__(self, exc_type, exec_value, traceback) -> None:
        """Perform when exiting the context."""
        self.driver.close()
