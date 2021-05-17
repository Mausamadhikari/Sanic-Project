from __future__ import annotations
from src.allocation.adapters import repository
from src.lib.abstract_uow import AbstractUnitOfWork


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

    def rollback(self):
        pass
