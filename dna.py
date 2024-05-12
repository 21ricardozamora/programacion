from __future__ import annotations


class DNA:
    ADENINE = "A"
    CYTOSINE = "C"
    GUANINE = "G"
    THYMINE = "T"

    def __init__(self, sequence: str):
        self.sequence = sequence

    def __str__(self):
        return self.sequence

    @property
    def adenines(self) -> int:
        """Número de adeninas de la secuencia de ADN"""
        return self.sequence.count(DNA.ADENINE)

    @property
    def cytosines(self) -> int:
        """Número de citosinas de la secuencia de ADN"""
        return self.sequence.count(DNA.CYTOSINE)

    @property
    def guanines(self) -> int:
        """Número de guaninas de la secuencia de ADN"""
        return self.sequence.count(DNA.GUANINE)

    @property
    def thymines(self) -> int:
        """Número de timinas de la secuencia de ADN"""
        return self.sequence.count(DNA.THYMINE)

    def __add__(self, other: DNA) -> DNA:
        """Se define la suma de dos secuencias de ADN como el máximo de cada base nitrogenada
        (base a base). Por ejemplo 'T' sería mayor que 'A'.
        Si las secuencias no tienen la misma longitud, habrá que aplicar el máximo base a base
        hasta donde se pueda, y completar el resto de la secuencia con la parte que falte, bien
        de la primera o bien de la segunda secuencia, en función de cuál sea mayor.
        """
        ...

    def __len__(self):
        """Longitud de la secuencia de ADN"""
        return len(self.sequence)

    def stats(self) -> dict[str, float]:
        """Porcentaje de aparición de cada base con respecto al total.
        Se devuelve un diccionario donde la clave será la base nitrogenada
        y el valor será el porcentaje."""
        dna = {
            DNA.ADENINE: self.sequence.count(DNA.ADENINE) / len(self.sequence) * 100,
            DNA.GUANINE: self.sequence.count(DNA.GUANINE) / len(self.sequence) * 100,
            DNA.THYMINE: self.sequence.count(DNA.THYMINE) / len(self.sequence) * 100,
            DNA.CYTOSINE: self.sequence.count(DNA.CYTOSINE) / len(self.sequence) * 100,
        }
        return dna

    def __mul__(self, other: DNA) -> DNA:
        """Se define la multiplicación de dos secuencias de ADN como una nueva cadena
        de ADN donde aparecen las bases que son iguales (posición a posición)"""
        ...

    @classmethod
    def build_from_file(cls, path: str) -> DNA:
        """Construye una secuencia de ADN a partir de un fichero.
        El formato del fichero es tener una única línea con todas las bases
        una detrás de otra."""
        with open(path, "r") as f:
            sequence = f.readline().strip()
            new_sequence = DNA(sequence)
        return new_sequence

    def dump_to_file(self, path: str) -> None:
        """Vuelca una secuencia de ADN a un fichero de salida.
        El formato del fichero es tener una única línea con todas las bases
        una detrás de otra."""
        with open(path, "w") as f:
            for _ in self.sequence:
                f.write(_)
        return f

    def __getitem__(self, index: int) -> str:
        """Devuelve la base que ocupa la posición 'index'"""
        return self.sequence[index]

    def __setitem__(self, index: int, base: str) -> None:
        """Fija la base 'base' en la posición 'index'
        NOTA: Si la base que se va a asignar no es ninguna de las 4 bases
        habituales, hay que asignar ADENINA."""
        new_sequence = ""
        if isinstance(base, str):
            if base not in (DNA.ADENINE, DNA.CYTOSINE, DNA.THYMINE, DNA.GUANINE):
                base = DNA.ADENINE
            new_sequence += self.sequence[0:index] + base + self.sequence[index:]
        else:
            new_sequence[index] = base
        return new_sequence
