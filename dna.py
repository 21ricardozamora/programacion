from __future__ import annotations


class DNA:
    def __init__(self, sequence: str):
        self.sequence = sequence

    def __str__(self):
        return f'{self.sequence}'

    @property
    def adenines(self):
        ADENINES = 'A'

    @property
    def cytosines(self):
        CYTOSINES = 'C'

    @property
    def guanines(self):
        GUANINES = 'G'

    @property
    def thymines(self):
        THYMINES = 'T'

    def __add__(self, other: DNA):
        ...

    def __len__(self):
        return len(self.sequence)

    def stats(self) -> dict[str, float]:
        ...

    def __mul__(self, other):
        ...

    @classmethod
    def build_from_file(cls, path: str) -> DNA:
        ...

    def dump_to_file(self, path: str) -> None:
        ...

    def __getitem__(self, index: int) -> str:
        ...

    def __setitem__(self, index: int, base: str) -> None:
        ...
