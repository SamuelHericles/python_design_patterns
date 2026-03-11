from abc import ABC, abstractmethod


# ---- prototype/prototype.py
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass
