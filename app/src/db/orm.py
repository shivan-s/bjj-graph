"""ORM."""
from typing import Self

from .connector import driver


class Position:
    """Position in BJJ."""

    _driver = driver()

    def __init__(self, id: str | None = None, name: str | None = None):
        """Construct position object."""
        self.id = id
        self.name = name

    @classmethod
    def read_all(cls) -> list[Self]:
        """Read all positions."""
        with cls._driver.session() as session:
            results = session.execute_write(
                lambda tx: tx.run(
                    """
                    MATCH (p:Position)
                    RETURN p
                    """
                )
            )
            return [Position(**result.data()) for result in results]

    @classmethod
    def read(cls, **kwargs) -> None:
        """Read a position."""
        pass

    def create(self) -> Self:
        """Create a position."""
        with self._driver.session() as session:
            result = session.execute_write(
                lambda tx: tx.run(
                    """
                    CREATE (p:Position)
                    SET p.name = $name
                    RETURN id(p), p.name AS name
                    """,
                    name=self.name,
                )
            )
            return Position(**result.single().get(0))

    def update(self) -> None:
        """Update the position."""
        pass

    def delete(self) -> None:
        """Delete the position."""
        pass

    def link(self) -> None:
        """Link two positions."""
        pass
