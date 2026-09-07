from app.domain.entities.item import Item
from app.domain.repositories.item_repository import ItemRepository


class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def list_items(self) -> list[Item]:
        return self.repository.list()

    def get_item(self, item_id: int) -> Item | None:
        return self.repository.get(item_id)

    def create_item(self, name: str) -> Item:
        return self.repository.create(name)
