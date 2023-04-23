from clause import Clause


class KnowledgeBase:

    # Knowledge Base Initialization
    def __init__(self):
        self.clauses = []

    # Add a clause to Knowledge Base
    def add_clause(self, clause):
        self.clauses.append(clause)

    # Build the Knowledge Base from a list of clause string
    @staticmethod
    def build_knowledge_base(kb, clause_str_list):
        for clause_str in clause_str_list:
            clause = Clause.parse_clause(clause_str)
            clause.unique_literals()
            kb.add_clause(clause)
