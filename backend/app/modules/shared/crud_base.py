from typing import TypeVar, List, Any, Generic, Type

ModelType = TypeVar("ModelType")


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_by_id(self, id_model: int) -> ModelType:
        pass

    def get_all(self, limit: int = 100) -> List[ModelType]:
        pass

    def create(self, obj: ModelType) -> ModelType:
        pass

    def update(self, obj: ModelType, id_model: int) -> ModelType:
        pass

    def delete(self, obj: ModelType) -> ModelType:
        pass

    def filter_by(self, field: str, value: Any) -> List[ModelType]:
        pass
