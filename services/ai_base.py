from abc import ABC, abstractmethod


class AIBaseProvider(ABC):
    @abstractmethod
    def send_prompt(self, prompt: str) -> str:
        pass
