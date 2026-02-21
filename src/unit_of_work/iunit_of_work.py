from abc import ABC, abstractmethod
from src.repositories.product_repository import ProductRepository
from src.repositories.category_repository import CategoryRepository

class IUnitOfWork(ABC):

    products: ProductRepository
    categories: CategoryRepository

    @abstractmethod
    def begin(self):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass

    @abstractmethod
    def dispose(self):
        pass
