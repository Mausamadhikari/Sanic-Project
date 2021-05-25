from typing import Union, List
from src.allocation.service_layer import service, unit_of_work
from src.allocation.adapters import email
from src.allocation.domain import events, command

Message = Union[command.Command, events.Event]


async def handle(message: Message, uow: unit_of_work.AbstractUnitOfWork):
    results = []
    queue = [message]
    while queue:
        message = queue.pop(0)
        if isinstance(message, events.Event):
            await handle_event(message, queue, uow)
        elif isinstance(message, command.Command):
            cmd_result = await handle_command(message, queue, uow)
            results.append(cmd_result)
        else:
            raise Exception(f"{message} is not recognized as Event or Command")
    return results

    # for handler in HANDLERS[type(event)]:
    #     handler(event)


async def handle_event(
    event: events.Event, queue: List[Message], uow: unit_of_work.AbstractUnitOfWork
):
    for handler in HANDLERS[type(event)]:
        await handler(event, uow=uow)
        queue.extend(uow.collect_new_events())


async def handle_command(
    command: command.Command,
    queue: List[Message],
    uow: unit_of_work.AbstractUnitOfWork,
):
    try:
        handler = COMMAND_HANDLERS[type(command)]
        result = await handler(command, uow=uow)
        queue.extend(uow.collect_new_events())
    except Exception:
        raise


async def send_out_of_stock_notification(event: events.OutOfStock):
    await email.send_email(
        "abc@abc.com",
        f"Out Of stock for {event.sku}",
    )


HANDLERS = {
    events.OutOfStock: [send_out_of_stock_notification],
}
# type:Dict[Type[events.Event],List[Callable]]

COMMAND_HANDLERS = {
    command.CreateProduct: service.add_product,
    command.Allocate: service.allocate,
    command.CreateBatch: service.add_batch,
}
