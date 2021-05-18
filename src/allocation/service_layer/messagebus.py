from src.allocation.domain import events
from src.allocation.adapters import email


def handle(event: events.Event):
    for handler in HANDLERS[type(event)]:
        handler(event)


async def send_out_of_stock_notification(event: events.OutOfStock):
    await email.send_email(
        "abc@abc.com",
        f"Out Of stock for {event.sku}",
    )


HANDLERS = {
    events.OutOfStock: [send_out_of_stock_notification],
}
# type:Dict[Type[events.Event],List[Callable]]
