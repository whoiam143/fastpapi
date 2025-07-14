from typing import Annotated
from fastapi import APIRouter, Path

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
def items():
    return {
        "1": "1hah",
        "2": "2hah",
        "3": "3hah",
    }

@router.get("/latest/")
def get_latest_item():
    return {"id": "latest"}


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=100_000)]):
    return {
        "item": {
            "id": item_id,
        },
    }