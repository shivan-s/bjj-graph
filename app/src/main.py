"""Main."""

import logging

from db import Position, driver

logging.basicConfig(level=logging.DEBUG)

positions = Position.read_all()

print(positions)

driver().close()
