from clause import Clause
from itertools import combinations


# PL Resolution Reference: Russell, S. J., & Norvig, P. (2020). Artificial intelligence: A modern approach (4th ed.).
# Pearson Education Limited.
def resolution(kb, alpha):
    steps = []
    entail = False
    alpha.negate()
    clauses = set(kb.clauses)
    clauses.add(alpha)

    while True:
        new_clauses = set()

        for (clause_i, clause_j) in combinations(sorted(clauses), 2):
            resolvents, is_empty = Clause.pl_resolve(clause_i, clause_j)
            new_clauses.update(resolvents)
            entail |= is_empty

        generated_clauses = sorted(new_clauses.difference(clauses))
        steps.append(generated_clauses)
        clauses.update(new_clauses)

        if entail:
            return True, steps
        if not generated_clauses:
            return False, steps
