import os

from neo4j import GraphDatabase

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
URL = os.getenv("URL")


def driver():
    """Connect to the database."""
    return GraphDatabase.driver(URL, auth=(USERNAME, PASSWORD))
