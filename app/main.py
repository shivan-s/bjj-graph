"""Main."""

import os

from neo4j import GraphDatabase

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
URL = os.getenv("URL")

with GraphDatabase.driver(URL, auth=(USERNAME, PASSWORD)) as driver:
    driver.verify_connectivity()
