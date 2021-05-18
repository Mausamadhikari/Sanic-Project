from pydantic import BaseModel, dataclasses


class Event(BaseModel):
    pass


class OutOfStock(Event):
    sku: str
