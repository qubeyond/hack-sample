from fastapi import APIRouter, Depends, HTTPException

from app.api.deps import get_item_service
from app.api.schemas.item import ItemCreate, ItemRead
from app.services.item_service import ItemService

router = APIRouter(prefix="/items", tags=["items"])


@router.get("", response_model=list[ItemRead])
def list_items(service: ItemService = Depends(get_item_service)):
    return service.list_items()


@router.post("", response_model=ItemRead)
def create_item(payload: ItemCreate, service: ItemService = Depends(get_item_service)):
    return service.create_item(payload.name)


@router.get("/{item_id}", response_model=ItemRead)
def get_item(item_id: int, service: ItemService = Depends(get_item_service)):
    item = service.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item
