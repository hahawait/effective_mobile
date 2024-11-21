from uuid import uuid4

from typing import Literal


class Book:
    def __init__(
        self,
        title: str,
        author: str,
        year: int,
        id: str = str(uuid4()),
        status: Literal["в наличии", "выдана"] = "в наличии"
    ) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.id = id
        self.status = status

    def __str__(self) -> str:
        return f"\nКнига: {self.id}\nНазвание: {self.title}\nАвтор: {self.author}\nГод: {self.year}\nСтатус: {self.status}\n"
