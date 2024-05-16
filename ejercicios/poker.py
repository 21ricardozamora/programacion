from __future__ import annotations


def load_card_glyphs(path: str = "cards.dat") -> dict[str, str]:
    """Retorna un diccionario donde las claves serán los palos
    y los valores serán cadenas de texto con los glifos de las
    cartas sin ningún separador"""
    with open(path, "r") as f:
        clean_cards = f.read().strip()
        for card in clean_cards.split(":"):
            index = clean_cards.find(":")
            first_cards_index = clean_cards[0:index]
            second_cards_index = clean_cards.replace(",", "")[index:]
        cards = {first_cards_index: second_cards_index for clean_cards in clean_cards}
    return cards


class Card:
    CLUBS = "♣"
    DIAMONDS = "◆"
    HEARTS = "❤"
    SPADES = "♠"
    #           1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13
    SYMBOLS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    A_VALUE = 1
    K_VALUE = 13
    GLYPHS = load_card_glyphs()
    FIGURES = (CLUBS, DIAMONDS, HEARTS, SPADES)
    VALUES = {"A": 1, "J": 11, "Q": 12, "K": 13}

    def __init__(self, value: int | str, suit: str):
        """Notas:
        - Si el suit(palo) no es válido hay que elevar una excepción de tipo
        InvalidCardError() con el mensaje: 🃏 Invalid card: {repr(suit)} is not a supported suit
        - Si el value(como entero) no es válido (es menor que 1 o mayor que 13) hay que
        elevar una excepción de tipo InvalidCardError() con el mensaje:
        🃏 Invalid card: {repr(value)} is not a supported value
        - Si el value(como string) no es válido hay que elevar una excepción de tipo
        🃏 Invalid card: {repr(value)} is not a supported symbol

        - self.suit deberá almacenar el palo de la carta '♣◆❤♠'.
        - self.value deberá almacenar el valor de la carta (1-13)"""
        if not isinstance(suit, str):
            raise InvalidCardError(
                f"🃏 Invalid card: {repr(suit)} is not a supported suit"
            )
        if isinstance(value, int):
            if value > Card.K_VALUE or value < Card.A_VALUE:
                raise InvalidCardError(
                    f"🃏 Invalid card: {repr(suit)} is not a supported suit"
                )
        elif isinstance(value, str):
            if value not in Card.SYMBOLS:
                raise InvalidCardError(
                    f"🃏 Invalid card: {repr(suit)} is not a supported suit"
                )
            value = Card.VALUES.get(value, int(value))
        self.suit = suit
        self.value = value

    @property
    def cmp_value(self) -> int:
        """Devuelve el valor (numérico) de la carta para comparar con otras.
        Tener en cuenta el AS."""
        if isinstance(self.value, str):
            if self.value in Card.VALUES:
                return Card.VALUES[self.value]
            return self.value

    def __repr__(self):
        """Devuelve el glifo de la carta"""
        return f"Card: {Card.GLYPHS}"

    def __eq__(self, other: Card | object):
        """Indica si dos cartas son iguales"""
        if self.value == other.value:
            return self.value

    def __lt__(self, other: Card):
        """Indica si una carta vale menos que otra"""
        if self.value < other.value:
            return self.value

    def __gt__(self, other: Card):
        """Indica si una carta vale más que otra"""
        if self.value < other.value:
            return other.value

    def __add__(self, other: Card) -> Card:
        """Suma de dos cartas:
        1. El nuevo palo será el de la carta más alta.
        2. El nuevo valor será la suma de los valores de las cartas. Si valor pasa
        de 13 se convertirá en un AS."""
        if self.value > other.value:
            new_suit = self.suit
        else:
            new_suit = other.suit
        new_value_sum = self.value + other.value
        if new_value_sum > Card.K_VALUE:
            new_value = "A"
        else:
            if new_value_sum in Card.VALUES.values():
                new_value = list(Card.VALUES.keys())[
                    list(Card.VALUES.values()).index(new_value_sum)
                ]
            else:
                new_value = str(new_value_sum)
        return Card(new_value, new_suit)

    def is_ace(self) -> bool:
        """Indica si una carta es un AS"""
        if self.value == "A":
            return True

    @classmethod
    def get_available_suits(cls) -> str:
        """Devuelve todos los palos como una cadena de texto"""
        return "".join(Card.FIGURES)

    @classmethod
    def get_cards_by_suit(cls, suit: str):
        """Función generadora que devuelve los glifos de las cartas por su palo"""
        if suit not in Card.FIGURES:
            raise InvalidCardError(
                f"🃏 Invalid card: {repr(suit)} is not a supported suit"
            )
        for card in Card.GLYPHS[suit]:
            yield card


class InvalidCardError(Exception):
    """Clase que representa un error de carta inválida.
    - El mensaje por defecto de esta excepción debe ser: 🃏 Invalid card
    - Si se añaden otros mensajes aparecerán como: 🃏 Invalid card: El mensaje que sea"""

    def __init__(self, msg: str = "🃏 Invalid card"):
        super().__init__(msg)  # Correcta llamada a la clase base 'Exception'
        self.msg = msg

    def __str__(self) -> str:
        return self.msg


a = Card(2, "◆")
print(a.GLYPHS.items())
