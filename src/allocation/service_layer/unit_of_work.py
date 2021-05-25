from __future__ import annotations
from src.allocation.adapters import repository
from src.lib.abstract_uow import AbstractUnitOfWork
from src.allocation.service_layer import messagebus


class BatchUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.batchref = repository.BatchRepository()
        self.committed = False

    def __enter__(self):
        self.batchref = repository.BatchRepository()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)

    def _commit(self):
        self.committed = True

    def collect_new_events(self):
        self.batchref = repository.BatchRepository()
        for batch in self.batchref.seen:
            while batch.events:
                yield batch.events.pop(0)

    def rollback(self):
        pass


class ProductUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.product = repository.ProductRepository()
        self.committed = False

    def __enter__(self):
        self.product = repository.ProductRepository()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)

    def _commit(self):
        self.committed = True

    def collect_new_events(self):
        self.product = repository.ProductRepository()
        for product in self.product.seen:
            while product.events:
                yield product.events.pop(0)

    def rollback(self):
        pass
