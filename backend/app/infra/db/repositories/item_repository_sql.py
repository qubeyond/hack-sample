from sqlalchemy.orm import Session

from app.domain.entities.item import Item
from app.infra.db.models import ItemModel


class SqlItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self) -> list[Item]:
        rows = self.db.query(ItemModel).all()
        return [Item(id=row.id, name=row.name) for row in rows]

    def get(self, item_id: int) -> Item | None:
        row = self.db.get(ItemModel, item_id)
        return Item(id=row.id, name=row.name) if row else None

    def create(self, name: str) -> Item:
        row = ItemModel(name=name)
        self.db.add(row)
        self.db.commit()
        self.db.refresh(row)
        return Item(id=row.id, name=row.name)
