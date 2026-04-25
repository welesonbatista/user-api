from abc import ABC, abstractmethod

class UserFinderInterface(ABC):

    @abstractmethod
    def find_user(self, user_name: str) -> dict: pass