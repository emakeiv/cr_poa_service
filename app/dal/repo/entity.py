from typing import TypeVar, List, Generic, Optional
from app.dal.repo.interface import IRepository


T = TypeVar("T")

class RepositoryEntity(Generic[T], IRepository[T]):

    def __init__(self, entity, session):
        self.entity = entity
        self.session = session

    def get(self, **kwargs) -> Optional[T]:
        return self.session.query(self.entity).filter_by(**kwargs).first()

    def list(self, offset: int = None, limit: int = None, **query_conditions) -> List[T]:
        query = self.session.query(self.entity)

        for key, value in query_conditions.items():
            query = query.filter(getattr(self.entity, key) == value)

        if offset is not None:
            query = query.offset(offset)
        if limit is not None:
            query = query.limit(limit)

        return [entity.dict() for entity in query.all()]

    def add(self, entity) -> T:
        # entity_model = self.entity(**kwargs)
        self.session.add(entity)
        self.commit()
        #return entity_model

    def update(self, entity_id: int, **kwargs) -> Optional[T]:
        entity_model = self.session.query(
            self.entity).filter_by(id=entity_id).first()
        if entity_model:
            for key, value in kwargs.items():
                setattr(entity_model, key, value)
            self.commit()     
            return entity_model.dict()
        return None

    def delete(self, entity_id: int) -> None:
        entity_model = self.session.query(
            self.entity).filter_by(id=entity_id).first()
        if entity_model:
            self.session.delete(entity_model)
            self.commit()

    def bulk_insert(self, records: List[dict]) -> None:
        self.session.bulk_insert_mappings(self.entity, records)
        
    def commit(self):
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e   
    