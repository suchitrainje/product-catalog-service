from src.database import SessionLocal
from src.repositories.product_repository import ProductRepository
from src.repositories.category_repository import CategoryRepository
from .iunit_of_work import IUnitOfWork

class SQLUnitOfWork(IUnitOfWork):

    def __init__(self):
        self.session = SessionLocal()
        self.products = ProductRepository(self.session)
        self.categories = CategoryRepository(self.session)

    def begin(self):
        pass  # SQLAlchemy autostarts transaction

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def dispose(self):
        self.session.close()
