class UnicornException(Exception):
    def __init__(self, name: str, status: int | None = 500):
        self.name = name
        self.status = status
