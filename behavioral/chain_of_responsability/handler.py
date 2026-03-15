from abc import ABC, abstractmethod


class SupportHandler(ABC):
    def __init__(self):
        self._next: SupportHandler = None

    def set_next(self, handler: "SupportHandler") -> "SupportHandler":
        self._next = handler
        return handler

    @abstractmethod
    def handle(self, level: int, issue: str) -> str:
        pass

    def _pass_to_next(self, level: int, issue: str) -> str:
        if self._next:
            return self._next.handle(level, issue)
        return f"  Sem handler para nível {level}: {issue}"
