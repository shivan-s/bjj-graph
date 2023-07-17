"""Database."""

import os

from neo4j import GraphDatabase

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
URL = os.getenv("URL")

URL = "bolt://localhost:7687"


class Database:
    """Database model."""

    def __init__(self, uri, user, password):
        """Init class."""
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def verify_connection(self):
        """Verify connection."""
        self.driver.verify_connectivity()

    def close(self):
        """Close database."""
        self.driver.close()
