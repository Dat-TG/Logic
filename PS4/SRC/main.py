from knowledge_base import KnowledgeBase
from clause import Clause
import glob
import os

from resolution import resolution

INPUT_DIR = './INPUT'
OUTPUT_DIR = './OUTPUT'


def main():
    input_dir = INPUT_DIR
    output_dir = OUTPUT_DIR

    inputs = glob.glob(input_dir + './*.txt')

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for index, input_file in enumerate(inputs):
        if '\\' in input_file:
            src = input_file.split('\\')[-1]
        else:
            src = input_file.split('/')[-1]

        file = open(input_file, 'r')
        kb = KnowledgeBase()
        alpha = Clause.parse_clause(file.readline())
        num_clauses = file.readline()
        clauses = file.readlines()
        KnowledgeBase.build_knowledge_base(kb, clauses)
        file.close()

        entail, new_clauses = resolution(kb, alpha)

        des = os.path.join(output_dir, src.replace('input', 'output'))
        file = open(des, 'w')
        for clauses in new_clauses:
            file.write('{}\n'.format(len(clauses)))
            for clause in clauses:
                file.write('{}\n'.format(clause))
        if entail:
            file.write('YES')
        else:
            file.write('NO')
        file.close()


if __name__ == '__main__':
    main()
