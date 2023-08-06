"""ORM."""
from typing import Self

from .base import BaseModel


class Position(BaseModel):
    """Position in BJJ."""

    def __init__(self, id: str | None = None, name: str | None = None):
        """Construct position object."""
        super().__init__()
        self.id = id
        self.name = name

    @classmethod
    def read_all(self) -> list[Position]:
        """Read all positions."""
        with self.driver.session() as session:
            results = session.execute_write(
                """
                MATCH (p:Position)
                RETURN id(p), p.name AS name
                """
            )
            return [Position(**result.data()) for result in results]

    def create(self) -> Position:
        """Create a position."""
        with self.driver.session() as session:
            result = session.execute_write(
                """
                CREATE (p:Position)
                SET p.name = $name
                RETURN id(p), p.name AS name
                """,
                name=self.name,
            )
            return Position(**result.single().get(0))
