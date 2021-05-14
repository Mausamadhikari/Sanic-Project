from __future__ import annotations
from src.allocation.adapters import repository
from src.lib.abstract_uow import AbstractUnitOfWork


class BatchUonitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.batchref = repository.Batchrepository([])
        self.committed = False

    def __enter__(self):
        self.batchref = repository.Batchrepository()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.close()

    def commit(self):
        self.committed = True

    def rollback(self):
        pass
