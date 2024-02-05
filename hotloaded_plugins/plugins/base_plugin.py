from abc import ABC, abstractmethod


class BasePlugin(ABC):
    @abstractmethod()
    def get_description(self) -> str:
        pass

    def get_name(self) -> str:
        return self.__class__.__name__
