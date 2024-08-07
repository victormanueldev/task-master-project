from abc import ABC, abstractmethod
from typing import Any, Optional


class AuthPort(ABC):

    @abstractmethod
    def create_access_token(
        self, identity: Any, fresh: Optional[bool], additional_claims: Optional[Any]
    ) -> str:
        pass

    @abstractmethod
    def create_refresh_token(
        self, identity: Any, additional_claims: Optional[Any]
    ) -> str:
        pass
