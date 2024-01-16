from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Optional

T = TypeVar("T")

class IRepository(Generic[T], ABC):

    @abstractmethod
    def get(self, entity_id: int) -> Optional[T]:
        pass

    @abstractmethod
    def list(self) -> List[T]:
        pass

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def update(self, entity_id: int, entity):
        pass

    @abstractmethod
    def delete(self, entity_id: int):
        pass