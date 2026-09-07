from fastapi import Depends
from sqlalchemy.orm import Session

from app.infra.db.repositories.item_repository_sql import SqlItemRepository
from app.infra.db.session import get_db
from app.services.item_service import ItemService


def get_item_service(db: Session = Depends(get_db)) -> ItemService:
    repository = SqlItemRepository(db)
    return ItemService(repository)
