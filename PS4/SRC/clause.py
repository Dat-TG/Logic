from literal import Literal


class Clause:

    # Clause initialization
    def __init__(self):
        self.literals = []

    # Represent clause
    def __repr__(self):
        return ' OR '.join(str(literal) for literal in self.literals) if len(self.literals) else '{}'

    # Remove duplicate literals and sort
    def unique_literals(self):
        self.literals = sorted(set(self.literals))

    # Overload == operator
    def __eq__(self, other):
        if len(self.literals) != len(other.literals):
            return False
        for index, element in enumerate(self.literals):
            if element != other.literals[index]:
                return False
        return True

    # Overload < operator
    def __lt__(self, other):
        if len(self.literals) != len(other.literals):
            return len(self.literals) < len(other.literals)
        for index, element in enumerate(self.literals):
            if element != other.literals[index]:
                return element < other.literals[index]

    # Hash clause
    def __hash__(self):
        return hash(tuple(self.literals))

    # Check if clause is empty
    def is_empty(self):
        return len(self.literals) == 0

    # Add literal into clause
    def add_literal(self, literal):
        self.literals.append(literal)

    # Negate a clause by negating all of its literals
    def negate(self):
        for literal in self.literals:
            literal.negate()

    # Check if clause is meaningless (example: A OR -A)
    def is_meaningless(self):
        for index in range(len(self.literals) - 1):
            if self.literals[index].is_opposite(self.literals[index + 1]):
                return True
        return False

    # Clone clause with exception
    def copy_clause_except(self, except_literal):
        clone = Clause()
        for literal in self.literals:
            if literal != except_literal:
                clone.add_literal(literal)
        return clone

    # Parse clause from string
    @staticmethod
    def parse_clause(clause_str):
        literal_str_list = clause_str.strip().split('OR')
        clause = Clause()
        for literal_str in literal_str_list:
            literal = Literal.parse_literal(literal_str)
            clause.add_literal(literal)
        clause.unique_literals()
        return clause

    # Merge two clauses
    @staticmethod
    def merge_clauses(clause_1, clause_2):
        clause = Clause()
        clause.literals = clause_1.literals + clause_2.literals
        clause.unique_literals()
        return clause

    # PL resolution Reference: Russell, S. J., & Norvig, P. (2020). Artificial intelligence: A modern approach (4th
    # ed.). Pearson Education Limited.
    @staticmethod
    def pl_resolve(clause_1, clause_2):
        is_empty = False
        resolvents = set()

        for literal_1 in clause_1.literals:
            for literal_2 in clause_2.literals:
                if literal_1.is_opposite(literal_2):
                    clause = Clause.merge_clauses(clause_1.copy_clause_except(literal_1),
                                                  clause_2.copy_clause_except(literal_2))
                    if clause.is_meaningless():
                        continue
                    if clause.is_empty():
                        is_empty = True
                    resolvents.add(clause)

        return resolvents, is_empty
