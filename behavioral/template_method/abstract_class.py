from abc import ABC, abstractmethod


# Class interface pode ter funções reais
class DataMiner(ABC):
    def mine(self, path: str) -> dict:
        """Template method"""
        raw = self.extract_data(path)
        parsed = self.parse_data(raw)
        analysis = self.analyze_data(parsed)
        self.send_report(analysis)
        return analysis

    @abstractmethod
    def extract_data(self, path: str) -> str:
        pass

    @abstractmethod
    def parse_data(self, raw: str) -> list:
        pass

    def analyze_data(self, data: list) -> dict:
        return {"count": len(data), "sample": data[:2]}

    def send_report(self, analysis: dict):
        print(f"  Relatório: {analysis}")
