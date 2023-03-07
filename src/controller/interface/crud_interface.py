from abc import ABC, abstractmethod
from typing import Any

class CrudInterface(ABC):

    @abstractmethod
    def run(self, **kwargs) -> Any:
        pass
