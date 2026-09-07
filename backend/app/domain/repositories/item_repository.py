from typing import Protocol

from app.domain.entities.item import Item


class ItemRepository(Protocol):
    def list(self) -> list[Item]: ...

    def get(self, item_id: int) -> Item | None: ...

    def create(self, name: str) -> Item: ...
