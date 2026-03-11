# ---- singleton/singleton.py
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connected = False
            cls._instance._url = None
        return cls._instance

    def connect(self, url: str):
        if not self._connected:
            self._url = url
            self._connected = True
            print(f"  Conectado a: {url}")
        else:
            print(f"  Já conectado a: {self._url}")

    def query(self, sql: str) -> str:
        return f"  Resultado de: {sql}"
