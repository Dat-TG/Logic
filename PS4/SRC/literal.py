class Literal:

    # Literal initialization
    def __init__(self, symbol="", negation=False):
        self.symbol = symbol
        self.negation = negation

    # Represent literal
    def __repr__(self):
        return '-{}'.format(self.symbol) if self.negation else self.symbol

    # Overload == operator
    def __eq__(self, other):
        return self.symbol == other.symbol and self.negation == other.negation

    # Hash literal
    def __hash__(self):
        s = '-' + self.symbol if self.negation else self.symbol
        return hash(s)

    # Overload < operator
    def __lt__(self, other) -> bool:
        if self.symbol != other.symbol:
            return self.symbol < other.symbol
        return self.negation < other.negation  # 0<1=>A<-A

    # Negate symbol
    def negate(self):
        self.negation = not self.negation

    # Check if opposite literals
    def is_opposite(self, literal):
        return self.symbol == literal.symbol and self.negation != literal.negation

    # Parse literal from string
    @staticmethod
    def parse_literal(literal_str):
        literal_str = literal_str.strip()
        literal = Literal(literal_str[1], True) if literal_str[0] == '-' else Literal(literal_str[0], False)
        return literal
