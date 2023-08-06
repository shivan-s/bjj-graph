"""Main."""

import logging

from src.db import Position

logging.basicConfig(level=logging.DEBUG)


positions = Position.read_all()

print(positions)
