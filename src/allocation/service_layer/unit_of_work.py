from __future__ import annotations
from src.allocation.adapters import repository
from src.lib.abstract_uow import AbstractUnitOfWork
from src.allocation.service_layer import messagebus


class BatchUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.batchref = repository.BatchRepository([])
        self.committed = False

    def __enter__(self):
        self.batchref = repository.BatchRepository()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.close()

    def commit(self):
        self.committed = True

    def rollback(self):
        pass


class ProductUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.batchref = repository.ProductRepository([])
        self.committed = False

    def __enter__(self):
        self.batchref = repository.ProductRepository()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.close()

    def commit(self):
        self.committed = True
        self.publish_events()

    def publish_events(self):
        for product in self.products.seen:
            while product.events:
                event = product.events.pop(0)
                messagebus.handle(event)

    def rollback(self):
        pass
